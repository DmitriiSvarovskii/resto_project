from django.db import models

from django.db import models


from django.db import models


class User(models.Model):
    user_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=64)
    role = models.CharField(max_length=32)
    bought = models.BooleanField(default=False)
    label = models.CharField(max_length=32, default='1')
    username = models.CharField(max_length=128)

    def __str__(self):
        return self.user_id


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.SmallIntegerField(null=True, blank=True)
    count = models.SmallIntegerField(null=True, blank=True)
    compound = models.TextField(null=True, blank=True)
    product_category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
