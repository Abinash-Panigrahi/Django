from django.shortcuts import render
from .forms import Password_Check

# Create your views here.

def Password_view(request):
    if request.method=='POST':
        form=Password_Check(request.POST)
        if form.is_valid():
            password=form.cleaned_data['password']
            confirm_password=form.cleaned_data['confirm_password']
            if password==confirm_password:
                d={'matched':True}
                return render(request,'PasswordCheckApp/welcome.html',d)
            else:
                d={'matched':False}
                return render(request,'PasswordCheckApp/welcome.html',d)
            
    form=Password_Check()
    d={'form':form}
    return render(request,'PasswordCheckApp/check.html',d)

