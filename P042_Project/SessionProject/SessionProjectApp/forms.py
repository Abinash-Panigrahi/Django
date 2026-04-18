from django import forms
from .models import SignUpModel

# Create your models here.

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUpModel
        fields = ['name','email','password','gender']

class SignInForm(forms.Form):
    email = forms.CharField()
    password = forms.IntegerField()