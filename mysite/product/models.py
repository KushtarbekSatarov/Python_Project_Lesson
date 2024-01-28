#models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=32)
    text = models.TextField()
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=16)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.product}'


