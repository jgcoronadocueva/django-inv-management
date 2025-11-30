# inventory_app/views/products.py
from django.shortcuts import render, redirect
from inventory_app.forms import ProductForm
from inventory_app.forms import StockAdjustForm
from inventory_app.services import product_services


def product_list(request):
    products = product_services.list_products()
    return render(request, "inventory_app/products/list.html", {"products": products})


def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product_services.create_product(form.cleaned_data)
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(request, "inventory_app/products/form.html", {"form": form})


def product_detail(request, id):
    product = product_services.get_product(id)
    form = StockAdjustForm()
    return render(request, "inventory_app/products/detail.html", {"product": product})


def product_edit(request, id):
    product = product_services.get_product(id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product_services.update_product(product, form.cleaned_data)
            return redirect("product_detail", id=product.id)
    else:
        form = ProductForm(instance=product)

    return render(request, "inventory_app/products/form.html", {"form": form, "product": product})