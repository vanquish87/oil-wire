from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *
from .models import *

import pymssql
from itertools import chain
from datetime import timedelta, date
import datetime
from datetime import *
from django.http import HttpResponse
import csv
import json
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.clickjacking import xframe_options_exempt
from account.models import ErrorLog
# Create your views here.

from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

def error_404_view(request,exception):
    return render(request,'error_404_view.html')



@xframe_options_exempt
def load_rigs(request):
    saswellname_id = request.GET.get('saswellname')
    sasrignames = SasRigName.objects.filter(saswellname=saswellname_id).order_by('name')

    context = {'sasrignames': sasrignames}
    return render(request, 'mechanical\well-dropdown.html', context)



@xframe_options_exempt
def save_well(request):
    conn = pymssql.connect("192.168.18.137:1433", "web_user", "Hyd@1234", "Mother_Database")
    try:
        with conn.cursor() as cur:
            query1 = 'select distinct  wellid, rigid from Mother_Database.dbo.SAP_DPR_DRL_AQC group by wellid, rigid;'

            cur.execute(query1)
            rows = cur.fetchall()
            for i in rows:
                if SasWellName.objects.filter(name=i[0]).exists():
                    well = SasWellName.objects.get(name=i[0])
                    if SasRigName.objects.filter(saswellname=well, name=i[1]).exists() == False:
                        data = SasRigName(name=i[1])
                        data.save()
                        well.sasrigname_set.add(data)
                else:
                    well = SasWellName(name=i[0])
                    well.save()

                    data = SasRigName(name=i[1])
                    data.save()
                    well.sasrigname_set.add(data)
    finally:
        conn.close()

    return redirect('index')

@xframe_options_exempt
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def equipmentLog(request):
    try:
        print(request.session['receiver'])
        form = RigForm()
        form_hsd_formset = formset_factory(HsdForm)
        equip_formset = formset_factory(EquipmentForm)
        equip_serv_formset = formset_factory(EquipServiceForm)
        down_formset = formset_factory(RigDownForm)

        if request.method == 'POST':
            form = RigForm(request.POST)
            if form.is_valid():
                rig = form.save(commit=False)
                rig.user=request.user
                form.save()
                rig = Rig.objects.get(id=rig.id)
            else:
                messages.error(request, 'Rig details are not valid')

            form_hsd_formset_class = formset_factory(HsdForm, extra=request.POST.get('hsd_form-TOTAL_FORMS'))

            data_dict1 = request.POST.dict()
            data_dict1['form-TOTAL_FORMS'] = request.POST.get('hsd_form-TOTAL_FORMS')

            form_hsd_formset = form_hsd_formset_class(data_dict1)

            if form_hsd_formset.is_valid():
                for form in form_hsd_formset:
                    hsd_balance = form.save(commit=False)
                    hsd_balance.hsd_user=request.user
                    hsd_balance.rig = rig
                    form.save()
            else:
                messages.error(request, 'H.S.D. Balance details are not valid')

            equip_formset_class = formset_factory(EquipmentForm, extra=request.POST.get('equip_form-TOTAL_FORMS'))

            data_dict4 = request.POST.dict()
            data_dict4['form-TOTAL_FORMS'] = request.POST.get('hsd_form-TOTAL_FORMS')

            equip_formset = equip_formset_class(data_dict4)

            if equip_formset.is_valid():
                for form in equip_formset:
                    equipment = form.save(commit=False)
                    equipment.equip_user=request.user
                    equipment.rig = rig
                    form.save()
            else:
                messages.error(request, 'Equipment Log Sheet is not valid')

            equip_serv_formset_class = formset_factory(EquipServiceForm, extra=request.POST.get('equip_serv-TOTAL_FORMS'))
            data_dict2 = request.POST.dict()
            data_dict2['form-TOTAL_FORMS'] = request.POST.get('equip_serv-TOTAL_FORMS')

            equip_serv_formset = equip_serv_formset_class(data_dict2)

            if equip_serv_formset.is_valid():
                for form in equip_serv_formset:
                    service = form.save(commit=False)
                    service.service_user=request.user
                    service.rig = rig
                    form.save()
            else:
                messages.error(request, 'Repairing Log Sheet is not valid')

            down_formset_class = formset_factory(RigDownForm, extra=request.POST.get('rig_down-TOTAL_FORMS'))
            data_dict3 = request.POST.dict()
            data_dict3['form-TOTAL_FORMS'] = request.POST.get('rig_down-TOTAL_FORMS')

            down_formset = down_formset_class(data_dict3)

            if down_formset.is_valid():
                for form in down_formset:
                    rig_down = form.save(commit=False)
                    rig_down.rigdown_user=request.user
                    rig_down.rig = rig
                    form.save()
            else:
                messages.error(request, 'Rig Down Time is not valid')
            send_mail(
        'Equipment Form Details',
        'Hello Sir, An Equipment form has been submitted recently. Its details can be accessed through the link : https://commonanalytics.ongc.co.in/mechanical/view-equipment-log/'+str(rig.id)+'/',

        'gaurav@ongc.co.in',
        ['gaurav.jain@inspiraenterprise.com',request.session['receiver']],
        fail_silently=False,)

            return redirect('view-equipment-log', rig.id)

        context = {
            'form': form,
            'form_hsd_formset': form_hsd_formset,
            'equip_formset': equip_formset,
            'equip_serv_formset': equip_serv_formset,
            'down_formset': down_formset,
        }

        return render(request, 'mechanical/create-equipment-log.html', context)
    except Exception as e:
        error=ErrorLog(user_name=request.user, function_name='Equipment_Log',error_desc=str(e))
        error.save()
        send_mail(
    'Equipment_Log Error',
   'Hi,'+str(request.session['username'])+' received an error which is '+str(e),

    'gaurav@ongc.co.in',
    [settings.EMAILS,request.session['receiver']],
    fail_silently=False,)
        return redirect('mechanical.views.error_404_view.html')


