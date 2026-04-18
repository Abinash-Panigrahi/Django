from django import forms

# Create your forms here.

class ProductForm(forms.Form):
    product_Name = forms.CharField()
    quantity = forms.IntegerField()