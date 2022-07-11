from django import forms
from django.forms import ModelForm
from .models import Log

class UploadFileForm(ModelForm):
    class Meta:
        model = Log
        # file = forms.FileField()
        fields = ['file']