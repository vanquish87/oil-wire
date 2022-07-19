from django.db import models

# Create your models here.
class Book(models.Model):

    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name


class Rig(models.Model):
    SHIFTS = (
        ('Day', 'Day Shift'),
        ('Night', 'Night Shift'),
    )
    # null=True: db can have null value, blank:True, it can be left blank in form
    name = models.CharField(max_length=50, null=True, blank=True)
    well = models.CharField(max_length=50, null=True, blank=True)
    shift = models.CharField(max_length=50, choices=SHIFTS, blank=False, default='Day')
    slug = models.CharField(max_length=255, unique=True, default=0)
    date = models.DateTimeField()


    def __str__(self):
        return self.name



class Equipment(models.Model):
    EQUIP_NAME = (
        ('Carrier Engine - 1', 'Carrier Engine - 1'),
        ('Carrier Engine - 2', 'Carrier Engine - 2'),
        ('MP Engine - 1', 'MP Engine - 1'),
        ('MP Engine - 2', 'MP Engine - 2'),
        ('DG SET Engine - 1', 'DG SET Engine - 1'),
        ('DG SET Engine - 2', 'DG SET Engine - 2'),
        ('DG SET Engine - 3', 'DG SET Engine - 3'),
        ('DG SET Engine - 4', 'DG SET Engine - 4'),
        ('Transmission CE - 1', 'Transmission CE - 1'),
        ('Transmission CE - 2', 'Transmission CE - 2'),
        ('Compresser (Elect.) - 1', 'Compresser (Elect.) - 1'),
        ('Compresser (Elect.) - 2', 'Compresser (Elect.) - 2'),
        ('Compresser (Mech.) - 1', 'Compresser (Mech.) - 1'),
        ('Compresser (Mech.) - 2', 'Compresser (Mech.) - 2'),
        ('Diesel Engine Comp.(Mech.) - 1', 'Compresser(Mech.) - 2'),
        ('Diesel Engine Comp.(Mech.) - 2', 'Diesel Engine Comp.(Mech.) - 2'),
        ('Mud Pump - 1', 'Mud Pump - 1'),
        ('Mud Pump - 2', 'Mud Pump - 2'),
        ('Torque Converter MP1', 'Torque Converter MP1'),
        ('Torque Converter MP1', 'Torque Converter MP1'),
        ('Fire Water Pump', 'Fire Water Pump'),
    )

    name = models.CharField(max_length=255, choices=EQUIP_NAME, blank=False)
    water_temp = models.DecimalField(max_digits=5, decimal_places=2)
    oil_temp = models.DecimalField(max_digits=5, decimal_places=2)
    oil_pressure = models.DecimalField(max_digits=7, decimal_places=2)
    working_hour = models.DateTimeField()
    equi_avail_hour = models.DateTimeField()
    oil_used = models.DecimalField(max_digits=7, decimal_places=2)
    # many to one relationship
    rig = models.ForeignKey(Rig, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class EquipmentService(models.Model):
    EQUIP_NAME = (
        ('Power Take - Off - 1', 'Power Take - Off - 1'),
        ('Power Take - Off - 2', 'Power Take - Off - 2'),
        ('Draw Works', 'Draw Works'),
        ('Rotary / Bevel Gear Box', 'Rotary / Bevel Gear Box'),
        ('C/B T/B - Hook', 'C/B T/B - Hook'),
        ('Swivel', 'Swivel'),
        ('Shale Shaker Bucket - 1', 'Shale Shaker Bucket - 1'),
        ('Shale Shaker Bucket - 2', 'Shale Shaker Bucket - 2'),
        ('R/T /Rotary Elevator Drive', 'R/T /Rotary Elevator Drive'),
        ('Hydromatic Brake', 'Hydromatic Brake'),
        ('Super Charger - 1', 'Super Charger - 1'),
        ('Super Charger - 2', 'Super Charger - 2'),
        ('Hopper Pump - 1', 'Hopper Pump - 1'),
        ('Hopper Pump - 2', 'Hopper Pump - 2'),
        ('Degasser', 'Degasser'),
        ('Desander', 'Desander'),
        ('Mud Cleaner', 'Mud Cleaner'),
        ('Desander Pump', 'Desander Pump'),
        ('Desilter Pump', 'Desilter Pump'),
        ('Ezy Torque', 'Ezy Torque'),
        ('Pipe Spinner', 'Pipe Spinner'),
        ('Kelly Spinner', 'Kelly Spinner'),
        ('Main Water Pump', 'Main Water Pump'),
        ('Second Water Pump', 'Second Water Pump'),
        ('Air Winch', 'Air Winch'),
        ('Mud Agitator - 1', 'Mud Agitator - 1'),
        ('Mud Agitator - 2', 'Mud Agitator - 2'),
        ('Mud Agitator - 3', 'Mud Agitator - 3'),
        ('Mud Agitator - 4', 'Mud Agitator - 4'),
        ('Mud Agitator - 5', 'Mud Agitator - 5'),
        ('Mud Agitator - 6', 'Mud Agitator - 6'),
        ('Mud Agitator - 7', 'Mud Agitator - 7'),
        ('Mud Agitator - 8', 'Mud Agitator - 8'),
        ('Mud Agitator - 9', 'Mud Agitator - 9'),
        ('Mud Agitator - 10', 'Mud Agitator - 10'),
        ('Mud Agitator - 11', 'Mud Agitator - 11'),
        ('Mud Agitator - 12', 'Mud Agitator - 12'),
    )


    name = models.CharField(max_length=255, choices=EQUIP_NAME, blank=False)
    working_hour = models.DateTimeField()
    equi_avail_hour = models.DateTimeField()
    oil_used = models.DecimalField(max_digits=7, decimal_places=2)
    intstructions = models.TextField(null=True, blank=True)
    rig_downtime_from = models.DateTimeField()
    rig_downtime_to = models.DateTimeField()
    requirements = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name