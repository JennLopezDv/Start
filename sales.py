# sales.py
# Handles creation of sales and automatic stock update.

import json
from utils import validate_positive_int
from datetime import datetime

SALES_FILE = "sales.json"

# -----------------------------
# Load & Save
# -----------------------------
def load_sales():
    try:
        with open(SALES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Sales file not found. A new one will be created.")
        return []

def save_sales(sales):
    with open(SALES_FILE, "w") as file:
        json.dump(sales, file, indent=4)
    print("Sales saved successfully.")


# -----------------------------
# Create Sale
# -----------------------------
def create_sale(inventory, sales):
    customer = input("Enter customer name: ").lower()
    product = input("Enter product sold: ").lower()

    if product not in inventory:
        print("Error: product not found in inventory.")
        return sales, inventory

    try:
        quantity = validate_positive_int(input("Enter quantity: "))
    except ValueError as e:
        print(e)
        return sales, inventory

    if quantity > inventory[product]["stock"]:
        print("Error: not enough stock available.")
        return sales, inventory

    discount = 0.20  # constant discount

    sale = {
        "customer": customer,
        "product": product,
        "quantity": quantity,
        "discount": discount,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    sales.append(sale)

    # Update stock automatically
    inventory[product]["stock"] -= quantity

    print("Sale registered successfully.")
    return sales, inventory
