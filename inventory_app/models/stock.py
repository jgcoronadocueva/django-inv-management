# inventory_app/models/stock.py
from django.db import models
from .product import Product


class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} — {self.quantity} units"