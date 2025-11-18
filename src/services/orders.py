# src/services/orders.py
from db.query import execute_query, execute_read_query
from models.stock import update_stock
from datetime import datetime

def process_order(connection, order_type, items, customer_id=None, supplier_id=None):
    """
    Process a Sale or Purchase order.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.
    order_type : str
        'Sale' or 'Purchase'.
    items : list of dict
        Each dict contains {"product_id": int, "quantity": int, "unit_price": float}.
    customer_id : int, optional
        Required for Sale orders.
    supplier_id : int, optional
        Required for Purchase orders.

    Returns
    -------
    int
        The ID of the newly created order.
    """
    now = datetime.now()
    current_date = now.date()
    # Insert order
    execute_query(connection, """
        INSERT INTO orders (order_date, customer_id, supplier_id, status, order_type)
        VALUES (?, ?, ?, ?, ?)
    """, (current_date, customer_id, supplier_id, "Completed", order_type))
    order_id = execute_read_query(connection, "SELECT last_insert_rowid()")[0][0]

    # Insert order details and update stock
    for item in items:
        product_id = item["product_id"]
        qty = item["quantity"]
        price = item["unit_price"]

        execute_query(connection, """
            INSERT INTO order_details (order_id, product_id, quantity_ordered, unit_price_at_time_of_order)
            VALUES (?, ?, ?, ?)
        """, (order_id, product_id, qty, price))

        # Get stock_id for this product
        stock_id = execute_read_query(connection, "SELECT stock_id FROM stock WHERE product_id = ?", (product_id,))[0][0]

        # Update stock: decrease for Sale, increase for Purchase
        update_stock(connection, stock_id, qty if order_type == "Purchase" else -qty, order_type)

    return order_id


def list_orders(connection):
    """List all orders with basic info."""
    return execute_read_query(connection, "SELECT order_id, order_type, status, order_date FROM orders")


def view_order(connection, order_id):
    """View details of a specific order."""
    return execute_read_query(connection, """
        SELECT od.order_detail_id, od.product_id, p.name,
               od.quantity_ordered, od.unit_price_at_time_of_order
        FROM order_details od
        JOIN products p ON p.product_id = od.product_id
        WHERE od.order_id = ?
    """, (order_id,))