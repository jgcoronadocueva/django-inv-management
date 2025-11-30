from django.contrib import admin
from django.urls import path, include
from inventory_app.views.home import home

urlpatterns = [
    path("", home, name="home"),
    path("products/", include("inventory_app.routes.products")),
    path("suppliers/", include("inventory_app.routes.suppliers")),
    path("stock/", include("inventory_app.routes.stock"))
]