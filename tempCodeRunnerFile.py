    def updatemenu(self):
        # ✅ Take input from the user
        item_name = input("Enter Item Name: ")
        new_price = input("Enter New Price: ")

        # ✅ Validate the new price
        try:
            new_price = float(new_price)
        except ValueError:
            print("❌ Invalid price entered. Please enter a valid number.")
            return

        # ✅ Update the menu in the database
        self.db.update_menu(item_name, new_price)
        print(f"✅ Menu updated successfully for '{item_name}' with new price: {new_price}")
