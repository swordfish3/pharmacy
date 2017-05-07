from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    barcode = models.BigIntegerField(max_length=100)
    name = models.CharField(max_length=512)
    retail = models.IntegerField(default=0)
    wholesale = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'products'
