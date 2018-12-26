from django import forms
from .models import ExcelFile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=False)
    password = forms.CharField(max_length=100, required=False)


class ExcelFileForm(forms.ModelForm):
    class Meta:
        model = ExcelFile
        fields = ('file',)