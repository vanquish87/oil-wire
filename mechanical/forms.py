# forms.py :: part 1

from django import forms
from django.forms import formset_factory
from .models import EquipmentService, Rig, Equipment


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.DateInput):
    input_type = 'time'


class RigForm(forms.ModelForm):
    class Meta:
        model = Rig
        fields = ['name', 'well', 'shift', 'date']
        widgets = {
            'date': DateInput()
            }

        labels = {
            'name': 'Rig',
        }

    def __init__(self, *args, **kwargs):
        super(RigForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        # self.fields['shift'].widget.attrs.update({'class': 'form-check-input'})


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'water_temp', 'oil_temp', 'oil_pressure', 'working_hour', 'equi_avail_hour', 'oil_used']

        widgets = {
            'working_hour': TimeInput(),
            'equi_avail_hour': TimeInput(),
            }

        labels = {
            'name': 'Equipment',
            'water_temp': 'Water Temp. (°C)',
            'oil_temp': 'Oil Temp. (°C)',
            'oil_pressure': 'Oil Pressure (kg/cm3)',
            'working_hour': 'Working Hours',
            'equi_avail_hour': 'Equip Avail Hrs.',
            'oil_used': 'Oil Used',
        }

    def __init__(self, *args, **kwargs):
        super(EquipmentForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class EquipServiceForm(forms.ModelForm):
    class Meta:
        model = EquipmentService
        fields = ['name', 'working_hour', 'equi_avail_hour', 'oil_used', 'intstructions', 'rig_downtime_from', 'rig_downtime_to', 'requirements']

        widgets = {
            'working_hour': TimeInput(),
            'equi_avail_hour': TimeInput(),
            'intstructions': forms.Textarea(attrs={'rows':4}),
            'rig_downtime_from': TimeInput(),
            'rig_downtime_to': TimeInput(),
            'requirements': forms.Textarea(attrs={'rows':4}),
            }

        labels = {
            'name': 'Equipments',
            'working_hour': 'Working Hours',
            'equi_avail_hour': 'Equip Avail Hrs.',
            'oil_used': 'Oil Used',
            'intstructions': 'Service/Repairing Instructions & Work Done',
            'rig_downtime_from': 'From (Hours)',
            'rig_downtime_to': 'To (Hours)',
            'requirements': 'Requirement & Important Information',
        }

    def __init__(self, *args, **kwargs):
        super(EquipServiceForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class BookForm(forms.Form):
    name = forms.CharField(
        label='Book Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name'
        })
    )

BookFormset = formset_factory(BookForm, extra=2)