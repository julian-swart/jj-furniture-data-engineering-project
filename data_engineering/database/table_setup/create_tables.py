import psycopg2
from sql_queries import create_table_queries, drop_table_queries
import configparser

ENCODING='utf-16'

def drop_tables(cur, conn):
    """
    Loops through list of drop table queries
    and drops tables listed in sql_queries.py
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """"
    Loops through list of create table queries
    and creates tables listed in sql_queries.py
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main(args):
    """
    Drops and creates tables as outlined in sql_queries.py
    You will need the following information in your config.init file:
    
    HOST
    USER
    PASSWORD
    DATABASE
    """
    config = configparser.ConfigParser()
    config.read(args, encoding=ENCODING)
    HOST=config.get('jj-furniture','host')
    USER=config.get('jj-furniture','user')
    PASSWORD=config.get('jj-furniture','password')
    DATABASE=config.get('jj-furniture','database')
    
    try:
        conn = psycopg2.connect(host=HOST, user=USER, password=PASSWORD, dbname=DATABASE)
        cur = conn.cursor()
    
        #drop_tables(cur, conn)
        create_tables(cur, conn)
    
    except Exception as e:
        print(e)
        
    finally:
        conn.close()


if __name__ == "__main__":
    import sys
    main(sys.argv[1])
