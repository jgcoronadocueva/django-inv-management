# inventory_app/services/supplier_services.py
from inventory_app.models import Supplier


def list_suppliers():
    return Supplier.objects.all()

def get_supplier(id):
    return Supplier.objects.get(id=id)

def create_supplier(data):
    supplier = Supplier.objects.create(**data)
    return supplier

def update_supplier(supplier, data):
    for key, value in data.items():
        setattr(supplier, key, value)
    supplier.save()
    return supplier