# src/db/initialize.py
from db.connection import create_connection
from db.query import execute_query

# SQL schema to create all tables for the inventory system
schema = ["""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    brand VARCHAR(50),
    category VARCHAR(50) CHECK (category IN ('Pants', 'Shirts', 'Shoes')),
    base_price DECIMAL(10, 2) NOT NULL,
    supplier_id INTEGER NOT NULL,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
)
""",
"""
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100),
    address TEXT
)
""",
"""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100),
    address TEXT
)
""",
"""
CREATE TABLE IF NOT EXISTS stock (
    stock_id INTEGER PRIMARY KEY AUTOINCREMENT,
    quantity_available INTEGER NOT NULL,
    last_updated TEXT NOT NULL DEFAULT (DATETIME('now')),
    product_id INTEGER,
    FOREIGN KEY(product_id) REFERENCES products(product_id)
)
""",
"""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date DATETIME NOT NULL,
    customer_id INTEGER, -- Optional: Use for Sales
    supplier_id INTEGER, -- Optional: Use for Purchases
    status VARCHAR(50) NOT NULL,
    order_type VARCHAR(50) NOT NULL CHECK (order_type IN ('Sale', 'Purchase')),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
)
""",
"""
CREATE TABLE IF NOT EXISTS order_details (
    order_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity_ordered INTEGER NOT NULL,
    unit_price_at_time_of_order DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
""",
"""
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stock_id INTEGER NOT NULL,
    quantity_change INTEGER NOT NULL,
    transaction_type VARCHAR(50) NOT NULL,
    transaction_date DATETIME NOT NULL,
    FOREIGN KEY (stock_id) REFERENCES stock(stock_id)
)
"""
]

def initialize_database(connection):
    """
    Create all tables in the database if they do not exist.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.
    """
    # Execute the list of SQL table creation queries.
    for query in schema:
        execute_query(connection, query)
    print("Database initialized successfully")