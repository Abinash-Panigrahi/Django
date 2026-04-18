from django.contrib import admin
from .models import Protien
# Register your models here.

class ProtienAdmin(admin.ModelAdmin):
    list_display=['id','product','brand','kg','price']

admin.site.register(Protien,ProtienAdmin)





