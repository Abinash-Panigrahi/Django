from django.shortcuts import render,HttpResponse
from .forms import SignUpForm,SignInForm
from .models import SignUpModel

# Create your views here.

def WelcomePage_view(request):
    return render(request,'SessionProjectApp/home.html')



def SignUp_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'SessionProjectApp/success.html')
    else:
        form = SignUpForm()
    context = {
        'form' : form
    }
    return render(request,'SessionProjectApp/signup.html',context)

def SignIn_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            data = SignUpModel.objects.get(email=email)
            check_email = data.email
            check_password = data.password
            if check_email == email and check_password == password:
                context = {
                    'data' : data
                }
                return render(request,'SessionProjectApp/dashboard.html',context)
            else:
                return HttpResponse('Not valid')
    else:       
        form = SignInForm()
    context = {
        'form' : form
    }
    return render(request,'SessionProjectApp/signin.html',context)