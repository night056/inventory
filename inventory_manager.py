import csv
import os

FILE_NAME = "inventory.csv"

def initialize_csv():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Product ID", "Product Name", "Category", "Price", "Stock", "Total Sales"])

def load_inventory():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_inventory(inventory):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Product ID", "Product Name", "Category", "Price", "Stock", "Total Sales"])
        writer.writeheader()
        writer.writerows(inventory)

def add_product_web(product_id, product_name, category, price, stock):
    inventory = load_inventory()
    if any(item['Product ID'] == product_id for item in inventory):
        return "Error: Product ID already exists!"
    inventory.append({
        "Product ID": product_id,
        "Product Name": product_name,
        "Category": category,
        "Price": price,
        "Stock": stock,
        "Total Sales": "0"
    })
    save_inventory(inventory)
    return "Product added successfully!"
