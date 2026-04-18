from django.db import models

# Create your models here.

class TMSModels(models.Model):
    task_name=models.CharField(max_length=30)
    task_status=models.BooleanField(default=False)
