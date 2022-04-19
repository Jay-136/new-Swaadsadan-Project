
from itertools import product
from xmlrpc.client import DateTime
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField, DateTimeField, IntegerField



# class Register(models.Model):
#     username = models.CharField(max_length=122,unique=True)
#     email = models.CharField(max_length=122,unique=True)
#     pnum = models.CharField(max_length=10)
#     pass1 = models.CharField(max_length=30)
#     pass2 = models.CharField(max_length=30)
#     pass

#     def __str__(self):
#         return self.username

# class Gujproduct(models.Model):
#     name = models.CharField( max_length=100,null=True)
#     img = models.ImageField(upload_to='pics',null=True)
#     desc = models.TextField(max_length=100,null=True)
#     price = models.IntegerField(null=True)

#     def __str__(self):
#         return self.name

# class Southjproduct(models.Model):
#     name = models.CharField( max_length=100,null=True)
#     img = models.ImageField(upload_to='pics',null=True)
#     desc = models.TextField(max_length=100,null=True)
#     price = models.IntegerField(null=True)

#     def __str__(self):
#         return self.name

# class Punjabijproduct(models.Model):
#     name = models.CharField( max_length=100,null=True)
#     img = models.ImageField(upload_to='pics',null=True)
#     desc = models.TextField(max_length=100,null=True)
#     price = models.IntegerField(null=True)

#     def __str__(self):
#         return self.name

# class Rajsthaniproduct(models.Model):
#     name = models.CharField( max_length=100,null=True)
#     img = models.ImageField(upload_to='pics',null=True)
#     desc = models.TextField(max_length=100,null=True)
#     price = models.IntegerField(null=True)

#     def __str__(self):
#         return self.name

# class Indianstreetproduct(models.Model):
#     name = models.CharField( max_length=100,null=True)
#     img = models.ImageField(upload_to='pics',null=True)
#     desc = models.TextField(max_length=100,null=True)
#     price = models.IntegerField(null=True)

#     def __str__(self):
#         return self.name

# class Chinesseproduct(models.Model):
#     name = models.CharField( max_length=100,null=True)
#     img = models.ImageField(upload_to='pics',null=True)
#     desc = models.TextField(max_length=100,null=True)
#     price = models.IntegerField(null=True)

#     def __str__(self):
#         return self.name


class Category(models.Model):
    name=models.CharField(max_length=150,db_index=True)
    slug=models.SlugField(unique=True)
    img = models.ImageField(upload_to='pics',null=True)


    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField( max_length=100,null=True)
    img = models.ImageField(upload_to='pics',null=True)
    desc = models.TextField(max_length=100,null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
       return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.user.username
    
