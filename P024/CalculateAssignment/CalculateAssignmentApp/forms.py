from django import forms

class Calculator(forms.Form):
    Num_1=forms.IntegerField()
    Num_2=forms.IntegerField()
    operation=forms.CharField()