# inventory_app/routes/stock.py
from django.urls import path
from inventory_app.views import stock

urlpatterns = [
    path("<int:id>/adjust/", stock.stock_adjust, name="stock_adjust")
]