from django import forms
from app.models import *

class CountryModelForm(forms.ModelForm):
    class Meta:
        model=Country
        fields='__all__'
class CapitalModelForm(forms.ModelForm):
    class Meta:
        model=Capital
        fields='__all__'