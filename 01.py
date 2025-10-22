import sys
from DataBase.db_01 import DBHELPER

class Flipkart:
    def __init__(self):
        self.db = DBHELPER()
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
1. Enter 1 to register
2. Enter 2 to login
3. Anything else to leave
Your choice: """)

            if user_input == "1":
                self.register()
            elif user_input == "2":
                self.login()
            else:
                print("Exiting program...")
                sys.exit(0)

    def register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        response = self.db.register(name, email, password)
        if response == 1:
            print(" Registration Successful!")
        else:
            print(" Registration Failed!")
        self.menu()

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        data = self.db.login(email, password)

        if len(data) == 0:
            print("Incorrect Email / Password")
            self.login()
        else:
            print("Hello", data[1],"and your user id is ", data[0])
