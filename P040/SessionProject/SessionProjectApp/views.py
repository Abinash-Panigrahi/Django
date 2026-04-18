from django.shortcuts import render,HttpResponse

# Create your views here.

def Session_view(request):
    request.session['name'] = 'Abinash'
    request.session['mark'] = 99
    request.session['mail'] = 'abi@gmail.com'
    request.session['age'] = 23
    request.session['Subject'] = 'Python'

    return HttpResponse('Session is ready')

