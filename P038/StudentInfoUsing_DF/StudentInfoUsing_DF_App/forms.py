from django import forms

# Create your forms here.

class EducationForm(forms.Form):
    college = forms.CharField()
    degree = forms.CharField()
    mark = forms.IntegerField()

class PersonalForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    email = forms.EmailField()

class ExtracuricularForm(forms.Form):
    fav_sports = forms.CharField()
    fav_actor = forms.CharField()