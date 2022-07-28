from unittest.util import _MAX_LENGTH
from django import forms

class CreateNewList(forms.Form):
    myans = forms.CharField(label="Answer",max_length=1000)