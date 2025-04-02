from django.db import models
from django.contrib.auth.models import User
from shop.models import Products
from decimal import Decimal

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price_at_addition = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    @property
    def amount(self):
        return Decimal(self.quantity * self.product.price if self.product else Decimal(0.0))

class Address(models.Model):
    region = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=30, default='Pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def amount(self):
        return Decimal(self.quantity * self.product.price if self.product else Decimal(0.0))


