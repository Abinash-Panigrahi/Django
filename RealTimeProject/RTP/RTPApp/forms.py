from django import forms
from .models import SignUpModel
from .models import ContactModels

# Create your forms here.

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUpModel
        fields = ['name','email','password','gender']

class SignInForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(max_length=20)

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModels
        fields = ['name','phone','email','message']