from django import forms

class StudentForm(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    mark=forms.IntegerField()
    email=forms.EmailField()

    def clean(self):
        d=super().clean()
        name=d['name']
        age=d['age']
        mark=d['mark']
        email=d['email']

        if len(name) < 2 or len(name) > 16:
            raise forms.ValidationError('Name length should be between 2-16')
        if age < 18:
            raise forms.ValidationError('Age must be greater than 18')
        if mark < 33:
            raise forms.ValidationError('Mark must be greater than 33')