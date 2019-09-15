from django import forms
from django.core import validators
from .models import feedback
# class FormName(forms.Form):
#     name = forms.CharField(max_length=255)
#     email = forms.EmailField()
#     feedback = forms.CharField(widget=forms.Textarea)


class formfeed(forms.ModelForm):

    class Meta():
        model = feedback
        fields = "__all__"