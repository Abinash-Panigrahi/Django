from django import forms

class StudentForm(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    mark=forms.IntegerField()
    roll_no=forms.IntegerField()
    e_mail=forms.EmailField()