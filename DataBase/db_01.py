import mysql.connector
import sys

class DBHELPER:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='class'
            )
            self.mycursor = self.conn.cursor()
            print("Connected to Database Successfully")
        except Exception as e:
            print("Error: Could not connect to database ->", e)
            sys.exit(0)

    def register(self, name, email, password):
        try:
            query = "INSERT INTO user (name, email, password) VALUES (%s, %s, %s)"            
            values = (name, email, password)
            self.mycursor.execute(query, values)
            self.conn.commit()
            return 1
        except mysql.connector.Error as err:
            print("Database Error:", err)
            return -1
        
    def login(self, email, password):
        try:
            query = "SELECT * FROM user WHERE email=%s AND password=%s"
            values = (email, password)
            self.mycursor.execute(query, values)
            result = self.mycursor.fetchone()
            if result:
                return result
            else:
                return  None
            
        except mysql.connector.Error as err:
            print("Database error ", err)    