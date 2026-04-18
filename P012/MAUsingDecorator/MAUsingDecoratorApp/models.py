from django.db import models

# Create your models here.

class Books(models.Model):
    bookname=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    price=models.FloatField()

