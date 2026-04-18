from django.shortcuts import render
from .models import DCA

# Create your views here.

def country(request):
    all_records=DCA.objects.all()
    d={'all_records':all_records}
    return render(request,'DCAApp/home.html',d)

def specific_country(request,id):
    record=DCA.objects.get(id=id)
    d={'record':record}
    return render(request,'DCAApp/desc.html',d)