from django.shortcuts import render, redirect

from .forms import BookFormset, EquipServiceForm, RigDownForm, RigForm, EquipmentForm
from .models import Book, Rig


# Create your views here.
def equipmentLog(request):
    form = RigForm()
    equip_form = EquipmentForm()
    equip_serv_form = EquipServiceForm()
    down_form = RigDownForm()

    if request.method == 'POST':
        form = RigForm(request.POST)
        rig = form.save(commit=False)
        rig.slug = str(request.POST['rig_name']) + '-' + \
                str(request.POST['well']) + '-' + \
                str(request.POST['date']) + '-' + \
                str(request.POST['shift'])
        form.save()

        rig = Rig.objects.get(id=rig.id)
        # import pdb; pdb.set_trace()


        equip_form = EquipmentForm(request.POST)
        equipment = equip_form.save(commit=False)
        equipment.rig = rig
        equip_form.save()

        equip_serv_form = EquipServiceForm(request.POST)
        service = equip_serv_form.save(commit=False)
        service.rig = rig
        equip_serv_form.save()

        down_form = RigDownForm(request.POST)
        rig_down = down_form.save(commit=False)
        rig_down.rig = rig
        down_form.save()

        return redirect('index')

    context = {
        'form': form,
        'equip_form': equip_form,
        'equip_serv_form': equip_serv_form,
        'down_form': down_form,
    }
    return render(request, 'mechanical/equipment-log.html', context)


def electricalLog(request):
    context = {}
    return render(request, 'mechanical/electric-log.html', context)


def create_book_normal(request):
    template_name = 'mechanical/create_normal.html'
    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = BookFormset(request.GET or None)
    elif request.method == 'POST':
        formset = BookFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # extract name from each form and save
                name = form.cleaned_data.get('name')
                # save book instance
                if name:
                    Book(name=name).save()
            # once all books are saved, redirect to book list view
            return redirect('index')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })