from django.db import models

# Create your models here.

class Employee_Model(models.Model):
    name=models.CharField(max_length=30)
    desg=models.CharField(max_length=30)
    age=models.IntegerField()
    sal=models.FloatField()
    address=models.CharField(max_length=30)
   