# src/models/customers.py
from db.query import execute_query, execute_read_query

def add_customer(connection, name, phone=None, email=None, address=None):
    """
    Add a new customer to the database.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.
    name : str
        Customer's full name.
    phone : str, optional
        Customer's phone number.
    email : str, optional
        Customer's email address.
    address : str
        Customer's physical address.

    Returns
    -------
    int
        The ID of the newly added customer.
    """
    execute_query(connection, """
        INSERT INTO customers (name, phone, email, address)
        VALUES (?, ?, ?, ?)
    """, (name, phone, email, address))

    # Return the last inserted ID
    result = execute_read_query(connection, "SELECT last_insert_rowid()")
    return result[0][0] if result else None


def get_customer_by_id(connection, customer_id):
    """
    Retrieve a single customer by their ID.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.
    customer_id : int
        The ID of the customer.

    Returns
    -------
    tuple or None
        Customer row if found, else None.
    """
    result = execute_read_query(connection, """
        SELECT * FROM customers WHERE customer_id = ?
    """, (customer_id,))
    return result[0] if result else None


def list_customers(connection):
    """
    Retrieve all customers from the database.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.

    Returns
    -------
    list of tuple
        List of all customer rows.
    """
    return execute_read_query(connection, "SELECT * FROM customers")


def update_customer_email(connection, customer_id, email):
    """
    Update the email address of a customer by their ID.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.
    customer_id : int
        The ID of the customer to update.
    email : str
        The new email address.
    """
    execute_query(connection, """
        UPDATE customers
        SET email = ?
        WHERE customer_id = ?
    """, (email, customer_id))
    