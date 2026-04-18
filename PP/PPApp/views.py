from django.shortcuts import render,HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse('Hello Ipsita')


def name_view(request):
    return render(request,'PPApp/name.html')

