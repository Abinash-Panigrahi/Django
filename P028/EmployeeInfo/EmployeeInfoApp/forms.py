from django import forms

# Create your forms here.

class Employee_Form(forms.Form):
    name=forms.CharField()
    desg=forms.CharField()
    age=forms.IntegerField()
    sal=forms.FloatField()
    address=forms.CharField()
