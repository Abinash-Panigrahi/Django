from django import forms

class StudentForms(forms.Form):
    name=forms.CharField(required='False')
    age=forms.IntegerField(label_suffix='-')
    mark=forms.IntegerField(label='hello')
    email=forms.EmailField(required='False',label='Mail_id')
    country=forms.CharField(initial='India',disabled='True')
    bio=forms.CharField(widget=forms.Textarea,help_text='Maximum 120 char',max_length=120)
    upload_cv=forms.FileField()
    upload_photo=forms.ImageField()
    agree=forms.CharField(widget=forms.CheckboxInput)