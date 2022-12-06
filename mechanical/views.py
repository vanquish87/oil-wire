from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *
from .models import *


# Create your views here.
def load_rigs(request):
    saswellname_id = request.GET.get('saswellname')
    sasrignames = SasRigName.objects.filter(saswellname=saswellname_id).order_by('name')

    context = {'sasrignames': sasrignames}
    return render(request, 'mechanical\well-dropdown.html', context)


@login_required(login_url='login')
def equipmentLog(request):
    form = RigForm()
    form_hsd = HsdForm()
    equip_formset = EquipmentFormset()
    equip_serv_formset = EquipServiceFormset()
    down_formset = RigDownFormset()

    if request.method == 'POST':
        form = RigForm(request.POST)
        if form.is_valid():
            rig = form.save(commit=False)
            form.save()
            rig = Rig.objects.get(id=rig.id)

        form_hsd = HsdForm(request.POST)
        if form_hsd.is_valid():
            hsd_balance = form_hsd.save(commit=False)
            hsd_balance.rig = rig
            form_hsd.save()

        equip_formset = EquipmentFormset(request.POST)
        if equip_formset.is_valid():
            for form in equip_formset:
                equipment = form.save(commit=False)
                equipment.rig = rig
                form.save()

        equip_serv_formset = EquipServiceFormset(request.POST)
        if equip_serv_formset.is_valid():
            for form in equip_serv_formset:
                service = form.save(commit=False)
                service.rig = rig
                form.save()

        down_formset = RigDownFormset(request.POST)
        if down_formset.is_valid():
            for form in down_formset:
                rig_down = form.save(commit=False)
                rig_down.rig = rig
                form.save()

        return redirect('view-equipment-log', rig.id)

    context = {
        'form': form,
        'form_hsd': form_hsd,
        'equip_formset': equip_formset,
        'equip_serv_formset': equip_serv_formset,
        'down_formset': down_formset,
    }
    return render(request, 'mechanical/create-equipment-log.html', context)


@login_required(login_url='login')
def viewEquipmentLog(request, rig_id):
    rig = Rig.objects.get(id=rig_id)
    equipments = Equipment.objects.filter(rig_id=rig.id).all()
    services = EquipmentService.objects.filter(rig_id=rig.id).all()
    rigdowns = RigDown.objects.filter(rig_id=rig.id).all()
    context = {
        'rig': rig,
        'equipments': equipments,
        'services': services,
        'rigdowns': rigdowns,
    }
    return render(request, 'mechanical/view-equipment-log.html', context)


@login_required(login_url='login')
def electricalLog(request):
    form = ElectricalRigForm()
    electrical_shift_formset = ElectricalShiftFormset()

    # # for further dev work for drowpdown menu
    # # wellid
    # wellid = [('CR_CW4#MOT16',), ('NJFN',), ('SXAG',), ('SKFJ',), ('NJFM',), ('JRFY',), ('GMBP',), ('SKFL',), ('SK#137A',), ('AKM#1',)]
    # # rigid
    # rigid = [('CW-100-I',), ('CW-100-VIII',)]

    if request.method == 'POST':
        form = ElectricalRigForm(request.POST)
        if form.is_valid():
            rig = form.save(commit=False)
            form.save()
        else:
            messages.error(request, 'Well or Rig is wrong')

        electrical_shift_formset = ElectricalShiftFormset(request.POST)
        if electrical_shift_formset.is_valid():
            for form in electrical_shift_formset:
                eshift = form.save(commit=False)
                eshift.rig = rig
                form.save()
        else:
            messages.error(request, 'You missed something in the form.')

        return redirect('view-electric-log', rig.id)

    context = {
        'form': form,
        'electrical_shift_formset': electrical_shift_formset,

    }
    return render(request, 'mechanical/electric-log.html', context)


@login_required(login_url='login')
def viewElecticLog(request,rig_id):
    rig = ElectricalRig.objects.get(id=rig_id)
    electricalShifts = ElectricalShift.objects.filter(rig_id=rig.id).all()

    context = {
        'rig': rig,
        'electricalShifts': electricalShifts,


    }
    return render(request, 'mechanical/view-electric-log.html', context)


