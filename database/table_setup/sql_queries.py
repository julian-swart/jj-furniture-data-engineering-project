# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 09:43:39 2020

@author: jonathan
"""

# DROP TABLES
drop_customer_table = "DROP TABLE IF EXISTS customers"

drop_product_table = "DROP TABLE IF EXISTS products"

# CREATE TABLES
create_customer_table = """
CREATE TABLE IF NOT EXISTS customers
(
     customer_id    BIGINT PRIMARY KEY,
     first_name     VARCHAR(20),
     last_name      VARCHAR(20),
     email_address  VARCHAR(50),
     dob            DATE,
     gender         VARCHAR(8),
     street_address VARCHAR(50),
     state          VARCHAR(50),
     date_created   DATE,
     create_source  VARCHAR(50)
 )
"""

create_product_table = """
CREATE TABLE IF NOT EXISTS products
(
     product_code       BIGINT PRIMARY KEY,
     manufacturer_id    INT,
     brand_id           INT,
     material_id        INT,
     material_type_id   INT,
     color_id           INT,
     state_id           INT,
     description        VARCHAR(100),
     number_of_pieces   DATE,
     cost               NUMERIC
 )
"""

# INSERT QUERIES
insert_customer_table = """
REPLACE INTO customers (customer_id, first_name, last_name, email_address, \
dob, gender, street_address, state, date_created, create_source)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

insert_product_table = """
REPLACE INTO products (product_code, manufacturer_id, brand_id, material_id, \
material_type_id, color_id, state_id, state, description, number_of_pieces, cost)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# QUERY LISTS
drop_table_queries = [drop_customer_table, drop_product_table]
create_table_queries = [create_customer_table, create_product_table]
insert_table_queries = [insert_customer_table, insert_product_table]
