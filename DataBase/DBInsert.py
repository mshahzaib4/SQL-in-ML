# Using Python, insert a new user into the users table by taking input from keyboard.
import sys
import mysql.connector

class database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "restaurant_management"
        )
            self.mycursor = self.conn.cursor()
            print("Connected to Database Successfully")
        except Exception as e:
            print("Error: Could not connect to database ->", e)
            sys.exit(0) 

    def add_user(self, name, email, phone, address, city, registration_date):
            try :
                query = """ Insert INTO customers (
                
                name,
                email,
                phone,
                address,
                city,
                registration_date
                ) values (%s, %s, %s, %s, %s, %s) """ 
                value = (name, email, phone, address, city, registration_date )
                self.mycursor.execute(query, value)
                self.conn.commit()
                print("Record added successfully!")

            except Exception as e:
                print(f"Insert failed: {e}")