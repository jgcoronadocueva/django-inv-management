# src/models/stock.py
from db.query import execute_query, execute_read_query

def add_stock_record(connection, product_id, quantity):
    """
    Add a new stock record for a product.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.
    product_id : int
        The ID of the product.
    quantity : int
        Initial quantity to add.

    Returns
    -------
    int
        ID of the newly created stock record.
    """
    execute_query(connection, """
        INSERT INTO stock (product_id, quantity_available)
        VALUES (?, ?)
    """, (product_id, quantity))

    result = execute_read_query(connection, "SELECT last_insert_rowid()")
    return result[0][0] if result else None


def update_stock(connection, stock_id, qty_change, transaction_type):
    """
    Update the stock quantity and record a transaction.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.
    stock_id : int
        The ID of the stock record to update.
    qty_change : int
        Positive number to increase stock, negative to decrease.
    transaction_type : str
        Type of transaction.
    """
    # Update stock quantity and timestamp
    execute_query(connection, """
        UPDATE stock
        SET quantity_available = quantity_available + ?,
            last_updated = datetime('now')
        WHERE stock_id = ?
    """, (qty_change, stock_id))

    # Record the stock change in the transactions table
    execute_query(connection, """
        INSERT INTO transactions (stock_id, quantity_change, transaction_type, transaction_date)
        VALUES (?, ?, ?, datetime('now'))
    """, (stock_id, qty_change, transaction_type))


def get_stock(connection):
    """
    Retrieve all stock records along with product details.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.

    Returns
    -------
    list of tuple
        Each row contains:
        (product_id, product_name, quantity_available)
    """
    return execute_read_query(connection, """
        SELECT p.product_id, p.name, s.quantity_available
        FROM stock s
        JOIN products p ON p.product_id = s.product_id
    """)