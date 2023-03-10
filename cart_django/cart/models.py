from django.db import models
from accounts.models import User
from products.models import *

# Gio hang phu thuoc vao vat pham dang ban (neu vat thay doi thi gh cung thay doi)
# Ls giao dich ko phu thuoc 

class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    # name = models.CharField(max_length = 100)
    # image = models.ImageField(upload_to = 'product_img', max_length = 10000)
    number = models.IntegerField()
    # price = models.IntegerField()
    # producer = models.CharField(max_length = 100, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    

class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    receiver = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    date = models.DateTimeField()
    user_id = models.IntegerField() # khoa ngoai
    def __unicode__(self):
        return self.receiver
    def __str__(self):
        return  self.receiver

class OrderDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'product_img', max_length = 10000)
    number = models.IntegerField()
    price = models.IntegerField()
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    # producer = models.CharField(max_length = 100, null=True)
    # product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,blank=True,related_name='ord')
    def __unicode__(self):
        return self.name 
    def __str__(self):
        return  self.name