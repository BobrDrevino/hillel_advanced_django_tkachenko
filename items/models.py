from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    price = models.PositiveIntegerField()
    sku = models.CharField(max_length=255)


class Discount(models.Model):
    CHOICES = [
        (0, 'В деньгах'),
        (1, 'В процентах')
    ]
    amount = models.PositiveIntegerField()
    code = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    discount_type = models.CharField(choices=CHOICES, max_length=20, default=1)
