from DataBase.DBInsert import database
import datetime

class insert:
    def __init__(self):
        self.db = database()
    def insert_user(self):
        try:
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone: ")
            address = input("Enter Address: ")
            city = input("Enter City: ")
            registration_date = datetime.datetime.now().strftime("%Y-%m-%d")
            self.db.add_user(name, email, phone, address, city, registration_date)
        except Exception as e:
            print("Error inserting user:", e)

    def disply_menu(self):
        data = self.db.display()
        if not data:
            print("Menu is empty")
        else:
            print("Complete Menu:")
        for row in data:
            print(row)

    def updatemenu(self):
        item_name = input("Enter Item Name: ")
        new_price = input("Enter New Price: ")
        try:
            new_price = float(new_price)
        except ValueError:
            print("❌ Invalid price entered. Please enter a valid number.")
            return
        self.db.update_menu(item_name, new_price)
        print(f"✅ Menu updated successfully for '{item_name}' with new price: {new_price}")


def menu(self):
        while True:
            choice = input("""
            1. Show Menu
            2. Add Item
            """)

if __name__ == "__main__":
    insert_obj = insert()
    insert_obj.updatemenu()
