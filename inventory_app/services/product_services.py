# inventory_app/services/product_services.py
from inventory_app.models import Product, Stock


def list_products():
    return Product.objects.select_related('stock', 'supplier').all()

def get_product(id):
    return Product.objects.get(id=id)

def create_product(data):
    product = Product.objects.create(**data)
    Stock.objects.create(product=product, quantity=0)
    return product

def update_product(product, data):
    for key, value in data.items():
        setattr(product, key, value)
    product.save()
    return product