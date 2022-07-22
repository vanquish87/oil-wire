# forms.py :: part 1

from django import forms
from django.forms import formset_factory
from .models import EquipmentService, Rig, Equipment, RigDown


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.DateInput):
    input_type = 'time'


class RigForm(forms.ModelForm):
    class Meta:
        model = Rig
        fields = ['rig_name', 'well', 'shift', 'date', 'requirements', 'mech_engineer']
        widgets = {
            'date': DateInput(),
            'requirements': forms.Textarea(attrs={'rows':6}),
            'mech_engineer': forms.Textarea(attrs={'rows':2}),
            }

        labels = {
            'rig_name': 'Rig',
            'requirements': 'Requirement & Important Information',
            'mech_engineer': 'Signature, Name & Designation of Rig Mechanical Engineer'
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
        fields = ['equip_name', 'water_temp', 'oil_temp', 'oil_pressure', 'equip_working_hour', 'equip_avail_hour', 'equip_oil_used']

        widgets = {
            'equip_working_hour': TimeInput(),
            'equip_avail_hour': TimeInput(),
            }

        labels = {
            'equip_name': 'Equipment',
            'water_temp': 'Water Temp. (°C)',
            'oil_temp': 'Oil Temp. (°C)',
            'oil_pressure': 'Oil Pressure (kg/cm3)',
            'equip_working_hour': 'Working Hours',
            'equip_avail_hour': 'Equip Avail Hrs.',
            'equip_oil_used': 'Oil Used',
        }

    def __init__(self, *args, **kwargs):
        super(EquipmentForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class EquipServiceForm(forms.ModelForm):
    class Meta:
        model = EquipmentService
        fields = ['equip_serv_name', 'working_hour', 'avail_hour', 'oil_used', 'intstructions']

        widgets = {
            'working_hour': TimeInput(),
            'avail_hour': TimeInput(),
            'intstructions': forms.Textarea(attrs={'rows':4}),
            }

        labels = {
            'equip_serv_name': 'Equipment',
            'working_hour': 'Working Hours',
            'avail_hour': 'Equip Avail Hrs.',
            'oil_used': 'Oil Used',
            'intstructions': 'Service/Repairing Instructions & Work Done',
        }

    def __init__(self, *args, **kwargs):
        super(EquipServiceForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class RigDownForm(forms.ModelForm):
    class Meta:
        model = RigDown
        fields = ['from_hr', 'to_hr']

        widgets = {
            'from_hr': TimeInput(),
            'to_hr': TimeInput(),
            }

        labels = {
            'from_hr': 'From (Hours)',
            'to_hr': 'To (Hours)',
        }

    def __init__(self, *args, **kwargs):
        super(RigDownForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


EquipmentFormset = formset_factory(EquipmentForm, extra=3)
EquipServiceFormset = formset_factory(EquipServiceForm, extra=3)
RigDownFormset = formset_factory(RigDownForm, extra=3)