from django.db import models


class ProductManager(models.Manager):
    def create_product(self, name, barcode, retail, quantity):
        product = self.create(name=name, barcode=barcode, retail=retail, quantity=quantity)
        return product


class Product(models.Model):
    # id = models.CharField(primary_key='true', max_length=100)
    name = models.CharField(default='test', max_length=200)
    barcode = models.BigIntegerField()
    retail = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    objects = ProductManager()

    def __str__(self):
        return self.name


class Meta:
    verbose_name_plural = 'products'
