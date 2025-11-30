# inventory_app/services/product_services.py
from inventory_app.models import Product, Stock


def list_products():
    """
    Retrieves all products, including their related stock and supplier information.
    """
    return Product.objects.select_related('stock', 'supplier').all()

def get_product(id):
    """
    Retrieves a single product by its ID.
    
    Args:
        id (int): The ID of the product to retrieve.
        
    Returns:
        Product: The product instance.
    """
    return Product.objects.get(id=id)

def create_product(data):
    """
    Creates a new product and initializes its stock record to 0.
    
    Args:
        data (dict): Dictionary of product fields.
        
    Returns:
        Product: The newly created product instance.
    """
    product = Product.objects.create(**data)
    Stock.objects.create(product=product, quantity=0)
    return product

def update_product(product, data):
    """
    Updates the fields of an existing product with the provided data.
    
    Args:
        product (Product): The product instance to update.
        data (dict): Dictionary of fields to update.
        
    Returns:
        Product: The updated product instance.
    """
    for key, value in data.items():
        setattr(product, key, value)
    product.save()
    return product