@xframe_options_exempt
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def viewEquipmentLog(request, rig_id):
    try:
        rig = Rig.objects.select_related('equipment_singlehit', 'service_singlehit', 'rigdown_singlehit', 'hsdbalance_singlehit').get(pk=rig_id)
        equipments = rig.equipment_set.all()
        services = rig.equipmentservice_set.all()
        rigdowns = rig.rigdown_set.all()
        hsd_balances = rig.hsd_balance_set.all()

        context = {
            'rig': rig,
            'equipments': equipments,
            'services': services,
            'rigdowns': rigdowns,
            'hsd_balances': hsd_balances,
        }

        return render(request, 'mechanical/view-equipment-log.html', context)
    except Exception as e:
        error=ErrorLog(user_name=request.user, function_name='View_Equipment',error_desc=str(e))
        error.save()
        send_mail(
    'View_Equipment Error',
   'Hi,'+str(request.session['username'])+' received an error which is '+str(e),

    'gaurav@ongc.co.in',
    [settings.EMAILS,request.session['receiver']],
    fail_silently=False,)
        return redirect('mechanical.views.error_404_view.html')


@xframe_options_exempt
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def reportEquipmentLog(request):
    try:
        if request.method=="POST":
            fromdate=datetime.strptime(request.POST.get('From'),'%Y-%m-%d').date()
            todate=datetime.strptime(request.POST.get('To'),'%Y-%m-%d').date()

            def daterange(start, end):
                delta = end - start
                days = [start + timedelta(days=i) for i in range(delta.days + 1)]
                return days
            #daterange
            range1 = daterange(fromdate, todate)

            date__range=[fromdate,todate]
            print(date__range)
            rig1=equipments1 =hsdbalances1= services1=rigdowns1=Rig.objects.filter(date__range=['2021-11-10','2021-11-11']).all()

            for i in range(len(range1)):
                rig = Rig.objects.filter(user=request.user,today_rig=range1[i]).all()
                rig1=chain(rig1,rig)
                print(rig1)
                equipments = Equipment.objects.filter(equip_user=request.user,today_equip=range1[i]).all()
                equipments1=chain(equipments1,equipments)
                hsdbalances = HSD_balance.objects.filter(hsd_user=request.user,today_hsdbal=range1[i]).all()
                hsdbalances1=chain(hsdbalances1,hsdbalances)
                services = EquipmentService.objects.filter(service_user=request.user,today_equip_service=range1[i]).all()
                services1=chain(services1,services)
                rigdowns = RigDown.objects.filter(rigdown_user=request.user,today_rigdown=range1[i]).all()
                rigdowns1=chain(rigdowns1,rigdowns)
                #print(equipments,hsdbalances,services,rigdowns)

            rig=rig1
            equipments=equipments1
            hsdbalances=hsdbalances1
            services=services1
            rigdowns=rigdowns1

            context = {'rig': rig,
            'equipments': equipments,
            'services': services,
            'rigdowns': rigdowns,
            'hsdbalances':hsdbalances,
            'fromdate':fromdate,
            'todate':todate,
            }
            return render(request, 'mechanical/report-equipment.html', context)
        else:
            rig = Rig.objects.filter(user=request.user)
            equipments = Equipment.objects.filter(equip_user=request.user).all()
            hsdbalances = HSD_balance.objects.filter(hsd_user=request.user).all()
            services = EquipmentService.objects.filter(service_user=request.user).all()
            rigdowns = RigDown.objects.filter(rigdown_user=request.user).all()

            context = {
                'rig': rig,
                'equipments': equipments,
                'services': services,
                'rigdowns': rigdowns,
                'hsdbalances':hsdbalances,
            }
            return render(request, 'mechanical/report-equipment.html', context)
    except Exception as e:
        error=ErrorLog(user_name=request.user, function_name='reportEquipmentLog',error_desc=str(e))
        error.save()
        send_mail(
    'Report_Euipment_Log Error',
   'Hi,'+str(request.session['username'])+' received an error which is '+str(e),

    'gaurav@ongc.co.in',
    [settings.EMAILS,request.session['receiver']],
    fail_silently=False,)
        return redirect('mechanical.views.error_404_view.html')


