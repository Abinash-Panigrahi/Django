from django.shortcuts import render,redirect,HttpResponse
from .forms import SignInForm,SignUpForm
from .models import SignUpModel
from .forms import ContactForm
from django.contrib.auth import logout
from django.contrib.sessions.models import Session

# Create your views here.

def Home_view(request):
        user_id = request.session.get('user_id')
        # Session.objects.all().delete()
        context = {}
        if user_id:
            user = SignUpModel.objects.get(id = user_id)
            context = {
                'user' : user
            }
            return render(request,'RTPApp/index.html',context)
        return render(request,'RTPApp/index.html',context)
        # else:
        #     return render(request,'RTPApp/index.html')


def Service_view(request):
    return render(request,'RTPApp/service.html')


def About_view(request):
    return render(request,'RTPapp/about.html')


def Project_view(request):
    return render(request,'RTPapp/project.html')


def Testimonial_view(request):
    return render(request,'RTPapp/testimonial.html')


def Contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'RTPApp/contact_success.html')
    else:
        form = ContactForm()
    return render(request,'RTPapp/contact.html',{'form':form})


def Sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'RTPApp/signup_success.html')
    else:
        form = SignUpForm()
        context = {
            'form' : form
        }
        return render(request,'RTPapp/sign_up.html',context)
    
    
# def Signup_Success_View(request):
#     return render(request,'RTPApp/signup_success.html')
    

def Sign_in_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            data = SignUpModel.objects.get(email = email)
            if data and data.password == password:
                request.session['user_id'] = data.id
                request.session['user_name'] = data.name
                return redirect('dashboard')
            else:
                return HttpResponse('Not matched')

    else:
        form = SignInForm()
        context = {
            'form' : form
        }
        return render(request,'RTPApp/signin.html',context)
    

def Dashboard_view(request):
        user_id = request.session.get('user_id')
        if user_id:
            user = SignUpModel.objects.get(id = user_id)
            context = {
                'user' : user
            }
            return render(request,'RTPApp/dashboard.html',context)


# def Contact_view(request):
#     form = ContactModels()
#     context = {
#         'form' : form
#     }
#     return render(request,'RTPApp/contact.html',context)


def Logout_view(request):
    logout(request)
    return redirect('home')



def base_view(request):
    return render(request,'RTPApp/base.html')