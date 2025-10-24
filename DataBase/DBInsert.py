# Using Python, insert a new user into the users table by taking input from keyboard.
# Using Python, display all menu items in a formatted output.
# Update the price of a menu item using Python input.

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

    def display(self):
         query = "Select * FROM menu"
         self.mycursor.execute(query)
         result = self.mycursor.fetchall()
         if result:
              return result
         else:
              return 0


    def update_menu(self, item_name, new_price):
         try:
              update_query = "UPDATE menu SET price = %s WHERE item_name = %s"
              value = (new_price, item_name)
              self.mycursor.execute(update_query, value)
              self.conn.commit()
              if self.mycursor.rowcount > 0:
                   print( f"Price updated successfully for '{item_name}'") 
              else:
                    print(f"⚠️ No menu item found with name '{item_name}'.")
         except Exception as e:
            print(f"Update failed: {e}")    