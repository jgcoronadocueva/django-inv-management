# src/models/suppliers.py
from db.query import execute_query, execute_read_query

def add_supplier(connection, name, phone, email=None, address=None):
    """
    Add a new supplier to the database.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.
    name : str
        Supplier's name.
    phone : str
        Supplier's phone number.
    email : str, optional
        Supplier's email address.
    address : str, optional
        Supplier's physical address.

    Returns
    -------
    int
        ID of the newly added supplier.
    """
    execute_query(connection, """
        INSERT INTO suppliers (name, phone, email, address)
        VALUES (?, ?, ?, ?)
    """, (name, phone, email, address))

    # Return the last inserted ID
    result = execute_read_query(connection, "SELECT last_insert_rowid()")
    return result[0][0] if result else None


def get_supplier_by_id(connection, supplier_id):
    """
    Retrieve a single supplier by their ID.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.
    supplier_id : int
        The ID of the supplier.

    Returns
    -------
    tuple or None
        Supplier row if found, else None.
    """
    result = execute_read_query(connection, "SELECT * FROM suppliers WHERE supplier_id = ?", (supplier_id,))
    return result[0] if result else None


def list_suppliers(connection):
    """
    Retrieve all suppliers from the database.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.

    Returns
    -------
    list of tuple
        All supplier rows.
    """
    return execute_read_query(connection, "SELECT * FROM suppliers")


def update_supplier_email(connection, supplier_id, email):
    """
    Update the email address of a supplier by their ID.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.
    supplier_id : int
       The ID of the supplier to update.
    email : str
        The new email address.
    """
    execute_query(connection, "UPDATE suppliers SET email = ? WHERE supplier_id = ?", (email, supplier_id))