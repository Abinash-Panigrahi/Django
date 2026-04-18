from django.contrib import admin
from .models import DCA

# Register your models here.

@admin.register(DCA)
class DCAAdmin(admin.ModelAdmin):
    list_display=['id','country','capital','population','readmore']