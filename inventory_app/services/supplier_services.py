# inventory_app/services/supplier_services.py
from inventory_app.models import Supplier


def list_suppliers():
    """
    Retrieves all suppliers.
    """
    return Supplier.objects.all()

def get_supplier(id):
    """
    Retrieves a single supplier by its ID.
    
    Args:
        id (int): The ID of the supplier to retrieve.
        
    Returns:
        Supplier: The supplier instance.
    """
    return Supplier.objects.get(id=id)

def create_supplier(data):
    """
    Creates a new supplier record.
    
    Args:
        data (dict): Dictionary of supplier fields (name, phone, email, etc.)
        
    Returns:
        Supplier: The newly created supplier instance.
    """
    supplier = Supplier.objects.create(**data)
    return supplier

def update_supplier(supplier, data):
    """
    Updates an existing supplier's fields with the provided data.
    
    Args:
        supplier (Supplier): The supplier instance to update.
        data (dict): Dictionary of fields to update.
        
    Returns:
        Supplier: The updated supplier instance.
    """
    for key, value in data.items():
        setattr(supplier, key, value)
    supplier.save()
    return supplier