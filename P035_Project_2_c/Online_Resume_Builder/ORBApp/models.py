from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    designation = models.CharField(max_length=100)
    summary = models.TextField()
    experience_company_details = models.TextField()
    experience = models.TextField()

    # def __str__(self):
    #     return self.name
