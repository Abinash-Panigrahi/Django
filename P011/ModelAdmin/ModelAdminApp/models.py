from django.db import models

# Create your models here.

class Protien(models.Model):
    product=models.CharField(max_length=20)
    brand=models.CharField(max_length=20)
    kg=models.FloatField()
    price=models.FloatField()

   