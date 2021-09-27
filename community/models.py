from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
import datetime as dt
from tinymce.models import HTMLField

# Create your models here.

Priority=(
    ('Informational','Informational'),
    ('High Priority','High Priority'),
)
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
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title