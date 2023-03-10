# Generated by Django 3.2.8 on 2023-01-02 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mechanical', '0002_auto_20221226_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drillrig',
            name='shifttype',
        ),
        migrations.RemoveField(
            model_name='electricalrig',
            name='electrical_shift',
        ),
        migrations.RemoveField(
            model_name='electricalrig',
            name='shifttype',
        ),
        migrations.AddField(
            model_name='drilldata',
            name='drill_data_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='drilldata',
            name='drill_data_hsdbal',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='drilldata',
            name='drill_data_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='drilllaboratory',
            name='drill_lab_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='drilllaboratory',
            name='drill_lab_service',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='drilllaboratory',
            name='drill_lab_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='drillmudchemicalreport',
            name='drill_mud_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='drillmudchemicalreport',
            name='drill_mud_hsdbal',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='drillmudchemicalreport',
            name='drill_mud_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='drillmudvolume',
            name='drill_vol_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='drillmudvolume',
            name='drill_vol_hsdbal',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='drillmudvolume',
            name='drill_vol_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='drillrig',
            name='daterig_drill',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='drillrig',
            name='today_rig_drill',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='drillrig',
            name='user_drill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='drillshift',
            name='drill_shift_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='drillshift',
            name='drill_shift_equip',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='drillshift',
            name='drill_shift_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='drillshift',
            name='shifttype',
            field=models.CharField(blank=True, choices=[('Day Shift', 'First Shift'), ('Night Shift', 'Second Shift')], default='Day Shift', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='drillsolidcontrol',
            name='drill_solid_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='drillsolidcontrol',
            name='drill_solid_hsdbal',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='drillsolidcontrol',
            name='drill_solid_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='electricalrig',
            name='daterig_electric',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='electricalrig',
            name='today_rig_electric',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='electricalrig',
            name='user_electric',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='electricalshift',
            name='dg1_unit',
            field=models.CharField(choices=[('kWh', 'kWH'), ('Wh', 'Wh')], default='kWh', max_length=50),
        ),
        migrations.AddField(
            model_name='electricalshift',
            name='dg2_unit',
            field=models.CharField(choices=[('kWh', 'kWH'), ('Wh', 'Wh')], default='kWh', max_length=50),
        ),
        migrations.AddField(
            model_name='electricalshift',
            name='dg3_unit',
            field=models.CharField(choices=[('kWh', 'kWH'), ('Wh', 'Wh')], default='kWh', max_length=50),
        ),
        migrations.AddField(
            model_name='electricalshift',
            name='dg4_unit',
            field=models.CharField(choices=[('kWh', 'kWH'), ('Wh', 'Wh')], default='kWh', max_length=50),
        ),
        migrations.AddField(
            model_name='electricalshift',
            name='electric_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='electricalshift',
            name='electric_today',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='electricalshift',
            name='electric_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='electricalshift',
            name='shifttype',
            field=models.CharField(choices=[('Day Shift', 'First Shift'), ('Night Shift', 'Second Shift')], default='Day Shift', max_length=50),
        ),
        migrations.AddField(
            model_name='hydraulicdata',
            name='hyd_data_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='hydraulicdata',
            name='hyd_data_rigdown',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='hydraulicdata',
            name='hyd_data_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
