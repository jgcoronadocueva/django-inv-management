# src/services/reports.py
from db.query import execute_read_query

def sales_summary_by_customer(connection):
    """
    Summarize sales per customer.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.

    Returns
    -------
    list of tuple
        Each row contains:
        (customer_name, total_items_sold, total_sales_amount)
    """
    query = """
    SELECT c.name AS customer_name,
           COUNT(od.order_detail_id) AS total_items_sold,
           SUM(od.quantity_ordered * od.unit_price_at_time_of_order) AS total_sales_amount
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    JOIN order_details od ON o.order_id = od.order_id
    WHERE o.order_type = 'Sale'
    GROUP BY c.customer_id
    """
    return execute_read_query(connection, query)


def purchase_summary_by_supplier(connection):
    """
    Summarize purchases per supplier.

    Parameters
    ----------
    connection : sqlite3.Connection
        Active database connection.

    Returns
    -------
    list of tuple
        Each row contains:
        (supplier_name, total_items_purchased, total_purchase_amount)
    """
    query = """
    SELECT s.name AS supplier_name,
           COUNT(od.order_detail_id) AS total_items_purchased,
           SUM(od.quantity_ordered * od.unit_price_at_time_of_order) AS total_purchase_amount
    FROM orders o
    JOIN suppliers s ON o.supplier_id = s.supplier_id
    JOIN order_details od ON o.order_id = od.order_id
    WHERE o.order_type = 'Purchase'
    GROUP BY s.supplier_id
    """
    return execute_read_query(connection, query)