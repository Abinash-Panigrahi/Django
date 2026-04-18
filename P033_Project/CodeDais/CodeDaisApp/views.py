from django.shortcuts import render,HttpResponse
from .forms import SignUpForm,SignInForm
from .models import SignUpModel

# Create your views here.

def Base_view(request):
    return render(request,'CodeDaisApp/base.html')

def SignUp_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'CodeDaisApp/signup_success.html')
    else:
        form = SignUpForm()
        context = {
            'form' : form
        }
        return render(request,'CodeDaisApp/signup.html',context)  

def Sign_In_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            data = SignUpModel.objects.get(email = email)
            check_email = data.email   
            check_password = data.password
            if check_email == email and check_password == password:
                context = {
                    'data' : data
                }       
                return render(request,'CodeDaisApp/signin_success.html',context)
            else:
                return HttpResponse('Not valid')
    else:
        form = SignInForm()
        context = {
            'form' : form
        }
        return render(request,'CodeDaisApp/signin.html',context)

def Front_view(request):
    return render(request,'CodeDaisApp/front.html')

def About_view(request):
    return render(request,'CodeDaisApp/about_us.html')

def Python_view(request):
    return render(request,'CodeDaisApp/python.html')