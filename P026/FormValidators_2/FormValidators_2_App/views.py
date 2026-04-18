from django.shortcuts import render
from .forms import StudentForm


# Create your views here.

def Student_view(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        data_valid=False
        if form.is_valid():
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            mark=form.cleaned_data['mark']
            email=form.cleaned_data['email']
            data_valid=True
            d={'data_valid':data_valid}
            return render(request,'FormValidators_2_App/display.html',d)
        else:
            return render(request,'FormValidators_2_App/forms.html',{'form':form})
    form=StudentForm()
    d={'form':form}
    return render(request,'FormValidators_2_App/forms.html',d)