from django.shortcuts import render,HttpResponse
from datetime import datetime

# Create your views here.

def get_time(request):
    now=datetime.now()
    return HttpResponse(now)