@xframe_options_exempt
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def electricalLog(request):
    try:
        print(request.session['receiver'])
        form = ElectricalRigForm()
        electrical_shift_formset = formset_factory(ElectricalShiftForm)

        if request.method == 'POST':
            print(request.POST)
            print(request.POST.getlist('form-TOTAL_FORMS'))
            print(request.POST.get('electric_form-TOTAL_FORMS'))
            form = ElectricalRigForm(request.POST)
            if form.is_valid():
                rig = form.save(commit=False)
                rig.user_electric=request.user
                form.save()
            else:
                messages.error(request, 'Rig details are not valid')

            electrical_shift_formset_class = formset_factory(ElectricalShiftForm, extra=request.POST.get('electric_form-TOTAL_FORMS'))
            data_dict = request.POST.dict()
            data_dict['form-TOTAL_FORMS'] = request.POST.get('electric_form-TOTAL_FORMS')
            electrical_shift_formset = electrical_shift_formset_class(data_dict)

            if electrical_shift_formset.is_valid():
                for form in electrical_shift_formset:
                    eshift = form.save(commit=False)
                    eshift.electric_user=request.user
                    eshift.rig = rig
                    form.save()
            else:
               messages.error(request, 'Equipment details are not valid')
            send_mail(
        'Electrical Form Details',
        'Hello Sir, An Electrical form has been submitted recently. Its details can be accessed through the link : https://commonanalytics.ongc.co.in/mechanical/view-electric-log/'+str(rig.id)+'/',

        'gaurav@ongc.co.in',
        ['gaurav.jain@inspiraenterprise.com',request.session['receiver']],fail_silently=False,)

            return redirect('view-electric-log', rig.id)

        context = {
            'form': form,
            'electrical_shift_formset': electrical_shift_formset,

        }
        return render(request, 'mechanical/electric-log.html', context)
    except Exception as e:
        error=ErrorLog(user_name=request.user, function_name='Electrical_Log',error_desc=str(e))
        error.save()
        send_mail(
    'Electrical_Log Error',
   'Hi,'+str(request.session['username'])+' received an error which is '+str(e),

    'gaurav@ongc.co.in',
    [settings.EMAILS,request.session['receiver']],
    fail_silently=False,)
        return redirect('mechanical.views.error_404_view.html')


@xframe_options_exempt
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def viewElecticLog(request,rig_id):
    try:
        rig = ElectricalRig.objects.select_related('user_electric').get(pk=rig_id)
        electricalShifts = rig.electricalshift_set.all()

        context = {
            'rig': rig,
            'electricalShifts': electricalShifts,


        }

        return render(request, 'mechanical/view-electric-log.html', context)
    except Exception as e:
        error=ErrorLog(user_name=request.user, function_name='viewElecticLog',error_desc=str(e))
        error.save()
        send_mail(
    'View_Electric_log Error',
   'Hi,'+str(request.session['username'])+' received an error which is '+str(e),

    'gaurav@ongc.co.in',
    [settings.EMAILS,request.session['receiver']],
    fail_silently=False,)
        return redirect('mechanical.views.error_404_view.html')


