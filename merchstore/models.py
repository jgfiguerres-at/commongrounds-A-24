from django.db import models

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'product type'
        verbose_name_plural = 'product types'


class Product(models.Model):
    name = models.CharField(max_length=255)
    ProductType
    description = models.TextField()
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'product'
        verbose_name_plural = 'products'

