from django.shortcuts import render
from .models import Profile

# Create your views here.

def Profile_View(request):
    all_records=Profile.objects.all()
    d={'all_records':all_records}
    return render(request,'ProfileCardApp/home.html',d)

def About_view(request,id):
    about=Profile.objects.get(id=id)
    d={
        'about':about
    }
    return render(request,'ProfileCardApp/wiki.html',d)