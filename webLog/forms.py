from django import forms
from django.forms import ModelForm
from .models import Log

class UploadFileForm(ModelForm):
    class Meta:
        model = Log
        # file = forms.FileField()
        fields = ['file']

    # with this we are modifying classes in html for form
    # didn't understand much, advanced concept
    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})