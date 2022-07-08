from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Manufacturer(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/logos')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    image = models.ImageField(upload_to='images/cats')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='images')
    count = models.IntegerField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
    manufacturer = models.ForeignKey(Manufacturer, related_name='products', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('prdouctDetail', args=[self.id])


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)