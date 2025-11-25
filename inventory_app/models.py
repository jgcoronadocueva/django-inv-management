from django.db import models
from django.utils import timezone


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    PANTS = "Pants"
    SHIRTS = "Shirts"
    SHOES = "Shoes"

    CATEGORY_CHOICES = [
        (PANTS, "Pants"),
        (SHIRTS, "Shirts"),
        (SHOES, "Shoes"),
    ]

    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    quantity_available = models.IntegerField()
    last_updated = models.DateTimeField(default=timezone.now)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} — {self.quantity_available}"


class Order(models.Model):
    SALE = "Sale"
    PURCHASE = "Purchase"

    ORDER_TYPE_CHOICES = [
        (SALE, "Sale"),
        (PURCHASE, "Purchase"),
    ]

    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField()
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    supplier = models.ForeignKey(Supplier, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=50)
    order_type = models.CharField(max_length=50, choices=ORDER_TYPE_CHOICES)

    def __str__(self):
        return f"Order {self.order_id} ({self.order_type})"


class OrderDetail(models.Model):
    order_detail_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_ordered = models.IntegerField()
    unit_price_at_time_of_order = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.order} - {self.product.name}"


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity_change = models.IntegerField()
    transaction_type = models.CharField(max_length=50)  # You can convert to choices later
    transaction_date = models.DateTimeField()

    def __str__(self):
        return f"{self.transaction_type} ({self.quantity_change})"