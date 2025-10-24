# Write Python code to connect to your MySQL database. 
import sys
import mysql.connector

class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = '',
                database = 'restaurant_management'
            )
            print("Connected to Database Successfully")
        except Exception as e:
            print("Error: Could not connect to database ->", e)
            sys.exit(0)        