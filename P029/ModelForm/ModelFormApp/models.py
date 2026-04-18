from django.db import models

# Create your models here.

class Employee_Model(models.Model):
    name=models.CharField(max_length=30)
    desg=models.CharField(max_length=30)
    age=models.IntegerField(null=True,blank=True)
    sal=models.FloatField(null=True,blank=True)
    address=models.CharField(max_length=30)
   