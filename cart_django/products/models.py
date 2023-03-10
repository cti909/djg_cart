from django.db import models
from  accounts.models import User
from django.forms import ModelForm
from PIL import Image
# from uuid import uuid5
# import os

# def content_file_name(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = "%s_%s.%s" % (instance.user.id, instance.questid.id, ext)
#     return os.path.join('uploads', filename)


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    number = models.IntegerField()
    price = models.IntegerField()
    describe = models.CharField(max_length = 100, null=True)
    producer = models.CharField(max_length = 100, null=True)
    image = models.ImageField(upload_to = 'product_img/')
    
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    # class Meta:
    #     ordering = ['-updated', '-price']\
    # def create(request):
    # def path_and_rename(path):
    #     def wrapper(instance, filename):
    #         ext = filename.split('.')[-1]
    #         f_name = '-'.join(filename.replace('.pdf', '').split() )
    #         rand_strings = ''.join( random.choice(string.lowercase+string.digits) for i in range(10) )
    #         filename = '{}_{}{}.{}'.format(f_name, rand_strings, uuid4().hex, ext)
    #         return os.path.join(path, filename)
    #     return wrapper
    def __str__(self):
        return self.name
        
    # def save(self):
    #     super().save()  # saving image first

    #     img = Image.open(self.image.path) # Open image using self

    #     if img.height > 300 or img.width > 300:
    #         new_img = (300, 300)
    #         img.thumbnail(new_img)
    #         img.save(self.image.path)  # saving image at the same path
