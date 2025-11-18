# Overview

This inventory management system is designed to help manage products, suppliers, customers, stock, orders, and transactions. My goal creating this program is sharpen my skills writing SQL queries including joins and using aggregate functions.

The program uses sqlite3 library in Python to perfom CRUD operations accross multiple related tables in an SQLite relational. The program is modular, with separate Python modules for managing products, suppliers, stock, orders, and transactions.

To use the program, simply run the main.py script. The program demonstrates using an interactive menu:

- Adding and modifying records from different tables
- Creating and managing orders and transactions
- Running queries to summarize data
- Joining tables to retrieve combined information

[Working with SQLite database in Python](https://youtu.be/aAGt33whKzI)

# Relational Database

The program uses SQLite as its relational database.

- **Suppliers:** `supplier_id` (PK), `name`, `phone`, `email`, `address`  
- **Products:** `product_id` (PK), `name`, `description`, `brand`, `category` (Pants/Shirts/Shoes), `base_price`, `supplier_id` (FK)
- **Customers:** `customer_id` (PK), `name`, `phone`, `email`, `address`  
- **Stock:** `stock_id` (PK), `quantity_available`, `last_updated`, `product_id` (FK)  
- **Orders:** `order_id` (PK), `order_date`, `customer_id` (FK), `supplier_id` (FK), `status`, `order_type`
- **Order Details:** `order_detail_id` (PK), `order_id` (FK), `product_id` (FK), `quantity_ordered`, `unit_price_at_time_of_order`  
- **Transactions:** `transaction_id` (PK), `stock_id` (FK), `quantity_change`, `transaction_type`, `transaction_date`  

# Development Environment

Tools used to develop this program:

- **Programming Language:** Python 3.14
- **Libraries:** SQLite3
- **IDE:** Visual Studio Code 

# Useful Websites

- [Python SQL Libraries – Real Python](https://realpython.com/python-sql-libraries/)
- [How to Work with SQLite in Python – freeCodeCamp](https://www.freecodecamp.org/news/work-with-sqlite-in-python-handbook/)

# Future Work

- Improve error handling and validation for user input.
- Implement a user-friendly GUI for easier interaction.
- Include report generation with export options (CSV, PDF).