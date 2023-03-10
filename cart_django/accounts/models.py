from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    username = models.CharField(unique=True, max_length=50)
    password =models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=100)
    # avatar = models.ImageField(null=True, default="avatar.svg")
    # store_id = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True,related_name='users')
    # customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True,related_name='users')

    def __str__(self):
        return self.username

class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    username = models.CharField(unique=True, max_length=50)
    password =models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.username