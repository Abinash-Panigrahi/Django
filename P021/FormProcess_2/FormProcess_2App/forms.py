from django import forms

class EmployeeForms(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    e_mail=forms.EmailField()