from django.db import models

# Create your models here.

class DCA(models.Model):
    country=models.CharField(max_length=20)
    capital=models.CharField(max_length=20)
    population=models.IntegerField()
    readmore=models.CharField(max_length=20)
    description=models.TextField()
    
