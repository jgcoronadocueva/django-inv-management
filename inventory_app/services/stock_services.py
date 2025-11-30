# inventory_app/services/stock_services.py
from inventory_app.models import Stock

def adjust_stock(id, qty_change):
    """
    Adjusts the quantity of a stock record by the given amount.
    
    Args:
        id (int): ID of the stock record.
        qty_change (int): Quantity change (positive for adding or negative for subtracting).
        
    Returns:
        Stock: The updated stock instance.
    """
    stock = Stock.objects.get(id=id)
    stock.quantity += qty_change
    stock.save()
    return stock
