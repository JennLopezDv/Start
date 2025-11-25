# inventory.py
# All inventory CRUD operations.

import json
from utils import validate_positive_int, validate_positive_float

INVENTORY_FILE = "inventory.json"

# -------------------------------
# Load and save inventory
# -------------------------------
def load_inventory():
    try:
        with open(INVENTORY_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Inventory file not found. A new one will be created.")
        return {}

def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent=4)
    print("Inventory saved successfully.")


# -------------------------------
# Create product
# -------------------------------
def create_product(inventory):
    title = input("Enter book title: ").lower()
    if title in inventory:
        print("Error: this product already exists.")
        return inventory
    
    author = input("Enter author: ").lower()
    category = input("Enter category: ").lower()

    try:
        price = validate_positive_float(input("Enter price: "))
        stock = validate_positive_int(input("Enter stock quantity: "))
    except ValueError as e:
        print(e)
        return inventory

    inventory[title] = {
        "author": author,
        "category": category,
        "price": price,
        "stock": stock
    }

    print("Product created successfully.")
    return inventory


# -------------------------------
# Read all products
# -------------------------------
def read_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    print("\n--- INVENTORY LIST ---")
    for title, data in inventory.items():
        print(f"Title: {title} | Author: {data['author']} | Category: {data['category']} | "
              f"Price: {data['price']} | Stock: {data['stock']}")


# -------------------------------
# Update product
# -------------------------------
def update_product(inventory):
    title = input("Enter the title to update: ").lower()

    if title not in inventory:
        print("Product not found.")
        return inventory

    print("\nWhat do you want to update?")
    print("1. Price")
    print("2. Stock")

    try:
        option = int(input("Select option: "))
        if option == 1:
            new_price = validate_positive_float(input("Enter new price: "))
            inventory[title]["price"] = new_price
        elif option == 2:
            new_stock = validate_positive_int(input("Enter new stock: "))
            inventory[title]["stock"] = new_stock
        else:
            print("Invalid option.")
            return inventory
    except ValueError:
        print("Invalid value.")
        return inventory

    print("Product updated successfully.")
    return inventory


# -------------------------------
# Delete product
# -------------------------------
def delete_product(inventory):
    title = input("Enter title to delete: ").lower()
    if title in inventory:
        del inventory[title]
        print("Product deleted.")
    else:
        print("Product not found.")
