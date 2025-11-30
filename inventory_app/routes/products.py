# inventory_app/routes/products.py
from django.urls import path
from inventory_app.views import products

urlpatterns = [
    path("", products.product_list, name="product_list"),
    path("add/", products.product_add, name="product_add"),
    path("<int:id>/", products.product_detail, name="product_detail"),
    path("<int:id>/edit/", products.product_edit, name="product_edit")
]