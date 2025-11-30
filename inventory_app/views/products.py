# inventory_app/views/products.py
from django.shortcuts import render, redirect
from inventory_app.forms import ProductForm
from inventory_app.forms import StockAdjustForm
from inventory_app.services import product_services


def product_list(request):
    """
    Display a list of all products with their related info.
    """
    products = product_services.list_products()
    return render(request, "inventory_app/products/list.html", {"products": products})


def product_add(request):
    """
    Add a new product.
    """
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid(): # Check all required fields
            product_services.create_product(form.cleaned_data)
            return redirect("product_list") # Redirect to product list after creation
    else:
        form = ProductForm()

    return render(request, "inventory_app/products/form.html", {"form": form})


def product_detail(request, id):
    """
    Show details for a specific product.
    """
    product = product_services.get_product(id)
    return render(request, "inventory_app/products/detail.html", {"product": product})


def product_edit(request, id):
    """
    Edit an existing product.
    """
    product = product_services.get_product(id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product_services.update_product(product, form.cleaned_data)
            return redirect("product_detail", id=product.id)
    else:
        form = ProductForm(instance=product) # Fill form with existing product data

    return render(request, "inventory_app/products/form.html", {"form": form, "product": product})