from django.shortcuts import render, redirect

from .forms import EquipServiceForm, EquipServiceFormset, EquipmentFormset, RigDownForm, RigDownFormset, RigForm, EquipmentForm
from .models import Rig, Equipment, EquipmentService, RigDown


# Create your views here.
def equipmentLog(request):
    form = RigForm()
    equip_formset = EquipmentFormset()
    equip_serv_formset = EquipServiceFormset()
    down_formset = RigDownFormset()

    if request.method == 'POST':
        form = RigForm(request.POST)
        if form.is_valid():
            rig = form.save(commit=False)
            form.save()
            rig = Rig.objects.get(id=rig.id)

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
        'equip_formset': equip_formset,
        'equip_serv_formset': equip_serv_formset,
        'down_formset': down_formset,
    }
    return render(request, 'mechanical/create-equipment-log.html', context)

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

def electricalLog(request):
    context = {}
    return render(request, 'mechanical/electric-log.html', context)


def drillLog(request):
    context = {}
    return render(request, 'mechanical/drill-mud.html', context)
