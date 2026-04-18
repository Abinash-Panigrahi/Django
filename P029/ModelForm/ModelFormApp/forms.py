from django import forms
from .models import Employee_Model

# Create your forms here

class Employee_Form(forms.ModelForm):
    class Meta:
        model=Employee_Model
        fields='__all__'
        # fields=['name','desg','address']

