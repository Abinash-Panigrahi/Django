from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class SignUpModel(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


class ContactModels(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    message = models.TextField()


