# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 15:34:59 2020

@author: jonathan
"""

import psycopg2
import pandas as pd
from configparser import ConfigParser

class PostgresConnector(section):
    '''Used for creating connection to MySQL database.
    Has methods for pulling data and performing database
    updates'''
    
    def __init__(self, config_file_path='config.ini', section=section):
        '''Initialize connection to MySQL database.
        This requires a config file with named section
        containing the following fields:
        HOST, PORT, USER, PASSWORD, DATABASE'''
        cf = ConfigParser()
        cf.read(config_file_path)

        self.db_host = cf.get(section, 'HOST')
        self.db_port = cf.getint(section, 'PORT')
        self.db_user = cf.get(section, 'USER')
        self.db_pwd = cf.get(section, 'PASSWORD')
        self.db_name = cf.get(section,'DATABASE')
        self._connect = psycopg2.connect(host=self.db_host, 
                                        port=int(self.db_port), 
                                        user=self.db_user, 
                                        password=self.db_pwd, 
                                        charset='UTF8MB4',
                                        db=self.db_name)
    
    def queryall(self, sql, params=None, return_df=True):
        '''Executes SQL query and returns the fetched dataset'''
        cursor = self._connect.cursor()
        try:
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            result = cursor.fetchall()
            columns = [cursor.description[i][0] for \
                       i in range(len(cursor.description))]
        except pymysql.MySQLError as e:
            print(e)
        finally:
            cursor.close()
        if return_df == True:
            return pd.DataFrame(result,columns=columns)
        else:
            return result
    
    def update(self, sql, params=None):
        '''Executes SQL queries used for updating database
        such as insert and update (CRUD operations)'''
        cursor = self._connect.cursor()
        try:
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            self._connect.commit()
        except pymysql.MySQLError as e:
            print(e)
        finally:
            cursor.close()
            
    def close(self):
        '''Close connection to MySQL database'''
        if self._connect:
            self._connect.close()
