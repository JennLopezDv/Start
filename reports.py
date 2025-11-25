# reports.py
# Dynamic reporting system.

def top_selling_products(sales):
    if not sales:
        print("No sales to analyze.")
        return

    # Aggregate quantities per product
    totals = {}
    for s in sales:
        totals[s["product"]] = totals.get(s["product"], 0) + s["quantity"]

    top3 = sorted(totals.items(), key=lambda x: x[1], reverse=True)[:3]

    print("\n--- TOP 3 BEST SELLING PRODUCTS ---")
    for product, qty in top3:
        print(f"{product}: {qty} units")


def sales_by_author(sales, inventory):
    if not sales:
        print("No sales to analyze.")
        return

    authors = {}
    for sale in sales:
        author = inventory[sale["product"]]["author"]
        authors[author] = authors.get(author, 0) + sale["quantity"]

    print("\n--- SALES BY AUTHOR ---")
    for author, qty in authors.items():
        print(f"{author}: {qty} units")


def income_report(sales, inventory):
    if not sales:
        print("No sales to analyze.")
        return

    # Use lambda functions
    gross_income = sum(map(lambda s: s["quantity"] * inventory[s["product"]]["price"], sales))
    net_income = sum(
        map(lambda s: (s["quantity"] * inventory[s["product"]]["price"]) * (1 - s["discount"]), sales)
    )

    print("\n--- INCOME REPORT ---")
    print(f"Gross income: ${gross_income:.2f}")
    print(f"Net income (after discounts): ${net_income:.2f}")