@xframe_options_exempt
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def reportElectricalLog(request):
    try:
        if request.method=="POST":
            fromdate=datetime.strptime(request.POST.get('From_electric'),'%Y-%m-%d').date()
            todate=datetime.strptime(request.POST.get('To_electric'),'%Y-%m-%d').date()

            def daterange(start, end):
                delta = end - start
                days = [start + timedelta(days=i) for i in range(delta.days + 1)]
                return days
            #daterange
            range1 = daterange(fromdate, todate)

            date__range=[fromdate,todate]
            print(date__range)
            rig1=electric_s1 =ElectricalRig.objects.filter(date__range=['2021-11-10','2021-11-11']).all()

            for i in range(len(range1)):
                rig = ElectricalRig.objects.filter(user_electric=request.user,today_rig_electric=range1[i]).all()
                rig1=chain(rig1,rig)
                print(rig1)
                electric_s = ElectricalShift.objects.filter(electric_user=request.user,electric_today=range1[i]).all()
                electric_s1=chain(electric_s1,electric_s)


                #print(equipments,hsdbalances,services,rigdowns)

            rig=rig1
            electric_s=electric_s1


            context = {'rig': rig,
            'electric_s': electric_s,
            'fromdate':fromdate,
            'todate':todate,
            }
            return render(request, 'mechanical/report-electrical.html', context)
        else:
            rig = ElectricalRig.objects.filter(user_electric=request.user)
            electric_s = ElectricalShift.objects.filter(electric_user=request.user).all()

            context = {
                'rig': rig,
                'electric_s': electric_s,

            }
            return render(request, 'mechanical/report-electrical.html', context)
    except Exception as e:
        error=ErrorLog(user_name=request.user, function_name='Report_Equipment_Log',error_desc=str(e))
        error.save()
        send_mail(
    'Report_Equipment_Log Error',
   'Hi,'+str(request.session['username'])+' received an error which is '+str(e),

    'gaurav@ongc.co.in',
    [settings.EMAILS,request.session['receiver']],
    fail_silently=False,)
        return redirect('mechanical.views.error_404_view.html')


