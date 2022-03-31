# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 09:43:39 2020

@author: jonathan
"""

# DROP TABLES
drop_customer_table = "DROP TABLE IF EXISTS customers"

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

# INSERT QUERIES
insert_customer_table = """
REPLACE INTO customers (customer_id, first_name, last_name, email_address, \
dob, gender, street_address, state, date_created, create_source)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# QUERY LISTS
drop_table_queries = [drop_customer_table]
create_table_queries = [create_customer_table]
insert_table_queries = [insert_customer_table]