@login_required(login_url='login')
def drillLog(request):
    form = DrillRigForm()
    drill_shift_formset = DrillShiftFormset()
    drill_laboratory_formset = DrillLaboratoryFormset()
    hydraulic_data_formset = HydraulicDataFormset()
    drill_data_formset = DrillDataFormset()
    drill_mud_chemical_formset = DrillMudChemicalReportFormset()
    drill_mud_volume_formset = DrillMudVolumeFormset()
    drill_solid_control_formset = DrillSolidControlFormset()

    if request.method == 'POST':
        form = DrillRigForm(request.POST)
        if form.is_valid():
            rig = form.save(commit=False)
            form.save()
            rig = DrillRig.objects.get(id=rig.id)

        drill_shift_formset = DrillShiftFormset(request.POST)
        if drill_shift_formset.is_valid():
            for form in drill_shift_formset:
                drillshift = form.save(commit=False)
                drillshift.rig = rig
                form.save()


        drill_laboratory_formset = DrillLaboratoryFormset(request.POST)
        if drill_laboratory_formset.is_valid():
            for form in drill_laboratory_formset:
                drilllab = form.save(commit=False)
                drilllab.rig = rig
                form.save()


        hydraulic_data_formset = HydraulicDataFormset(request.POST)
        if hydraulic_data_formset.is_valid():
            for form in hydraulic_data_formset:
                hydraulicdata = form.save(commit=False)
                hydraulicdata.rig = rig
                form.save()

        drill_data_formset = DrillDataFormset(request.POST)
        if drill_data_formset.is_valid():
            for form in drill_data_formset:
                drilldata = form.save(commit=False)
                drilldata.rig = rig
                form.save()

        drill_mud_chemical_formset = DrillMudChemicalReportFormset(request.POST)
        if drill_mud_chemical_formset.is_valid():
            for form in drill_mud_chemical_formset:
                drillmud = form.save(commit=False)
                drillmud.rig = rig
                form.save()

        drill_mud_volume_formset  = DrillMudVolumeFormset(request.POST)
        if drill_mud_volume_formset.is_valid():
            for form in drill_mud_volume_formset:
                drillmudvolume = form.save(commit=False)
                drillmudvolume.rig = rig
                form.save()

        drill_solid_control_formset = DrillSolidControlFormset(request.POST)
        if drill_solid_control_formset.is_valid():
            for form in drill_solid_control_formset:
                drillsolid = form.save(commit=False)
                drillsolid.rig = rig
                form.save()

        return redirect('view-drill-log', rig.id)

    context = {
        'form': form,
        'drill_shift_formset': drill_shift_formset,
        'drill_laboratory_formset': drill_laboratory_formset,
        'hydraulic_data_formset': hydraulic_data_formset,
        'drill_data_formset':drill_data_formset,
        'drill_mud_chemical_formset':drill_mud_chemical_formset,
        'drill_mud_volume_formset':drill_mud_volume_formset,
        'drill_solid_control_formset':drill_solid_control_formset,
    }

    return render(request, 'mechanical/drill-mud.html', context)


@login_required(login_url='login')
def viewDrillLog(request, rig_id):
    rig = DrillRig.objects.get(id=rig_id)
    drillshifts = DrillShift.objects.filter(rig_id=rig.id).all()
    drilllaboratorys = DrillLaboratory.objects.filter(rig_id=rig.id).all()
    hydraulicdatas = HydraulicData.objects.filter(rig_id=rig.id).all()
    drilldatas = Drilldata.objects.filter(rig_id=rig.id).all()
    drillchemicals = DrillMudChemicalReport.objects.filter(rig_id=rig.id).all()
    drillvolumes = DrillMudVolume.objects.filter(rig_id=rig.id).all()
    drillsolids = DrillSolidControl.objects.filter(rig_id=rig.id).all()

    context = {
        'rig': rig,
        'drillshifts': drillshifts,
        'drilllaboratorys': drilllaboratorys,
        'hydraulicdatas': hydraulicdatas,
        'drilldatas':drilldatas,
        'drillchemicals':drillchemicals,
        'drillvolumes':drillvolumes,
        'drillsolids':drillsolids,
    }

    return render(request, 'mechanical/view-drill-log.html', context)


