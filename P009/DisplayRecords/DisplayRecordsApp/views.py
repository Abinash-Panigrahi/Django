from django.shortcuts import render
from .models import Shirt

# Create your views here.

def retrieve_view(request):
    record=Shirt.objects.all()
    d={'records':record}
    return render(request,'DisplayRecordsApp/shirts.html',d)

