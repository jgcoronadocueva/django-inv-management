# inventory_app/models/stock.py
from django.db import models
from .product import Product


class Stock(models.Model):
    """
    Represents the stock level of a product.
    """
    # Each product has exactly one stock record
    product = models.OneToOneField(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    # Automatically updated timestamp
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} — {self.quantity} units"