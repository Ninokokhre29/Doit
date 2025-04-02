from pickletools import decimalnl_long

from django.db import models
from django.db.models import CASCADE


class Category(models.Model):
    name = models.CharField(max_length=200)
    category_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField()
    category = models.ManyToManyField(Category, related_name='product_category')
    image = models.ImageField(upload_to='products', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name