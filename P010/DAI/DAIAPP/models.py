from django.db import models

# Create your models here.

class Electronics(models.Model):
    name=models.CharField(max_length=20)
    price=models.FloatField()
    brand=models.CharField(max_length=20)

    def __str__(self):
        data=str(self.brand)
        return data
