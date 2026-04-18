from django import forms

class Password_Check(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)