@xframe_options_exempt
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def drillLog(request):
    try:
        print(request.session['receiver'])
        form = DrillRigForm()

        drill_shift_formset = formset_factory(DrillShiftForm)
        drill_mud_chemical_formset= formset_factory(DrillMudChemicalReportForm)

        drill_laboratory_formset = formset_factory(DrillLaboratoryForm, extra=2)
        hydraulic_data_formset = formset_factory(HydraulicDataForm, extra=1)
        drill_data_formset = formset_factory(DrilldataForm, extra=2)
        drill_mud_volume_formset = formset_factory(DrillMudVolumeForm, extra=1)
        drill_solid_control_formset = formset_factory(DrillSolidControlForm, extra=1)

        if request.method == 'POST':
            form = DrillRigForm(request.POST)
            if form.is_valid():
                rig = form.save(commit=False)
                rig.user_drill=request.user
                form.save()
                rig = DrillRig.objects.get(id=rig.id)

            drill_shift_formset_class = formset_factory(DrillShiftForm, extra=request.POST.get('drill_shift_form-TOTAL_FORMS'))
            data_dict = request.POST.dict()
            data_dict['form-TOTAL_FORMS'] = request.POST.get('drill_shift_form-TOTAL_FORMS')
            drill_shift_formset = drill_shift_formset_class(data_dict)


            if drill_shift_formset.is_valid():
                for form in drill_shift_formset:
                    drillshift = form.save(commit=False)
                    drillshift.drill_shift_user=request.user
                    drillshift.rig = rig
                    form.save()

            data_dict2 = request.POST.dict()
            data_dict2['form-TOTAL_FORMS'] = 2

            drill_laboratory_formset = drill_laboratory_formset(data_dict2)
            if drill_laboratory_formset.is_valid():
                for form in drill_laboratory_formset:
                    drilllab = form.save(commit=False)
                    drilllab.drill_lab_user=request.user
                    drilllab.rig = rig
                    form.save()
            else:
               messages.error(request, 'drill_laboratory details are not valid')

            hydraulic_data_formset = hydraulic_data_formset(request.POST)
            if hydraulic_data_formset.is_valid():
                for form in hydraulic_data_formset:
                    hydraulicdata = form.save(commit=False)
                    hydraulicdata.hyd_data_user=request.user
                    hydraulicdata.rig = rig
                    form.save()


            data_dict3 = request.POST.dict()
            data_dict3['form-TOTAL_FORMS'] = 2

            drill_data_formset = drill_data_formset(data_dict3)
            if drill_data_formset.is_valid():
                for form in drill_data_formset:
                    drilldata = form.save(commit=False)
                    drilldata.drill_data_user=request.user
                    drilldata.rig = rig
                    form.save()


            drill_mud_chemical_formset_class = formset_factory(DrillMudChemicalReportForm, extra=request.POST.get('drill_mud_chemical_form-TOTAL_FORMS'))
            data_dict1 = request.POST.dict()
            data_dict1['form-TOTAL_FORMS'] = request.POST.get('drill_mud_chemical_form-TOTAL_FORMS')
            drill_mud_chemical_formset = drill_mud_chemical_formset_class(data_dict1)

            if drill_mud_chemical_formset.is_valid():
                for form in drill_mud_chemical_formset:
                    drillmud = form.save(commit=False)
                    drillmud.drill_mud_user=request.user
                    drillmud.rig = rig
                    form.save()

            drill_mud_volume_formset  = drill_mud_volume_formset(request.POST)
            if drill_mud_volume_formset.is_valid():
                for form in drill_mud_volume_formset:
                    drillmudvolume = form.save(commit=False)
                    drillmudvolume.drill_vol_user=request.user
                    drillmudvolume.rig = rig
                    form.save()

            drill_solid_control_formset = drill_solid_control_formset(request.POST)
            if drill_solid_control_formset.is_valid():
                for form in drill_solid_control_formset:
                    drillsolid = form.save(commit=False)
                    drillsolid.drill_solid_user=request.user
                    drillsolid.rig = rig
                    form.save()
            send_mail(
        'Drilling Form Details',
        'Hello Sir, A Drilling form has been submitted recently. Its details can be accessed through the link : https://commonanalytics.ongc.co.in/mechanical/view-drill-log/'+str(rig.id)+'/',
        'gaurav@ongc.co.in',
        ['gaurav.jain@inspiraenterprise.com',request.session['receiver']],
        fail_silently=False,)


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
    except Exception as e:
        error=ErrorLog(user_name=request.user, function_name='Drill_Log',error_desc=str(e))
        error.save()
        send_mail(
    'Drill_Log Error',
   'Hi,'+str(request.session['username'])+' received an error which is '+str(e),

    'gaurav@ongc.co.in',
    [settings.EMAILS,request.session['receiver']],
    fail_silently=False,)
        return redirect('mechanical.views.error_404_view.html')


@xframe_options_exempt
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def viewDrillLog(request, rig_id):
    try:
        rig = DrillRig.objects.get(id=rig_id)
        drillshifts = DrillShift.objects.filter(rig_id=rig_id).all()
        drilllaboratorys = DrillLaboratory.objects.filter(rig_id=rig_id).all()
        hydraulicdatas = HydraulicData.objects.filter(rig_id=rig_id).all()
        drilldatas = Drilldata.objects.filter(rig_id=rig_id).all()
        drillchemicals = DrillMudChemicalReport.objects.filter(rig_id=rig_id).all()
        drillvolumes = DrillMudVolume.objects.filter(rig_id=rig_id).all()
        drillsolids = DrillSolidControl.objects.filter(rig_id=rig_id).all()

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
    except Exception as e:
        error=ErrorLog(user_name=request.user, function_name='View_Drill_Log',error_desc=str(e))
        error.save()
        send_mail(
    'View_Drill_Log Error',
   'Hi,'+str(request.session['username'])+' received an error which is '+str(e),

    'gaurav@ongc.co.in',
    [settings.EMAILS,request.session['receiver']],
    fail_silently=False,)
        return redirect('mechanical.views.error_404_view.html')


