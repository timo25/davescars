from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class Product(models.Model):
    image=models.ImageField(upload_to='static/images',blank=True,null=True)
    image_left=models.ImageField(upload_to='static/images',blank=True,null=True)
    image_right=models.ImageField(upload_to='static/images',blank=True,null=True)
    image_front=models.ImageField(upload_to='static/images',blank=True,null=True)
    image_back=models.ImageField(upload_to='static/images',blank=True,null=True)
    image_interior=models.ImageField(upload_to='static/images',blank=True,null=True)
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=15,decimal_places=2)
    description=models.TextField(max_length=500)
    category=models.CharField(max_length=100)
    created=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name
