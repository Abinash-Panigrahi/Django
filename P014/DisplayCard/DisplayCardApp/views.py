from django.shortcuts import render
from .models import Student

# Create your views here.

def retrieve_view(request):
    records=Student.objects.all()
    d={'records':records}
    return render(request,'DisplayCardApp/records.html',d)










