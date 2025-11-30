# inventory_app/models/product.py
from django.db import models
from .supplier import Supplier


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("Pants", "Pants"),
        ("Shirts", "Shirts"),
        ("Shoes", "Shoes"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)

    def __str__(self):
        return self.name