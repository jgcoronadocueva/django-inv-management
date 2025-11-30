# inventory_app/views/stock.py
from django.shortcuts import render, redirect
from inventory_app.forms import StockAdjustForm
from inventory_app.services import stock_services

def stock_adjust(request, id):
    """
    Adjust stock quantity for a specific product.
    """
    if request.method == "POST":
        form = StockAdjustForm(request.POST)
        if form.is_valid():
            qty = form.cleaned_data["qty_change"] # Get quantity to add/subtract
            stock_services.adjust_stock(id, qty)
            return redirect("product_list")
    else:
        form = StockAdjustForm()

    return render(request, "inventory_app/stock/adjust.html", {"form": form})