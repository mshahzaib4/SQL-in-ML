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


if __name__ == "__main__":
    insert_obj = insert()
    insert_obj.insert_user()
