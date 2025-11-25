# main.py
# Interactive menu that controls the whole system.

from inventory import *
from sales import *
from reports import *


def main_menu():
    print("\n========= MAIN MENU =========")
    print("1. Inventory Management")
    print("2. Sales")
    print("3. Reports")
    print("4. Exit")


def inventory_menu():
    print("\n--- INVENTORY MENU ---")
    print("1. Create product")
    print("2. Show inventory")
    print("3. Update product")
    print("4. Delete product")
    print("5. Save inventory")
    print("6. Back")


def sales_menu():
    print("\n--- SALES MENU ---")
    print("1. Register sale")
    print("2. Save sales")
    print("3. Back")


def reports_menu():
    print("\n--- REPORTS MENU ---")
    print("1. Top 3 best selling products")
    print("2. Sales by author")
    print("3. Income report")
    print("4. Back")


# ============================
# MAIN PROGRAM EXECUTION
# ============================
def run_program():
    inventory = load_inventory()
    sales = load_sales()

    while True:
        main_menu()
        option = input("Choose option: ")

        # --- INVENTORY ---
        if option == "1":
            while True:
                inventory_menu()
                op = input("Choose option: ")

                if op == "1":
                    inventory = create_product(inventory)

                elif op == "2":
                    read_inventory(inventory)

                elif op == "3":
                    inventory = update_product(inventory)

                elif op == "4":
                    delete_product(inventory)

                elif op == "5":
                    save_inventory(inventory)

                elif op == "6":
                    break
                else:
                    print("Invalid option.")

        # --- SALES ---
        elif option == "2":
            while True:
                sales_menu()
                op = input("Choose option: ")

                if op == "1":
                    sales, inventory = create_sale(inventory, sales)

                elif op == "2":
                    save_sales(sales)

                elif op == "3":
                    break
                else:
                    print("Invalid option.")

        # --- REPORTS ---
        elif option == "3":
            while True:
                reports_menu()
                op = input("Choose option: ")

                if op == "1":
                    top_selling_products(sales)

                elif op == "2":
                    sales_by_author(sales, inventory)

                elif op == "3":
                    income_report(sales, inventory)

                elif op == "4":
                    break
                else:
                    print("Invalid option.")

        elif option == "4":
            print("Closing program...")
            save_inventory(inventory)
            save_sales(sales)
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    run_program()
