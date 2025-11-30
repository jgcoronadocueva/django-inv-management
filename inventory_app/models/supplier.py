# inventory_app/models/supplier.py
from django.db import models


class Supplier(models.Model):
    """
    Represents a supplier that provides products.
    """
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name