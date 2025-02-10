from datetime import date

from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    release_date = models.DateField('Дата производства', default=date.today) #YYYY-MM-DD
    manufacturer = models.ForeignKey(Manufacturer,verbose_name="Производитель", on_delete=models.CASCADE)