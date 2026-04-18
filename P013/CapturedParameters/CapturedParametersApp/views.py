from django.shortcuts import render,HttpResponse

# Create your views here.

def msg_view(request,name):
    d={'name':name}
    return render(request,'CapturedParametersApp/msg.html',d)


def add_view(request,a,b):
    add=a+b
    d={'add':add}
    return render(request,'CapturedParametersApp/add.html',d)
