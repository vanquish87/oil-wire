from django.db import models
from mechanical.equip_list import EQUIP_NAME
from django.core.validators import MaxValueValidator
from mechanical.models.sas_db import SasWellName, SasRigName
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Rig(models.Model):
	SHIFTS = (
		('Day Shift', 'Shift-I'),
		('Night Shift', 'Shift-II'),
	)

	sasrigname=models.ForeignKey(SasRigName,on_delete=models.CASCADE)
	saswellname=models.ForeignKey(SasWellName,on_delete=models.CASCADE)
	
	equipment_singlehit = models.ForeignKey('Equipment', null=True, blank=True, on_delete=models.SET_NULL, related_name='equipment_singlehit')
	service_singlehit = models.ForeignKey('EquipmentService', null=True, blank=True, on_delete=models.SET_NULL, related_name='service_singlehit')
	rigdown_singlehit = models.ForeignKey('RigDown', null=True, blank=True, on_delete=models.SET_NULL, related_name='rigdown_singlehit')
	hsdbalance_singlehit = models.ForeignKey('HSD_balance', null=True, blank=True, on_delete=models.SET_NULL, related_name='hsdbalance_singlehit')

	shift = models.CharField(max_length=50, choices=SHIFTS, default='Day Shift', null=False, blank=False)
	date = models.DateTimeField(null=True, blank=True,default=timezone.now)
	requirements = models.TextField(null=False, blank=False)
	mech_engineer = models.TextField(null=False,blank=False)
	
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	daterig = models.DateTimeField(default=timezone.now)
	today_rig = models.DateField(default=timezone.now)

	def __str__(self):
		return self.sasrigname.name


class Equipment(models.Model):
	equip_name = models.CharField(max_length=255, choices=EQUIP_NAME, null=True,blank=True )
	water_temp = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
	oil_temp = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False )
	oil_pressure = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	equip_working_hour = models.PositiveIntegerField(default=0, null=True, blank=True, validators=[MaxValueValidator(24)])
	equip_avail_hour = models.PositiveIntegerField(default=0, null=True, blank=True, validators=[MaxValueValidator(24)])
	equip_oil_used = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	oil_grade = models.CharField(max_length=255, null=True, blank=False)
	oil_level = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	
	equip_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	equip_date = models.DateTimeField(default=timezone.now)
	today_equip = models.DateField(default=timezone.now)
	# many to one relationship
	rig = models.ForeignKey(Rig, null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.rig.sasrigname.name


class EquipmentService(models.Model):
	equip_serv_name = models.CharField(max_length=255, choices=EQUIP_NAME, null=True, blank=True)
	working_hour = models.PositiveIntegerField(default=0, null=True, blank=True, validators=[MaxValueValidator(24)])
	avail_hour = models.PositiveIntegerField(default=0, null=True, blank=True, validators=[MaxValueValidator(24)])
	oil_used = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
	intstructions = models.TextField(null=False, blank=False)
	
	service_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	service_date = models.DateTimeField(default=timezone.now)
	today_equip_service = models.DateField(default=timezone.now)
	# many to one relationship
	rig = models.ForeignKey(Rig, null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.rig.sasrigname.name


class RigDown(models.Model):
	from_hr = models.TimeField(null=True, blank=True)
	to_hr = models.TimeField(null=True, blank=True)
	
	rigdown_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	rigdown_date = models.DateTimeField(default=timezone.now)
	today_rigdown = models.DateField(default=timezone.now)
	# many to one relationship
	rig = models.ForeignKey(Rig, null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.rig.sasrigname.name


class HSD_balance(models.Model):
	TANKS = (
		('tank1', 'Tank 1'),
		('tank2', 'Tank 2'),
	)
	
	tank = models.CharField(max_length=50, choices=TANKS, default='tank1', null=True, blank=True)
	
	opening = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
	consumption = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
	received = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	closing_bal = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)


	hsd_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	hsd_date = models.DateTimeField(default=timezone.now)
	today_hsdbal = models.DateField(default=timezone.now)

	# many to one relationship
	rig = models.ForeignKey(Rig, null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.rig.sasrigname.name
