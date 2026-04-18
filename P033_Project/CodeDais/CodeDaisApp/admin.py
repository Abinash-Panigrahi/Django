from django.contrib import admin
from .models import SignUpModel

# Register your models here.

@admin.register(SignUpModel)
class SignUpAdmin(admin.ModelAdmin):
    list_display=['name','email','password','gender']