from typing import Pattern
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.

class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    # category = models.ForeignKey('Category', null=True, blank=True,on_delete=models.CASCADE)
    category = models.ManyToManyField('Category',related_name="categories")
    slug = models.SlugField(unique=True)


    def categories(self):
        return ', '.join([c.name for c in self.category.all()])
    

    def __str__(self):
        return self.productname


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete=models.CASCADE)   

    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])