@xframe_options_exempt
@login_required(login_url='login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def reportDrillLog(request):
    try:

        if request.method=="POST":



                fromdate=datetime.strptime(request.POST.get('From_drill'),'%Y-%m-%d').date()
                todate=datetime.strptime(request.POST.get('To_drill'),'%Y-%m-%d').date()
                print(fromdate)
                print(todate)
                def daterange(start, end):
                    delta = end - start
                    days = [start + timedelta(days=i) for i in range(delta.days + 1)]
                    return days
                #daterange
                range1 = daterange(fromdate, todate)

                date__range=[fromdate,todate]
                print(date__range)
                rig1=drillshift1 =drilllaboratory1= hydraulic1=drilldata1=drillmud1=drillvol1=drillsolid1=DrillRig.objects.filter(date__range=['2021-11-10','2021-11-11']).all()

                for i in range(len(range1)):
                    rig = DrillRig.objects.filter(user_drill=request.user,today_rig_drill=range1[i]).all()
                    rig1=chain(rig1,rig)
                    print(rig1)
                    drillshift = DrillShift.objects.filter(drill_shift_user=request.user,drill_shift_equip=range1[i]).all()
                    drillshift1=chain(drillshift1,drillshift)
                    drilllaboratory = DrillLaboratory.objects.filter(drill_lab_user=request.user,drill_lab_service=range1[i]).all()
                    drilllaboratory1=chain(drilllaboratory1,drilllaboratory)
                    hydraulic = HydraulicData.objects.filter(hyd_data_user=request.user,hyd_data_rigdown=range1[i]).all()
                    hydraulic1=chain(hydraulic1,hydraulic)
                    drilldata = Drilldata.objects.filter(drill_data_user=request.user,drill_data_hsdbal=range1[i]).all()
                    drilldata1=chain(drilldata1,drilldata)
                    drillmud = DrillMudChemicalReport.objects.filter(drill_mud_user=request.user,drill_mud_hsdbal=range1[i]).all()
                    drillmud1=chain(drillmud1,drillmud)
                    drillvol = DrillMudVolume.objects.filter(drill_vol_user=request.user,drill_vol_hsdbal=range1[i]).all()
                    drillvol1=chain(drillvol1,drillvol)
                    drillsolid = DrillSolidControl.objects.filter(drill_solid_user=request.user,drill_solid_hsdbal=range1[i]).all()
                    drillsolid1=chain(drillsolid1,drillsolid)
                    #print(equipments,hsdbalances,services,rigdowns)

                rig=rig1
                drillshift=drillshift1
                drilllaboratory=drilllaboratory1
                hydraulic=hydraulic1
                drilldata=drilldata1
                drillmud=drillmud1
                drillvol=drillvol1
                drillsolid=drillsolid1
                context = {'rig': rig,
                'drillshift': drillshift,
                'drilllaboratory': drilllaboratory,
                'hydraulic':hydraulic,
                'drilldata': drilldata,
                'drillmud':drillmud,
                'drillvol':drillvol,
                'drillsolid':drillsolid,

                'fromdate':fromdate,
                'todate':todate,
                }
                return render(request, 'mechanical/report-drill.html', context)

        else:
            rig = DrillRig.objects.filter(user_drill=request.user).all()
            drillshift = DrillShift.objects.filter(drill_shift_user=request.user).all()
            drilllaboratory = DrillLaboratory.objects.filter(drill_lab_user=request.user).all()
            hydraulic = HydraulicData.objects.filter(hyd_data_user=request.user).all()
            drilldata = Drilldata.objects.filter(drill_data_user=request.user).all()
            drillmud = DrillMudChemicalReport.objects.filter(drill_mud_user=request.user).all()
            drillvol = DrillMudVolume.objects.filter(drill_vol_user=request.user).all()
            drillsolid = DrillSolidControl.objects.filter(drill_solid_user=request.user).all()
            context = {
                'rig': rig,
                'drillshift': drillshift,
                'drilllaboratory': drilllaboratory,
                'hydraulic':hydraulic,
                'drilldata':drilldata,
                'drillmud':drillmud,
                'drillvol':drillvol,
                'drillsolid':drillsolid


            }
            return render(request, 'mechanical/report-drill.html', context)
    except Exception as e:
        error=ErrorLog(user_name=request.user, function_name='Report_Drill_Log',error_desc=str(e))
        error.save()
        send_mail(
    'Report_Drill_Log Error',
   'Hi,'+str(request.session['username'])+' received an error which is '+str(e),

    'gaurav@ongc.co.in',
    [settings.EMAILS,request.session['receiver']],
    fail_silently=False,)
        return redirect('mechanical.views.error_404_view.html')


