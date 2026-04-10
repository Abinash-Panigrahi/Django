from django.shortcuts import render
from datetime import datetime

# Create your views here.


def time_view(request):
    current_datetime=datetime.now()
    time=current_datetime.strftime('%H:%M:%S')
    d={'time':time}
    return render(request,'TemplateApp/home.html',d)