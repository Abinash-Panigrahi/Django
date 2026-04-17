from django.db import models

# Create your models here.

class Shirt(models.Model):
    brand=models.CharField(max_length=20)
    price=models.FloatField()
    color=models.CharField(max_length=20)