from django.contrib import admin

# Register your models here.
from django.contrib import admin
from inventory_app.models import Supplier, Product, Stock

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Stock)