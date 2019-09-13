from django import forms
from django.core import validators
class FormName(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
