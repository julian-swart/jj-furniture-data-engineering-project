
# DROP TABLES
drop_customer_table = "DROP TABLE IF EXISTS customers"

drop_product_table = "DROP TABLE IF EXISTS products"

drop_material_table = "DROP TABLE IF EXISTS materials"

drop_color_table = "DROP TABLE IF EXISTS colors"

drop_description_table = "DROP TABLE IF EXISTS desription"

drop_transactions_table = "DROP TABLE IF EXISTS transactions"

# CREATE TABLES
create_customer_table = """
CREATE TABLE IF NOT EXISTS customers
(
     customer_id    SERIAL PRIMARY KEY,
     first_name     VARCHAR(200),
     last_name      VARCHAR(200),
     email_address  VARCHAR(200),
     dob            DATE,
     gender         VARCHAR(100),
     street_address VARCHAR(1000),
     state          VARCHAR(20),
     date_created   DATE,
     create_source  VARCHAR(100)
 )
"""

create_product_table = """
CREATE TABLE IF NOT EXISTS products
(
     product_id       SERIAL PRIMARY KEY,
     material_id      INT,
     color_id         INT,
     description_id   INT,
     pieces           INT,
     cost             NUMERIC
 )
"""

create_material_table = """
CREATE TABLE IF NOT EXISTS materials
(
     material_id      SERIAL PRIMARY KEY,
     material_desc    VARCHAR(1000)
 )
"""

create_color_table = """
CREATE TABLE IF NOT EXISTS colors
(
     color_id       SERIAL PRIMARY KEY,
     color_desc     VARCHAR(1000)
 )
"""

create_description_table = """
CREATE TABLE IF NOT EXISTS descriptions
(
     description_id          SERIAL PRIMARY KEY,
     product_description     VARCHAR(1000)
 )
"""

create_transactions_table = """
CREATE TABLE IF NOT EXISTS transactions
(
     id                  SERIAL PRIMARY KEY,
     transaction_id          INT,
     transaction_date        DATE,
     customer_id             INT,
     product_id              INT,
     line_item_number        SMALLINT,
     sale_amount             NUMERIC(20),
     quantity                SMALLINT,
     sale_or_return          INT
 )
"""

# INSERT QUERIES
insert_customer_table = """
INSERT INTO customers (first_name, last_name, email_address,
dob, gender, street_address, state, date_created, create_source)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

insert_product_table = """
INSERT INTO products (material_id, color_id, description_id, pieces, cost)
VALUES (%s, %s, %s, %s, %s)
"""

insert_material_table = """
INSERT INTO materials (material_desc)
VALUES (%s)
"""

insert_color_table = """
INSERT INTO colors (color_desc)
VALUES (%s)
"""

insert_description_table = """
INSERT INTO descriptions (product_description)
VALUES (%s)
"""

insert_transactions_table = """
INSERT INTO transactions (transaction_id, transaction_date, customer_id, product_id, line_item_number, sale_amount, quantity, sale_or_return)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

# QUERY LISTS
drop_table_queries = [drop_customer_table, drop_product_table, drop_material_table, drop_color_table, drop_description_table, drop_transactions_table]
create_table_queries = [create_customer_table, create_product_table, create_material_table, create_color_table, create_description_table, create_transactions_table]
insert_table_queries = [insert_customer_table, insert_product_table, insert_material_table, insert_color_table, insert_description_table, insert_transactions_table]
