from django.db import models
from django.core.validators import validate_image_file_extension

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    profile_pic=models.ImageField(upload_to='images/',validators=[validate_image_file_extension])
    email=models.EmailField()
    desc=models.TextField(blank=True, null=True)

