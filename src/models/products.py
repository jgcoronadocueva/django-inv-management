# src/models/products.py
from db.query import execute_query, execute_read_query

def add_product(connection, name, base_price, supplier_id, category=None, description=None, brand=None):
    """
    Add a new product to the database.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.
    name : str
        Product name.
    base_price : float
        Base price of the product.
    supplier_id : int
        ID of the supplier.
    category : str, optional
        Category of the product (e.g., 'Pants', 'Shirts', 'Shoes').
    description : str, optional
        Product description.
    brand : str, optional
        Brand of the product.
    
    Returns
    -------
    int
        ID of the newly added product.
    """
    execute_query(connection, """
        INSERT INTO products (name, description, brand, category, base_price, supplier_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, description, brand, category, base_price, supplier_id))


def get_product_by_id(connection, product_id):
    """
    Retrieve a single product by its ID.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.
    product_id : int
        ID of the product.

    Returns
    -------
    tuple or None
        Product row if found, else None.
    """
    result = execute_read_query(connection, "SELECT * FROM products WHERE product_id = ?", (product_id,))
    return result[0] if result else None


def list_products(connection):
    """
    Retrieve all products from the database.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.

    Returns
    -------
    list of tuple
        All product rows.
    """
    return execute_read_query(connection, "SELECT * FROM products")


def update_product_price(connection, product_id, base_price):
    """
    Update the base price of a product.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.
    product_id : int
        ID of the product.
    base_price : float
        Base price of the product.
    """
    execute_query(connection, "UPDATE products SET base_price = ? WHERE product_id = ?", (base_price, product_id))


def delete_product(connection, product_id):
    """
    Delete a product by its ID.

    Parameters
    ----------
    connection : sqlite3.Connection
        The active database connection.
    product_id : int
        ID of the product.
    
    Returns
    -------
    string
        Depends if the product exists or not.
    """
    product = execute_read_query(connection, "SELECT * FROM products WHERE product_id = ?", (product_id,))
    if not product:
        return "Product not found"

    execute_query(connection, "DELETE FROM products WHERE product_id = ?", (product_id,))
    return f"Product {product_id} was deleted"
