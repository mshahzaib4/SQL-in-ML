## Build a small Python script that manages restaurant menu data stored in MySQL.
## You’ll perform the four CRUD operations (Create, Read, Update, Delete) using Python code.

import mysql.connector
import sys

class BDHELPER():
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database ="restaurant_management"
            )
            self.mycursor = self.conn.cursor()
            print("Connected to Database Successfully")
        except Exception as e:
            print("Error: Could not connect to database ->", e)
            sys.exit(0)   

    def show_menu(self):
        try:
            query = "SELECT * FROM menu"  
            self.mycursor.execute(query)
            result = self.mycursor.fetchall()
            if result:
                return result
            else:
                return  None
        except mysql.connector.Error as err:
            print("Database error ", err)

    def add_item(self):
        print()


            