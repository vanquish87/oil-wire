# Generated by Django 4.0.6 on 2022-07-20 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mechanical', '0003_rig_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='rig',
            name='mech_engineer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rig',
            name='requirements',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rig',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rig',
            name='shift',
            field=models.CharField(blank=True, choices=[('Day', 'First Shift'), ('Night', 'Second Shift')], default='Day', max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='RigDown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_hr', models.DateTimeField(blank=True, null=True)),
                ('to_hr', models.DateTimeField(blank=True, null=True)),
                ('rig', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mechanical.rig')),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('Carrier Engine - 1', 'Carrier Engine - 1'), ('Carrier Engine - 2', 'Carrier Engine - 2'), ('MP Engine - 1', 'MP Engine - 1'), ('MP Engine - 2', 'MP Engine - 2'), ('DG SET Engine - 1', 'DG SET Engine - 1'), ('DG SET Engine - 2', 'DG SET Engine - 2'), ('DG SET Engine - 3', 'DG SET Engine - 3'), ('DG SET Engine - 4', 'DG SET Engine - 4'), ('Transmission CE - 1', 'Transmission CE - 1'), ('Transmission CE - 2', 'Transmission CE - 2'), ('Compresser (Elect.) - 1', 'Compresser (Elect.) - 1'), ('Compresser (Elect.) - 2', 'Compresser (Elect.) - 2'), ('Compresser (Mech.) - 1', 'Compresser (Mech.) - 1'), ('Compresser (Mech.) - 2', 'Compresser (Mech.) - 2'), ('Diesel Engine Comp.(Mech.) - 1', 'Compresser(Mech.) - 2'), ('Diesel Engine Comp.(Mech.) - 2', 'Diesel Engine Comp.(Mech.) - 2'), ('Mud Pump - 1', 'Mud Pump - 1'), ('Mud Pump - 2', 'Mud Pump - 2'), ('Torque Converter MP1', 'Torque Converter MP1'), ('Torque Converter MP1', 'Torque Converter MP1'), ('Fire Water Pump', 'Fire Water Pump'), ('Power Take - Off - 1', 'Power Take - Off - 1'), ('Power Take - Off - 2', 'Power Take - Off - 2'), ('Draw Works', 'Draw Works'), ('Rotary / Bevel Gear Box', 'Rotary / Bevel Gear Box'), ('C/B T/B - Hook', 'C/B T/B - Hook'), ('Swivel', 'Swivel'), ('Shale Shaker Bucket - 1', 'Shale Shaker Bucket - 1'), ('Shale Shaker Bucket - 2', 'Shale Shaker Bucket - 2'), ('R/T /Rotary Elevator Drive', 'R/T /Rotary Elevator Drive'), ('Hydromatic Brake', 'Hydromatic Brake'), ('Super Charger - 1', 'Super Charger - 1'), ('Super Charger - 2', 'Super Charger - 2'), ('Hopper Pump - 1', 'Hopper Pump - 1'), ('Hopper Pump - 2', 'Hopper Pump - 2'), ('Degasser', 'Degasser'), ('Desander', 'Desander'), ('Mud Cleaner', 'Mud Cleaner'), ('Desander Pump', 'Desander Pump'), ('Desilter Pump', 'Desilter Pump'), ('Ezy Torque', 'Ezy Torque'), ('Pipe Spinner', 'Pipe Spinner'), ('Kelly Spinner', 'Kelly Spinner'), ('Main Water Pump', 'Main Water Pump'), ('Second Water Pump', 'Second Water Pump'), ('Air Winch', 'Air Winch'), ('Mud Agitator - 1', 'Mud Agitator - 1'), ('Mud Agitator - 2', 'Mud Agitator - 2'), ('Mud Agitator - 3', 'Mud Agitator - 3'), ('Mud Agitator - 4', 'Mud Agitator - 4'), ('Mud Agitator - 5', 'Mud Agitator - 5'), ('Mud Agitator - 6', 'Mud Agitator - 6'), ('Mud Agitator - 7', 'Mud Agitator - 7'), ('Mud Agitator - 8', 'Mud Agitator - 8'), ('Mud Agitator - 9', 'Mud Agitator - 9'), ('Mud Agitator - 10', 'Mud Agitator - 10'), ('Mud Agitator - 11', 'Mud Agitator - 11'), ('Mud Agitator - 12', 'Mud Agitator - 12')], max_length=255, null=True)),
                ('working_hour', models.DateTimeField(blank=True, null=True)),
                ('equi_avail_hour', models.DateTimeField(blank=True, null=True)),
                ('oil_used', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('intstructions', models.TextField(blank=True, null=True)),
                ('rig', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mechanical.rig')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('Carrier Engine - 1', 'Carrier Engine - 1'), ('Carrier Engine - 2', 'Carrier Engine - 2'), ('MP Engine - 1', 'MP Engine - 1'), ('MP Engine - 2', 'MP Engine - 2'), ('DG SET Engine - 1', 'DG SET Engine - 1'), ('DG SET Engine - 2', 'DG SET Engine - 2'), ('DG SET Engine - 3', 'DG SET Engine - 3'), ('DG SET Engine - 4', 'DG SET Engine - 4'), ('Transmission CE - 1', 'Transmission CE - 1'), ('Transmission CE - 2', 'Transmission CE - 2'), ('Compresser (Elect.) - 1', 'Compresser (Elect.) - 1'), ('Compresser (Elect.) - 2', 'Compresser (Elect.) - 2'), ('Compresser (Mech.) - 1', 'Compresser (Mech.) - 1'), ('Compresser (Mech.) - 2', 'Compresser (Mech.) - 2'), ('Diesel Engine Comp.(Mech.) - 1', 'Compresser(Mech.) - 2'), ('Diesel Engine Comp.(Mech.) - 2', 'Diesel Engine Comp.(Mech.) - 2'), ('Mud Pump - 1', 'Mud Pump - 1'), ('Mud Pump - 2', 'Mud Pump - 2'), ('Torque Converter MP1', 'Torque Converter MP1'), ('Torque Converter MP1', 'Torque Converter MP1'), ('Fire Water Pump', 'Fire Water Pump'), ('Power Take - Off - 1', 'Power Take - Off - 1'), ('Power Take - Off - 2', 'Power Take - Off - 2'), ('Draw Works', 'Draw Works'), ('Rotary / Bevel Gear Box', 'Rotary / Bevel Gear Box'), ('C/B T/B - Hook', 'C/B T/B - Hook'), ('Swivel', 'Swivel'), ('Shale Shaker Bucket - 1', 'Shale Shaker Bucket - 1'), ('Shale Shaker Bucket - 2', 'Shale Shaker Bucket - 2'), ('R/T /Rotary Elevator Drive', 'R/T /Rotary Elevator Drive'), ('Hydromatic Brake', 'Hydromatic Brake'), ('Super Charger - 1', 'Super Charger - 1'), ('Super Charger - 2', 'Super Charger - 2'), ('Hopper Pump - 1', 'Hopper Pump - 1'), ('Hopper Pump - 2', 'Hopper Pump - 2'), ('Degasser', 'Degasser'), ('Desander', 'Desander'), ('Mud Cleaner', 'Mud Cleaner'), ('Desander Pump', 'Desander Pump'), ('Desilter Pump', 'Desilter Pump'), ('Ezy Torque', 'Ezy Torque'), ('Pipe Spinner', 'Pipe Spinner'), ('Kelly Spinner', 'Kelly Spinner'), ('Main Water Pump', 'Main Water Pump'), ('Second Water Pump', 'Second Water Pump'), ('Air Winch', 'Air Winch'), ('Mud Agitator - 1', 'Mud Agitator - 1'), ('Mud Agitator - 2', 'Mud Agitator - 2'), ('Mud Agitator - 3', 'Mud Agitator - 3'), ('Mud Agitator - 4', 'Mud Agitator - 4'), ('Mud Agitator - 5', 'Mud Agitator - 5'), ('Mud Agitator - 6', 'Mud Agitator - 6'), ('Mud Agitator - 7', 'Mud Agitator - 7'), ('Mud Agitator - 8', 'Mud Agitator - 8'), ('Mud Agitator - 9', 'Mud Agitator - 9'), ('Mud Agitator - 10', 'Mud Agitator - 10'), ('Mud Agitator - 11', 'Mud Agitator - 11'), ('Mud Agitator - 12', 'Mud Agitator - 12')], max_length=255, null=True)),
                ('water_temp', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('oil_temp', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('oil_pressure', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('working_hour', models.DateTimeField(blank=True, null=True)),
                ('equi_avail_hour', models.DateTimeField(blank=True, null=True)),
                ('oil_used', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('rig', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mechanical.rig')),
            ],
        ),
    ]
