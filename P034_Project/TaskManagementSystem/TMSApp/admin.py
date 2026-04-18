from django.contrib import admin
from .models import TMSModels

# Register your models here.

@admin.register(TMSModels)
class TMSAdmin(admin.ModelAdmin):
    list_display=('id','task_name','task_status')