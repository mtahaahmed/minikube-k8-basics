import mysql.connector
import os
class database():
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.hostname = os.getenv("MYSQL_SERVICE_HOST")
        self.username = "root"
        self.db ="pythonApp"
        self.password = os.getenv("MYSQL_DB_PASSWORD")

    def makeConnSQL(self):
        self.conn = mysql.connector.Connect(host=self.hostname, user=self.username, passwd=self.password, db=self.db)
        self.cursor = self.conn.cursor()

    def closeConn(self):
        self.conn.close()

    def getData(self):
        try:
            self.makeConnSQL()
        except Exception as e:
            print ("ERROR: An exception while making connection to SQL in getData e = " + str(e))
            #raise
            return False
        sql= 'SELECT word from data'
        try:
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            print("Data has been fetched")
            # self.conn.commit()
        except Exception as e:
            print ("ERROR in getData :  " + str(e))
            # raise
            return False
        self.closeConn()
        return str(records[0][0])
