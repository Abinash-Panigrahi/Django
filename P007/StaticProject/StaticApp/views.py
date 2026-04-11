from django.shortcuts import render

# Create your views here.

def avenger_view(request):
    return render(request,'StaticApp/home.html')
