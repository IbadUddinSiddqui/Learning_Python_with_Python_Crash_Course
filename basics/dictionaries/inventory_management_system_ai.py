def display_menu():
    print("\n=== Inventory Management System ===")
    print("1. View all items")
    print("2. Add new item")
    print("3. Update stock")
    print("4. Remove item")
    print("5. View item details")
    print("6. Exit")

def view_all_items(inventory):
    print("\n=== Current Inventory ===")
    if not inventory:
        print("Inventory is empty!")
        return
    
    for item, details in inventory.items():
        print(f"{item}: {details['quantity']} in stock - ${details['price']}")

def add_item(inventory):
    name = input("Enter item name: ").lower()
    if name in inventory:
        print("Item already exists!")
        return
    
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: $"))
        description = input("Enter description: ")
        
        inventory[name] = {
            "quantity": quantity,
            "price": price,
            "description": description
        }
        print(f"\n{name.title()} has been added to inventory.")
    except ValueError:
        print("Invalid input! Please enter numbers for quantity and price.")

def update_stock(inventory):
    name = input("Enter item name: ").lower()
    if name not in inventory:
        print("Item not found!")
        return
    
    try:
        new_quantity = int(input("Enter new quantity: "))
        inventory[name]["quantity"] = new_quantity
        print(f"\nStock updated for {name.title()}")
    except ValueError:
        print("Invalid input! Please enter a number for quantity.")

def remove_item(inventory):
    name = input("Enter item name to remove: ").lower()
    if name in inventory:
        del inventory[name]
        print(f"\n{name.title()} has been removed from inventory.")
    else:
        print("Item not found!")

def view_item_details(inventory):
    name = input("Enter item name: ").lower()
    if name in inventory:
        item = inventory[name]
        print(f"\n=== {name.title()} Details ===")
        print(f"Quantity: {item['quantity']}")
        print(f"Price: ${item['price']}")
        print(f"Description: {item['description']}")
    else:
        print("Item not found!")

def main():
    # Sample inventory
    inventory = {
        "apple": {"quantity": 100, "price": 0.50, "description": "Fresh red apples"},
        "banana": {"quantity": 150, "price": 0.30, "description": "Yellow bananas"},
        "orange": {"quantity": 75, "price": 0.60, "description": "Juicy oranges"}
    }
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            view_all_items(inventory)
        elif choice == "2":
            add_item(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            remove_item(inventory)
        elif choice == "5":
            view_item_details(inventory)
        elif choice == "6":
            print("\nThank you for using the Inventory Management System!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
