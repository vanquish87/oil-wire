from django import forms
from django.forms import formset_factory
from mechanical.models import *
from .input import *
import datetime


#ElectricalShift models
class ElectricalRigForm(forms.ModelForm):
    class Meta:
        model = ElectricalRig
        exclude = ["user_electric"]
        fields = ['sasrigname', 'saswellname', 'location',
        'date', 'doc_no']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date','disabled':'disabled', 'value': datetime.datetime.today().strftime("%d%m%Y%H%M%S")}),
            }

        labels = {
            'saswellname': 'Well No.',
            'sasrigname': 'Rig',
            'location': 'Location',
            'date': 'DATE',
            'doc_no': 'QHSE | DOC. NO.',
        }

    def __init__(self, *args, **kwargs):
        super(ElectricalRigForm, self).__init__(*args, **kwargs)

        # to create empty list initially
        self.fields['sasrigname'].queryset = SasRigName.objects.none()

        if 'saswellname' in self.data:
            try:
                saswellname_id = int(self.data.get('saswellname'))
                self.fields['sasrigname'].queryset = SasRigName.objects.filter(saswellname=saswellname_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty sasrigname queryset

        elif self.instance.pk:
            self.fields['sasrigname'].queryset = self.instance.sasrigname.order_by('name')


        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})



class ElectricalShiftForm(forms.ModelForm):
    class Meta:
        model = ElectricalShift
        exclude = ["electric_user"]
        fields = ['equipdetails', 'equipstatus', 'runninghours_prev', 'runninghours', 'breakfrom', 'breakto','totalcummulative',
        'remarks','equipment','job','energydg1','energydg2','energydg3','energydg4','safetyreport','shifttype']
        widgets = {
            'breakfrom': TimeInput(),
            'runninghours': forms.NumberInput(attrs={'max':24}),
            'breakto': TimeInput(),
            'breakfrom': TimeInput(),
            'energydg1': forms.NumberInput(attrs={'min':0}),
            'energydg2': forms.NumberInput(attrs={'min':0}),
            'energydg3': forms.NumberInput(attrs={'min':0}),
            'energydg4': forms.NumberInput(attrs={'min':0}),
            'remarks':forms.Textarea(attrs={'rows':3}),
            'equipment':forms.Textarea(attrs={'rows':3}),
            'job':forms.Textarea(attrs={'rows':3}),
            'safetyreport':forms.Textarea(attrs={'rows':3}),
            }

        labels = {
            'equipdetails': 'Equipment Details & Ratings',
            'equipstatus': 'Equipment Status',
            'runninghours_prev': 'Previous day Cumulative running hours',
            'runninghours': 'Running Hours during the shift',
            'breakfrom':'From (Hours)',
            'breakto': 'To (Hours)',
            'totalcummulative': 'Total Cumulative Running Hours',
            'remarks': 'Remarks/Requirements from Base, if any:',
            'equipment':'Equipment/Material Received/Sent:',
            'job': 'Job Caring Out During the Shift: Defect/Failure reports, if any',
            'energydg1': 'DG-1',
            'energydg2':'DG-2',
            'energydg3':'DG-3',
            'energydg4':'DG-4',

            'safetyreport':'Report on Safety/ Near Miss Accidents:',
            'shifttype':'Shift Type',
        }


    def __init__(self, *args, **kwargs):
        super(ElectricalShiftForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        # self.fields['energydg1'].widget.attrs.update({'required': 'required'})
        # self.fields['energydg2'].widget.attrs.update({'required': 'required'})
        # self.fields['energydg3'].widget.attrs.update({'required': 'required'})
        # self.fields['energydg4'].widget.attrs.update({'required': 'required'})


# ElectricalShiftFormset = formset_factory(ElectricalShiftForm, extra=1)
