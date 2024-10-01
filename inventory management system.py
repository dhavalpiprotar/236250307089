inventory = {}
def add_item():
    item = input("Enter item name: ")
    if item in inventory:
        print(f"{item} already exists.")
    else:
        quantity = int(input(f"Enter quantity of {item}: "))
        price = float(input(f"Enter price of {item}: "))
        inventory[item] = {'quantity': quantity, 'price': price}
        print(f"{item} added to inventory.")

def remove_item():
    item = input("Enter the name of the item to remove: ")
    if item in inventory:
        del inventory[item]
        print(f"{item} removed from inventory.")
    else:
        print(f"{item} does not exist in inventory.")

def update_item():
    item = input("Enter the name of the item to update: ")
    if item in inventory:
        quantity = int(input(f"Enter new quantity of {item}: "))
        price = float(input(f"Enter new price of {item}: "))
        inventory[item]['quantity'] = quantity
        inventory[item]['price'] = price
        print(f"{item} updated.")
    else:
        print(f"{item} does not exist in inventory.")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        for item, details in inventory.items():
            print(f"Item: {item}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}")

def save_inventory():
    with open('inventory.txt', 'w') as f:
        for item, details in inventory.items():
            f.write(f"{item},{details['quantity']},{details['price']}\n")
    print("Inventory saved to inventory.txt")

def load_inventory():
    try:
        with open('inventory.txt', 'r') as f:
            for line in f:
                item, quantity, price = line.strip().split(',')
                inventory[item] = {'quantity': int(quantity), 'price': float(price)}
        print("Inventory loaded from inventory.txt")
    except FileNotFoundError:
        print("Inventory file not found. Starting with an empty inventory.")

def menu():
    while True:
        print("\nInventory Management System")
        print("NAME:-PIPROTAR DHAVAL,PARMAR PRAHLAD,RAJ SOLANKI")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. View Inventory")
        print("5. Save Inventory")
        print("6. Load Inventory")      
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            update_item()
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            save_inventory()
        elif choice == '6':
            load_inventory()
        elif choice == '7':
            print("Exiting......")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
