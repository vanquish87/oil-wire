from django import forms
from django.forms import formset_factory
from mechanical.models import *
from .input import *


class RigForm(forms.ModelForm):
    class Meta:
        model = Rig
        exclude = ["user"]
        fields = ['sasrigname', 'saswellname', 'shift', 'date', 'requirements', 'mech_engineer']
        widgets = {
            'date': DateInput(),
            'requirements': forms.Textarea(attrs={'rows':6}),
            'mech_engineer': forms.Textarea(attrs={'rows':6}),
            }

        labels = {
            'sasrigname': 'Rig',
            'saswellname': 'Well No.',
            'requirements': 'Requirement & Important Information',
            'mech_engineer': 'Signature, Name & Designation of Rig Mechanical Engineer'
        }

    def __init__(self, *args, **kwargs):
        super(RigForm, self).__init__(*args, **kwargs)

        # to create empty list initially
        self.fields['sasrigname'].queryset = SasRigName.objects.none()

        if 'saswellname' in self.data:
            try:
                saswellname_id = int(self.data.get('saswellname'))
                self.fields['sasrigname'].queryset = SasRigName.objects.filter(saswellname=saswellname_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset

        elif self.instance.pk:
            self.fields['sasrigname'].queryset = self.instance.sasrigname.order_by('name')

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        # self.fields['shift'].widget.attrs.update({'class': 'form-check-input'})


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        exclude = ["equip_user"]
        fields = ['equip_name', 'water_temp', 'oil_temp', 'oil_pressure', 'equip_working_hour', 'equip_avail_hour', 'equip_oil_used', 'oil_grade', 'oil_level']

        widgets = {
            'equip_working_hour': forms.NumberInput(attrs={'max':24}),
            'equip_avail_hour': forms.NumberInput(attrs={'max':24}),
            'equip_oil_used': forms.NumberInput(attrs={'min':0}),
            'oil_pressure': forms.NumberInput(attrs={'min':0}),
            'oil_level': forms.NumberInput(attrs={'min':0}),
            }

        labels = {
            'equip_name': 'Equipment',
            'water_temp': 'Water Temp. (°C)',
            'oil_temp': 'Oil Temp. (°C)',
            'oil_pressure': 'Oil Pressure (kg/cm3)',
            'equip_working_hour': 'Working Hours',
            'equip_avail_hour': 'Equipment Available Hours',
            'equip_oil_used': 'Oil Used (Ltr.)',
            'oil_grade': 'Oil Grade',
            'oil_level': 'Oil Level (Ltr.)',
        }

    def __init__(self, *args, **kwargs):
        super(EquipmentForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class EquipServiceForm(forms.ModelForm):
    class Meta:
        model = EquipmentService
        exclude=['service_user']
        fields = ['service_user','equip_serv_name', 'working_hour', 'avail_hour', 'oil_used', 'intstructions']

        widgets = {
            'working_hour': forms.NumberInput(attrs={'max':24}),
            'avail_hour': forms.NumberInput(attrs={'max':24}),
            'oil_used': forms.NumberInput(attrs={'min':0}),
            'intstructions': forms.Textarea(attrs={'rows':4}),
            }

        labels = {
            'equip_serv_name': 'Equipment',
            'working_hour': 'Working Hours',
            'avail_hour': 'Equipment Available Hours',
            'oil_used': 'Oil Used (Ltr.)',
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
        exclude=['rigdown_user']
        fields = ['rigdown_user','from_hr', 'to_hr']

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


class HsdForm(forms.ModelForm):
    class Meta:
        model = HSD_balance
        fields = ['tank', 'opening', 'consumption', 'received', 'closing_bal']
        exclude=['hsd_user']
        widgets = {
            'opening': forms.NumberInput(attrs={'min':0}),
            'consumption': forms.NumberInput(attrs={'min':0}),
            'received': forms.NumberInput(attrs={'min':0}),
            'closing_bal': forms.NumberInput(attrs={'min':0}),
            }

        labels = {
            'opening': 'Opening (Ltr.)',
            'consumption': 'Consumption (Ltr.)',
            'received': 'Received (Ltr.)',
            'closing_bal': 'Closing Balance (Ltr.)',
        }

    def __init__(self, *args, **kwargs):
        super(HsdForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


# EquipmentFormset = formset_factory(EquipmentForm, extra=1)
# EquipServiceFormset = formset_factory(EquipServiceForm, extra=1)
# RigDownFormset = formset_factory(RigDownForm, extra=1)
# HsdFormset = formset_factory(HsdForm, extra=1)

