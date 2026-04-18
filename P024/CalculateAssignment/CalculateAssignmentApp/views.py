from django.shortcuts import render,HttpResponse
from .forms import Calculator

# Create your views here.

def Calculator_view(request):
    if request.method=='POST':
        form=Calculator(request.POST)
        if form.is_valid():
            a=form.cleaned_data['Num_1']
            b=form.cleaned_data['Num_2']
            op=form.cleaned_data['operation']
            if op=='+':
                sum=a+b
                d={'sum':sum}
                return render(request,'CalculateAssignmentApp/calculator.html',d)
            elif op=='*':
                mul=a*b
                d={'mul':mul}
                return render(request,'CalculateAssignmentApp/calculator.html',d)
            elif op=='-':
                sub=a-b
                d={'sub':sub}
                return render(request,'CalculateAssignmentApp/calculator.html',d)
            else:
                return HttpResponse('Not a valid operation')
    form=Calculator()
    d={'form':form}
    return render(request,'CalculateAssignmentApp/home.html',d)
