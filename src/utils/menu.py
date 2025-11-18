# src/utils/menu.py
from models.products import add_product, list_products, update_product_price, delete_product
from models.customers import add_customer, list_customers, update_customer_email
from models.suppliers import add_supplier, list_suppliers, update_supplier_email
from models.stock import get_stock, add_stock_record
from services.orders import process_order, list_orders, view_order
from services.reports import sales_summary_by_customer, purchase_summary_by_supplier

def run_menu(connection):
    menu_options = {
        "1": add_product_option,
        "2": list_products_option,
        "3": delete_product_option,
        "4": update_product_price_option,
        "5": add_customer_option,
        "6": list_customers_option,
        "7": update_customer_email_option,
        "8": add_supplier_option,
        "9": list_suppliers_option,
        "10": update_supplier_email_option,
        "11": add_stock_option,
        "12": check_stock_option,
        "13": process_purchase_order_option,
        "14": process_sale_order_option,
        "15": list_orders_option,
        "16": view_order_option,
        "17": sales_report_option,
        "18": purchase_report_option,
    }

    while True:
        print_menu()
        choice = input("Select an option: ")
        action = menu_options.get(choice)
        if action:
            action(connection)
        else:
            print("Invalid option. Try again.")

def print_menu():
    print("""
--- Inventory Menu ---
1. Add Product
2. List Products
3. Delete Product
4. Update Product Price
5. Add Customer
6. List Customers
7. Update Customer Email
8. Add Supplier
9. List Suppliers
10. Update Supplier Email
11. Add Stock
12. Check Stock 
13. Process Purchase Order
14. Process Sale Order
15. List Orders
16. View Order Details
17. Sales Report by Customer
18. Purchase Report by Supplier
""")


def add_product_option(connection):
    print("Adding sample product...")
    add_product(connection, name="Blue Shirt", base_price=15.0, supplier_id=1, category="Shirts", description="Cotton shirt", brand="BrandA")
    add_product(connection, name="Black Pants", base_price=25.0, supplier_id=1, category="Pants", description="Formal pants", brand="BrandB")
    print("Products added.")

def list_products_option(connection):
    print("Listing all products:")
    for p in list_products(connection):
        print(p)

def delete_product_option(connection):
    print("Deleting product ID 2...")
    msg = delete_product(connection, 2)
    print(msg)

def update_product_price_option(connection):
    print("Updating product ID 1 price to 20.0...")
    update_product_price(connection, 1, 20.0)
    print("Price updated.")

def add_customer_option(connection):
    print("Adding sample customers...")
    add_customer(connection, "Alice", phone="1234567890", email="alice@example.com")
    add_customer(connection, "Bob", phone="0987654321", email="bob@example.com")
    print("Customers added.")

def list_customers_option(connection):
    print("Listing all customers:")
    for c in list_customers(connection):
        print(c)

def update_customer_email_option(connection):
    print("Updating customer ID 1 email...")
    update_customer_email(connection, 1, "alice_new@example.com")
    print("Customer email updated.")

def add_supplier_option(connection):
    print("Adding sample suppliers...")
    add_supplier(connection, "SupplierX", phone="111222333", email="supx@example.com", address="Street 123")
    add_supplier(connection, "SupplierY", phone="444555666", email="supy@example.com", address="Street 456")
    print("Suppliers added.")

def list_suppliers_option(connection):
    print("Listing all suppliers:")
    for s in list_suppliers(connection):
        print(s)

def update_supplier_email_option(connection):
    print("Updating supplier ID 1 email...")
    update_supplier_email(connection, 1, "supx_new@example.com")
    print("Supplier email updated.")

def add_stock_option(connection):
    print("Add stock to a product")
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity to add: "))
    add_stock_record(connection, product_id, quantity)
    print(f"Added {quantity} units to product {product_id}.")

def process_purchase_order_option(connection):
    print("Processing a purchase order...")
    items = [{"product_id": 1, "quantity": 50, "unit_price": 10.0}]
    order_id = process_order(connection, "Purchase", items=items, supplier_id=1)
    print(f"Purchase order created with ID: {order_id}")

def process_sale_order_option(connection):
    print("Processing a sale order...")
    items = [{"product_id": 1, "quantity": 5, "unit_price": 15.0}]
    order_id = process_order(connection, "Sale", items=items, customer_id=1)
    print(f"Sale order created with ID: {order_id}")

def list_orders_option(connection):
    print("Listing all orders:")
    for o in list_orders(connection):
        print(o)

def view_order_option(connection):
    print("Viewing details of order ID 1:")
    for detail in view_order(connection, 1):
        print(detail)

def check_stock_option(connection):
    print("Checking stock:")
    for row in get_stock(connection):
        print(row)

def sales_report_option(connection):
    print("Sales summary by customer:")
    for row in sales_summary_by_customer(connection):
        print(row)

def purchase_report_option(connection):
    print("Purchase summary by supplier:")
    for row in purchase_summary_by_supplier(connection):
        print(row)