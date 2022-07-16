from django.forms import ModelForm
from .models import LogFile

class LogFileForm(ModelForm):
    class Meta:
        model = LogFile
        # file = forms.FileField()
        fields = ['file']

    # with this we are modifying classes in html for form
    # didn't understand much, advanced concept
    def __init__(self, *args, **kwargs):
        super(LogFileForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})