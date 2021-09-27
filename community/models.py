from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q
import datetime as dt

Priority=(
    ('Informational','Informational'),
    ('High Priority','High Priority'),
)

# Create your models here.
class neighbourhood(models.Model):
    neighbourhood= models.CharField(max_length=100)

    def __str__(self):
        return self.neighbourhood

class notifications(models.Model):
    title = models.CharField(max_length=100)
    notification = HTMLField()
    priority = models.CharField(max_length=15,choices=Priority,default="Informational")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class healthservices(models.Model):
    healthservices = models.CharField(max_length=100)

    def __str__(self):
        return self.healthservices



class Business(models.Model):
    logo = models.ImageField(upload_to='businesslogo/')
    description = HTMLField()
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    address =models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.name

class Health(models.Model):
    logo = models.ImageField(upload_to='healthlogo/')
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)
    healthservices = models.ManyToManyField(healthservices)

    def __str__(self):
        return self.name

class Authorities(models.Model):
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    description = HTMLField()
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='post/')
    post = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood= models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='avatars/')


    def __str__(self):
        return self.title