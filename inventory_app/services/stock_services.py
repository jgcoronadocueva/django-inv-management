# inventory_app/services/stock_services.py
from inventory_app.models import Stock

def adjust_stock(id, qty_change):
    stock = Stock.objects.get(id=id)
    stock.quantity += qty_change
    stock.save()
    return stock
