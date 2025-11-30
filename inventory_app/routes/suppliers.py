# inventory_app/routes/suppliers.py
from django.urls import path
from inventory_app.views import suppliers

urlpatterns = [
    path("", suppliers.supplier_list, name="supplier_list"),
    path("add/", suppliers.supplier_add, name="supplier_add"),
    path("<int:id>/", suppliers.supplier_detail, name="supplier_detail"),
    path("<int:id>/edit/", suppliers.supplier_edit, name="supplier_edit")
]