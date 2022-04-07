
from django.db import models

# class Register(models.Model):
#     username = models.CharField(max_length=122,unique=True)
#     email = models.CharField(max_length=122,unique=True)
#     pnum = models.CharField(max_length=10)
#     pass1 = models.CharField(max_length=30)
#     pass2 = models.CharField(max_length=30)
#     pass

#     def __str__(self):
#         return self.username

class Gujproduct(models.Model):
    name = models.CharField( max_length=100,null=True)
    img = models.ImageField(upload_to='pics',null=True)
    desc = models.TextField(max_length=100,null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Southjproduct(models.Model):
    name = models.CharField( max_length=100,null=True)
    img = models.ImageField(upload_to='pics',null=True)
    desc = models.TextField(max_length=100,null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Punjabijproduct(models.Model):
    name = models.CharField( max_length=100,null=True)
    img = models.ImageField(upload_to='pics',null=True)
    desc = models.TextField(max_length=100,null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Rajsthaniproduct(models.Model):
    name = models.CharField( max_length=100,null=True)
    img = models.ImageField(upload_to='pics',null=True)
    desc = models.TextField(max_length=100,null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Indianstreetproduct(models.Model):
    name = models.CharField( max_length=100,null=True)
    img = models.ImageField(upload_to='pics',null=True)
    desc = models.TextField(max_length=100,null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Chinesseproduct(models.Model):
    name = models.CharField( max_length=100,null=True)
    img = models.ImageField(upload_to='pics',null=True)
    desc = models.TextField(max_length=100,null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name
    
    
