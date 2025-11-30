from django import forms
from inventory_app.models import Product, Supplier, Stock

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "brand", "category", "base_price", "supplier"]

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["name", "phone", "email", "address"]

class StockAdjustForm(forms.Form):
    qty_change = forms.IntegerField(
        label="Quantity Change",
        help_text="Enter a positive or negative number"
    )

