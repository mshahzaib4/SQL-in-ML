## Build a small Python script that manages restaurant menu data stored in MySQL.
## You’ll perform the four CRUD operations (Create, Read, Update, Delete) using Python code.

from DataBase.DB_Restaurant_Menu_Management import BDHELPER
import sys

class _Restaurant_Menu_Management:
    def __init__(self):
        self.db = BDHELPER()
        self.menu()

    def menu(self):
        while True:
            choice = input("""
            1. Show Menu
            2. Add Item
            3. Update Item
            4. Delete Item
            5. Exit
            """)

            if choice.strip() == "1":
                data = self.db.show_menu()
                if not data:
                    print("Menu is empty")
                else:
                    print("Complete Menu:")
                    for row in data:
                        print(row)

            elif choice.strip() == "2":
                data = self.db.add_item()
                if not data:
                    print("It is Already exist!")
                else:
                    print("Enter Item Successfull")
            else:
                print("Invalid choice. Enter 1 to show menu.")    


if __name__ == "__main__":
    _Restaurant_Menu_Management()