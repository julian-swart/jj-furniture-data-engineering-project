
# import

import sys 
import os
import configparser
import pandas as pd
import numpy as np
import datetime as dt
from faker import Faker
from sqlalchemy import create_engine

# importing custom modules from upper directories

script_dir = os.path.abspath('')
mymodule_dir = os.path.join( script_dir, '..', '..', 'database', 'table_setup' )
sys.path.append( mymodule_dir )

import sql_queries

mymodule_dir = os.path.join( script_dir, '..', '..', 'database', 'connection' )
sys.path.append( mymodule_dir )

import postgres_db


# connect to database 

encoding = 'utf-16'

config_file_path = os.path.join( script_dir, '..', '..', 'database', 'connection' )
config_file_path += '/config.ini'

db_conn = postgres_db.PostgresConnector(config_file_path = config_file_path,
                                       section = 'jj-furniture',
                                       encoding = encoding)


# insert data: colors

color_list = ['grey', 'dark grey', 'red', 'blue', 'green', 'black', 'brown', 'beige', 'white', 'yellow']

for color in color_list:
    db_conn.update(sql_queries.insert_color_table, [color])


# insert data: descriptions

description_list = ['sofa', 'love-seat', 'dinette set', 'mattress', 'bedframe', 'nightstand', 'chest', 'dresser', 'chair', 'desk', 'desk chair', 'bookcase', 'coffee table', 'end table'] 

for description in description_list:
    db_conn.update(sql_queries.insert_description_table, [description])


# insert data: materials

material_list = ['fabric', 'leather', 'wood', 'metal', 'plastic']

for material in material_list:
    db_conn.update(sql_queries.insert_material_table, [material])


# insert data: products

def get_ids(table_name):
    
    query = '''
    select {}_id
    from {}
    '''
    
    results = db_conn.queryall(query.format(table_name[:-1], table_name))
    
    return results[results.columns[0]].values.tolist()


material_ids = get_ids('materials')
color_ids = get_ids('colors')
description_ids = get_ids('descriptions')

products = [
    {
     'material_id': np.random.choice(material_ids),
     'color_id': np.random.choice(color_ids),
     'description_id': np.random.choice(description_ids),
     'pieces': np.random.randint(low = 1, high = 8, size = 1)[0],
     'cost': np.round(np.random.lognormal(mean = np.log(100), sigma = 1, size = 1)[0],2) # make sure to give same cost to manufacturer 
    }
    for x in range(200)
]

df_products = pd.DataFrame(products)


for i, row in df_products.iterrows():
    if i % 100 == 0:
        print(i)
    db_conn.update(sql_queries.insert_product_table, 
                        (row['material_id'],
                        row['color_id'],
                        row['description_id'],
                        row['pieces'],
                        row['cost'])
                  )

    
# insert data: customers

fake = Faker()
store_type = ['Store', 'Web']
num_customers = 10000

customers = [
    {
     'first_name': fake.first_name(),
     'last_name': fake.last_name(),
     'email_address': fake.email(),
     'dob': fake.date_between(start_date ='-70y', end_date = '-18y'),
     'gender': fake.profile()['sex'],
     'street_address': fake.street_address(),
     'state': fake.random_element(elements = ('NC', 'SC', 'TN', 'FL', 'GA', 'MS', 'AL')),
     'date_created': fake.date_between(start_date ='-12y'),
     'create_source': np.random.choice(store_type, p = [.8, .2]) # can give probability of selection to Store Type
    }
    for x in range(1, num_customers+1)
]


df_customers = pd.DataFrame(customers)

for i, row in df_customers.iterrows():
    if i % num_customers*.25 == 0:
        print(i)
    db_conn.update(sql_queries.insert_customer_table, 
                        (row['first_name'],
                        row['last_name'],
                        row['email_address'],
                        row['dob'],
                        row['gender'],
                        row['street_address'],
                        row['state'],
                        row['date_created'],
                        row['create_source'])
                  )

    
# insert data: transactions

def get_cost(product):
    
    query = '''
    select cost
    from products
    where product_id = {}
    '''
    
    return float(db_conn.queryall(query.format(product))['cost'][0])


customer_id_list = get_ids('customers')
product_id_list = get_ids('products')

num_trans = 25000
transaction_id = 1
years = list(range(2010, 2023))
weights = list(range(1, len(years) + 1))
weights = [x/sum(weights) for x in weights]

for trans in range(num_trans):
    
    if transaction_id % num_trans*.25 == 0:
        print(i)
    
    num_items = np.random.randint(low = 1, high = 5)
    year = np.random.choice(years, size = None, p = weights)
    transaction_date = fake.date_between_dates(date_start = dt.datetime.strptime(str(year) + '-01-01', '%Y-%m-%d'), date_end = dt.datetime.strptime(str(year) + '-12-31', '%Y-%m-%d'))
    customer_id = np.random.choice(customer_id_list).item()
    
    for item in range(num_items): 
        
        
        product_id = np.random.choice(product_id_list).item()
        line_item_number = item + 1
        sale_or_return = 0
        
        sale_amount = round(get_cost(product_id) * np.random.uniform(low = 1.43, high = 4), 2)
        quantity = np.random.choice([1,2,3], p = [.8, .15, .05]).item()
        
        db_conn.update(sql_queries.insert_transactions_table,
                          (transaction_id,
                          transaction_date,
                          customer_id,
                          product_id,
                          line_item_number,
                          sale_amount,
                          quantity,
                          sale_or_return))
                          
    transaction_id += 1                         

