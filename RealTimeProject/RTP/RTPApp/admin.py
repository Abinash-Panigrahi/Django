from django.contrib import admin
from .models import SignUpModel
from .models import ContactModels

# Register your models here.

@admin.register(SignUpModel)
class SignUpModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password','gender']

@admin.register(ContactModels)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone','email','message']
