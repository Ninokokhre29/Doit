from django.db import models
from shop.models import Products

# Retrieve all products
products = Products.objects.all()

# Display the products
for product in products:
    print(product.name, product.price)
