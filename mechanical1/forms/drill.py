from django import forms
from django.forms import formset_factory
from mechanical.models import *
from .input import *


#Drill Models
class DrillRigForm(forms.ModelForm):
    class Meta:
        model = DrillRig
        exclude = ["user_drill"]
        fields = ['sasrigname', 'saswellname', 'asset', 'date', 'shifttype']
        widgets = {
            'date': DateInput(),
            }

        labels = {
            'sasrigname': 'Rig',
            'saswellname': 'Well No.',
            'asset': 'Asset/Basin',
            'date':'DATE:',
            'shifttype': 'Shift Type',
        }

    def __init__(self, *args, **kwargs):
        super(DrillRigForm, self).__init__(*args, **kwargs)

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

class DrillShiftForm(forms.ModelForm):
    class Meta:
        model = DrillShift
        exclude = ["drill_shift_user"]
        fields = ['drillfrom', 'drillto', 'timefrom', 'timeto', 'operation', 'spgrade', 'visc', 'gel', 'ph' ]
        widgets = {
            'timefrom': TimeInput(),
            'timeto': TimeInput(),
            'drillfrom': forms.NumberInput(attrs={'min':0}),
            'drillto': forms.NumberInput(attrs={'min':0}),
            'spgrade': forms.NumberInput(attrs={'min':0}),
            'visc': forms.NumberInput(attrs={'min':0}),
            'gel': forms.NumberInput(attrs={'min':0}),
            'ph': forms.NumberInput(attrs={'min':0}),
            'operation':forms.Textarea(attrs={'rows':6}),
            }

        labels = {
            'drillfrom': 'Drilled From (mtr)',
            'drillto': 'To (mtr)',
            'timefrom':'From (Hours)',
            'timeto': 'To (Hours)',
            'operation': 'Operation',
            'spgrade': 'Sp. Gr.',
            'visc':'Visc(Sec.)',
            'gel': 'Gel 10',
            'ph': 'pH',
        }

    def __init__(self, *args, **kwargs):
        super(DrillShiftForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class DrillLaboratoryForm(forms.ModelForm):
    class Meta:
        model = DrillLaboratory
        exclude = ["drill_lab_user"]
        fields = ['sample', 'time', 'depth', 'apifilter',
        'cakethickness', 'ph', 'sand', 'apparentvisc','plasticvisc','yieldpoint',
        'gelzero','gelten','oilcontent','solidcontent','watercontent','mbc','filtersalinity','flowlinetemp']

        widgets = {'time': TimeInput(),}

        # from depth to filtersalinity
        for i in range(2, len(fields)-1):
            widgets[fields[i]] = forms.NumberInput(attrs={'min':0})

        labels = {
            'sample': 'Sample Type',
            'time': 'Time',
            'depth': 'Depth',
            'apifilter': 'API Filtration',
            'cakethickness': 'Cake Thickness',
            'ph': 'pH',
            'sand':'Sand',
            'apparentvisc': 'Apparent Visc.(cp)',
            'plasticvisc': 'Plastic Visc.(cp)',
            'yieldpoint':'Yield Point(Lbs/100ft',
            'gelzero': 'Gel 0(Lbs/100ft)',
            'gelten': 'Gel 10(Lbs/100ft)',
            'oilcontent': 'Oil Content(%v/v)',
            'solidcontent': 'Solid Content(%v/v)',
            'watercontent': 'Water Content(%v/v)',
            'mbc': 'MBC',
            'filtersalinity':'Filtrate Salinity(gm/ml)',
            'flowlinetemp': 'Flow Line Temp(°C)',
        }

    def __init__(self, *args, **kwargs):
        super(DrillLaboratoryForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class HydraulicDataForm(forms.ModelForm):
    class Meta:
        model = HydraulicData
        exclude = ["hyd_data_user"]
        fields = ['pumplinersize', 'strokelength', 'discharge',
        'stroke', 'standpipepressure', 'dpsize', 'dcsize', 'stabilizers','ohdc','ohdp',
        'casdp','lastcasingsize','lastlength','csgvol','mudhole','sandtrap','pitvol','totalcirc','lagtime',
        'cycletime','ECD','presslosses']

        widgets = {}

        # from depth to filtersalinity
        for i in range(len(fields)):
            widgets[fields[i]] = forms.NumberInput(attrs={'min':0})

        labels = {
            'pumplinersize': 'Pump Liner Size',
            'strokelength': 'Stroke Length',
            'discharge': 'Discharge',
            'stroke': 'Stroke/min.',
            'standpipepressure': 'Stand Pipe Pressure',
            'dpsize':'DP Size/Length',
            'dcsize': 'DC Size/Length',
            'stabilizers':'No. of Stabilizers',
            'ohdc': '(a) OH-DC',
            'ohdp':'(b) OH-DP',
            'casdp': '(c) Cas-DP',
            'lastcasingsize': 'Last Casing Size',
            'lastlength': 'Last csg. Length',
            'csgvol':'Csg. Vol(m',
            'mudhole': 'Mud in Hole(m',
            'sandtrap': 'Sand Trap Vol.(m',
            'pitvol': 'Pit Vol. in circ(m',
            'totalcirc':'Total circ. Vol(m',
            'lagtime': 'Lag Time(min)',

            'cycletime': 'Cycle Time(min)',
            'ECD':'E.C.D.',
            'presslosses': 'Ann. Press Losses',

        }

    def __init__(self, *args, **kwargs):
        super(HydraulicDataForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class DrilldataForm(forms.ModelForm):
    class Meta:
        model = Drilldata
        exclude = ["drill_data_user"]
        fields = ['sample', 'bitsize', 'jetsize',
        'onbit', 'rotaryrpm', 'bhalengths']

        widgets = {}

        # from depth to filtersalinity
        for i in range(1, len(fields)):
            widgets[fields[i]] = forms.NumberInput(attrs={'min':0})

        labels = {
            'sample': 'Sample Type',
            'bitsize': 'Bit Size(Inches)',
            'jetsize': 'Jet Size(Inches)',
            'onbit': 'Wt. on Bit(MT)',
            'rotaryrpm': 'Rotary RPM',
            'bhalengths':'BHA Length(mts)',
        }

    def __init__(self, *args, **kwargs):
        super(DrilldataForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class DrillMudChemicalReportForm(forms.ModelForm):
    class Meta:
        model = DrillMudChemicalReport
        exclude = ["drill_mud_user"]
        fields = ['chemical', 'unit', 'opening',
        'receipt', 'consumption', 'closing', 'total']

        widgets = {}

        # from depth to filtersalinity
        for i in range(len(fields)):
            widgets[fields[i]] = forms.NumberInput(attrs={'min':0})

        labels = {
            'chemical': 'Chemical',
            'unit': 'Unit',
            'opening': 'Opening Balance',
            'receipt': 'Receipt',
            'consumption': 'Consumption',
            'closing':'Closing Balance',
            'total':'Cumulative Consumption',
        }

    def __init__(self, *args, **kwargs):
        super(DrillMudChemicalReportForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class DrillMudVolumeForm(forms.ModelForm):
    class Meta:
        model = DrillMudVolume
        exclude = ["drill_vol_user"]
        fields = ['shalevole', 'shalespgr', 'settingvole', 'settingspgr',
        'intervole', 'interspgr', 'suctionvole', 'suctionspgr','tank1vole','tank1spgr','tank2vole','tank2spgr']

        widgets = {}

        # from depth to filtersalinity
        for i in range(len(fields)):
            widgets[fields[i]] = forms.NumberInput(attrs={'min':0})

        labels = {
            'shalevole': 'Shale Shaker (Vol (m))',
            'shalespgr': 'Sp. Gr.',
            'settingvole': 'Setting Tank (Vol (m))',
            'settingspgr': 'Sp. Gr.',
            'intervole': 'Intermediate Tank (Vol (m))',
            'interspgr': 'Sp. Gr.',
            'suctionvole':'Suction Tank (Vol (m))',
            'suctionspgr': 'Sp. Gr.',
            'tank1vole': 'Reserver Tank-1 (Vol (m))',
            'tank1spgr':'Sp. Gr.',
            'tank2vole': 'Reserver Tank-2 (Vol (m))',
            'tank2spgr':'Sp. Gr.',
        }

    def __init__(self, *args, **kwargs):
        super(DrillMudVolumeForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})



class DrillSolidControlForm(forms.ModelForm):
    class Meta:
        model = DrillSolidControl
        exclude = ["drill_solid_user"]
        fields = ['shaleshaker', 'desander', 'desilter', 'degasser', 'mudlcleaner','remarks']
        widgets = {
            'remarks':forms.Textarea(attrs={'rows':6}),
            }

        # from depth to filtersalinity
        for i in range(len(fields)-1):
            widgets[fields[i]] = forms.NumberInput(attrs={'min':0})

        labels = {
            'shaleshaker': 'Shale Shaker',
            'desander': 'Desander',
            'desilter': 'Desilter',
            'degasser':'Degasser',
            'mudlcleaner': 'Mud Cleaner',
            'remarks': 'Remarks',
        }

    def __init__(self, *args, **kwargs):
        super(DrillSolidControlForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


# DrillShiftFormset = formset_factory(DrillShiftForm, extra=1)
# DrillLaboratoryFormset = formset_factory(DrillLaboratoryForm, extra=2)
# HydraulicDataFormset = formset_factory(HydraulicDataForm, extra=1)
# DrillDataFormset = formset_factory(DrilldataForm, extra=2)
# DrillMudChemicalReportFormset= formset_factory(DrillMudChemicalReportForm, extra=1)
# DrillMudVolumeFormset=formset_factory(DrillMudVolumeForm, extra=1)
# DrillSolidControlFormset=formset_factory(DrillSolidControlForm, extra=1)
