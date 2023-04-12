from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    products = models.ManyToManyField('Product', related_name='tags')

    class Meta:
        ordering = ['tag_name']

    def __str__(self):
        return self.tag_name

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name