from collections import OrderedDict
import os

class GroceryListOrganizer:
    def __init__(self, filename="grocery_list.txt"):
        self.grocery_list = OrderedDict()
        self.filename = filename
        self.load_list_from_file()

    def add_item(self, item, quantity):
        """Add an item to the grocery list with its quantity."""
        self.grocery_list[item] = quantity
        print(f"Added {item} with quantity {quantity}.")

    def remove_item(self, item):
        """Remove an item from the grocery list."""
        if item in self.grocery_list:
            del self.grocery_list[item]
            print(f"Removed {item}.")
        else:
            print(f"{item} is not in the grocery list.")

    def view_list(self):
        """Display the current grocery list."""
        if self.grocery_list:
            print("\nCurrent Grocery List:")
            for item, quantity in self.grocery_list.items():
                print(f"{item}: {quantity}")
        else:
            print("Your grocery list is empty.")

    def update_quantity(self, item, new_quantity):
        """Update the quantity of an existing item."""
        if item in self.grocery_list:
            self.grocery_list[item] = new_quantity
            print(f"Updated {item} quantity to {new_quantity}.")
        else:
            print(f"{item} is not in the grocery list.")

    def clear_list(self):
        """Clear the entire grocery list."""
        self.grocery_list.clear()
        print("All items have been removed from your grocery list.")

    def save_list_to_file(self):
        """Save the grocery list to a file."""
        try:
            with open(self.filename, "w") as file:
                for item, quantity in self.grocery_list.items():
                    file.write(f"{item},{quantity}\n")
            print(f"\nGrocery list saved to file: {self.filename}")
        except Exception as e:
            print(f"Error saving the file: {e}")

    def load_list_from_file(self):
        """Load the grocery list from a file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    for line in file:
                        item, quantity = line.strip().split(",")
                        self.grocery_list[item] = int(quantity)
                print(f"\nGrocery list loaded from file: {self.filename}")
            except Exception as e:
                print(f"Error loading the file: {e}")
        else:
            print(f"\nNo grocery list file found. Starting fresh!")

def main():
    organizer = GroceryListOrganizer()

    while True:
        print("\n--- Grocery List Organizer ---")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Update item quantity")
        print("5. Clear list")
        print("6. Save list to file")
        print("7. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            item = input("Enter the item: ")
            quantity = input(f"Enter the quantity of {item}: ")
            try:
                quantity = int(quantity)
                organizer.add_item(item, quantity)
            except ValueError:
                print("Please enter a valid number for quantity.")
        
        elif choice == "2":
            item = input("Enter the item to remove: ")
            organizer.remove_item(item)

        elif choice == "3":
            organizer.view_list()

        elif choice == "4":
            item = input("Enter the item to update: ")
            new_quantity = input(f"Enter the new quantity for {item}: ")
            try:
                new_quantity = int(new_quantity)
                organizer.update_quantity(item, new_quantity)
            except ValueError:
                print("Please enter a valid number for quantity.")

        elif choice == "5":
            organizer.clear_list()

        elif choice == "6":
            organizer.save_list_to_file()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
