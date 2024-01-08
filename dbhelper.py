#!/usr/bin/python
import psycopg2
from config import config

class DbConnection:

    conn = None
    def getConnection(self):
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            return cur
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def getDataByQuery(self,sqlstatementquery):
        try:
            cur = self.getConnection()
            cur.execute(sqlstatementquery)
            result = cur.fetchone()
            return result
        except (Exception) as error:
            print(error)             

    def getDataByProcedure(self,procedurename,params:list = None):
        try:
            cur = self.getConnection()
            cur.callproc(procedurename,params)
            result = cur.fetchall()
            return result
        except (Exception) as error:
            print(error)    

                                 