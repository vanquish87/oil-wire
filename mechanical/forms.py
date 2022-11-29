from django import forms
from django.forms import formset_factory
from .models import EquipmentService, Rig, Equipment, RigDown, DrillRig, DrillShift, DrillLaboratory, HydraulicData, Drilldata,ElectricalRig,ElectricalShift,Electricalrunninghours, DrillMudChemicalReport, DrillMudVolume, DrillSolidControl


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


#Drill Models
class DrillRigForm(forms.ModelForm):
    class Meta:
        model = DrillRig
        fields = ['rig_name', 'well', 'asset', 'date']
        widgets = {
            'date': DateInput(),
            }

        labels = {
            'rig_name': 'Rig',
            'well': 'Well No.',
            'asset': 'Asset/Basin',
            'date':'DATE:'
        }

    def __init__(self, *args, **kwargs):
        super(DrillRigForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class DrillShiftForm(forms.ModelForm):
    class Meta:
        model = DrillShift
        fields = ['drillfrom', 'drillto', 'timefrom', 'timeto', 'operation','spgrade','visc','gel','ph','shifttype' ]
        widgets = {
            'timefrom': TimeInput(),
            'timeto': TimeInput(),
            'operation':forms.Textarea(attrs={'rows':6}),
            }

        labels = {
            'shifttype': 'Shift Type',
            'drillfrom': 'DRILLED FROM',
            'drillto': 'TO (MTS.)',
            'timefrom':'From',
            'timeto': 'To',
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
        fields = ['sample', 'time', 'depth', 'apifilter',
        'cakethickness', 'ph', 'sand', 'apparentvisc','plasticvisc','yieldpoint',
        'gelzero','gelten','oilcontent','solidcontent','watercontent','mbc','filtersalinity','flowlinetemp']

        widgets = {
            'time': TimeInput(),
            }
       
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
        fields = ['pumplinersize', 'strokelength', 'discharge',
        'stroke', 'standpipepressure', 'dpsize', 'dcsize', 'stabilizers','ohdc','ohdp',
        'casdp','lastcasingsize','lastlength','csgvol','mudhole','sandtrap','pitvol','totalcirc','lagtime',
        'cycletime','ECD','presslosses']
       
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
        fields = ['sample', 'bitsize', 'jetsize',
        'onbit', 'rotaryrpm', 'bhalengths']
       
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
        fields = ['chemical', 'unit', 'opening',
        'receipt', 'consumption', 'closing', 'total']
       
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
        fields = ['shalevole', 'shalespgr', 'settingvole', 'settingspgr',
        'intervole', 'interspgr', 'suctionvole', 'suctionspgr','tank1vole','tank1spgr','tank2vole','tank2spgr']

        labels = {
            'shalevole': 'Vol (m)',
            'shalespgr': 'Sp. Gr.',
            'settingvole': 'Vol (m)',
            'settingspgr': 'Sp. Gr.',
            'intervole': 'Vol (m)',
            'interspgr': 'Sp. Gr.',
            'suctionvole':'Vol (m)',
            'suctionspgr': 'Sp. Gr.',
            'tank1vole': 'Vol (m)',
            'tank1spgr':'Sp. Gr.',
            'tank2vole': 'Vol (m)',
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
        fields = ['shaleshaker', 'desander', 'desilter', 'degasser', 'mudlcleaner','remarks']
        widgets = {
            'remarks':forms.Textarea(attrs={'rows':6}),
            }

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


DrillShiftFormset = formset_factory(DrillShiftForm, extra=1)
DrillLaboratoryFormset = formset_factory(DrillLaboratoryForm, extra=1)
HydraulicDataFormset = formset_factory(HydraulicDataForm, extra=1)
DrillDataFormset = formset_factory(DrilldataForm, extra=1)
DrillMudChemicalReportFormset= formset_factory(DrillMudChemicalReportForm, extra=1)
DrillMudVolumeFormset=formset_factory(DrillMudVolumeForm, extra=1)
DrillSolidControlFormset=formset_factory(DrillSolidControlForm, extra=1)


#ElectricalShift models
class ElectricalRigForm(forms.ModelForm):
    class Meta:
        model = ElectricalRig
        fields = ['rig_name', 'well', 'location',
        'date', 'doc_no']

        widgets = {
            'date': DateInput(),
            
            }
        labels = {
            'rig_name': 'Name of RIG',
            'well': 'Well NO.',
            'location': 'Location',
            'date': 'DATE',
            'doc_no': 'QHSE | DOC. NO.',
        }

    def __init__(self, *args, **kwargs):
        super(ElectricalRigForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class ElectricalrunninghoursForm(forms.ModelForm):
    class Meta:
        model = Electricalrunninghours
        fields = ['runninghours']

        labels = {
            'runninghours': 'Hours',
        }

    def __init__(self, *args, **kwargs):
        super(ElectricalrunninghoursForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class ElectricalShiftForm(forms.ModelForm):
    class Meta:
        model = ElectricalShift
        fields = ['equipdetails', 'equipstatus', 'runninghours', 'breakfrom', 'breakto','totalcummulative',
        'remarks','equipment','job','energydg1','energydg2','energydg3','energydg4','safetyreport','shifttype']
        widgets = {
            'breakfrom': TimeInput(),
            'runninghours': forms.NumberInput(attrs={'max':24}),
            'breakto': TimeInput(),
            'remarks':forms.Textarea(attrs={'rows':3}),
            'equipment':forms.Textarea(attrs={'rows':3}),
            'job':forms.Textarea(attrs={'rows':3}),
            'safetyreport':forms.Textarea(attrs={'rows':3}),
            }

        labels = {
            'equipdetails': 'Equipment Details & Ratings',
            'equipstatus': 'Equipment Status',
            'runninghours': 'Running Hours during the shift',
            'breakfrom':'From (Hours)',
            'breakto': 'To (Hours)',
            'totalcummulative': 'Total Cumulative Running Hours',
            'remarks': 'Remarks/Requirements from Base, if any:',
            'equipment':'Equipment/Material Received/Sent:',
            'job': 'Job Caring Out During the Shift: Defect/Failure reports, if any',
            'energydg1': 'DG-1 :',
            'energydg2':'DG-2 :',
            'energydg3':'DG-3 :',
            'energydg4':'DG-4 :',
            'safetyreport':'Report on Safety/ Near Miss Accidents:',
            'shifttype':'Shift Type',
        }

    def __init__(self, *args, **kwargs):
        super(ElectricalShiftForm, self).__init__(*args, **kwargs)

        # to avoid repetition for every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


ElectricalrunninghoursFormset = formset_factory(ElectricalrunninghoursForm, extra=1)
ElectricalShiftFormset = formset_factory(ElectricalShiftForm, extra=1)