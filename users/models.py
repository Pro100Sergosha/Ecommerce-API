from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product

class CustomUser(AbstractUser):
    products = models.ManyToManyField(Product, related_name='cart')