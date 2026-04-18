from django import forms
from .models import Resume

class ResumeFormPart1(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'age', 'address1', 'address2', 'state', 'city', 'email', 'mobile', 'linkedin', 'github']

class ResumeFormPart2(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['designation', 'summary', 'experience_company_details', 'experience']
