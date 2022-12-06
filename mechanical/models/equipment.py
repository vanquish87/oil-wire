from django.db import models
from mechanical.equip_list import EQUIP_NAME
from django.core.validators import MaxValueValidator
from mechanical.models.sas_db import SasWellName, SasRigName


# Create your models here.
class Rig(models.Model):
	SHIFTS = (
		('Day Shift', 'Shift-I'),
		('Night Shift', 'Shift-II'),
	)

	sasrigname=models.ForeignKey(SasRigName,on_delete=models.CASCADE)
	saswellname=models.ForeignKey(SasWellName,on_delete=models.CASCADE)

	shift = models.CharField(max_length=50, choices=SHIFTS, default='Day', null=True, blank=True)
	date = models.DateTimeField(null=True, blank=True)
	requirements = models.TextField(null=True, blank=True)
	mech_engineer = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.sasrigname.name


class Equipment(models.Model):
	equip_name = models.CharField(max_length=255, choices=EQUIP_NAME, null=True, blank=True)
	water_temp = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	oil_temp = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	oil_pressure = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	equip_working_hour = models.PositiveIntegerField(default=0, null=True, blank=True, validators=[MaxValueValidator(24)])
	equip_avail_hour = models.PositiveIntegerField(default=0, null=True, blank=True, validators=[MaxValueValidator(24)])
	equip_oil_used = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	oil_grade = models.CharField(max_length=255, null=True, blank=False)
	oil_level = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	# many to one relationship
	rig = models.ForeignKey(Rig, null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.rig.sasrigname.name


class EquipmentService(models.Model):
	equip_serv_name = models.CharField(max_length=255, choices=EQUIP_NAME, null=True, blank=True)
	working_hour = models.PositiveIntegerField(default=0, null=True, blank=True, validators=[MaxValueValidator(24)])
	avail_hour = models.PositiveIntegerField(default=0, null=True, blank=True, validators=[MaxValueValidator(24)])
	oil_used = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	intstructions = models.TextField(null=True, blank=True)
	# many to one relationship
	rig = models.ForeignKey(Rig, null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.rig.sasrigname.name


class RigDown(models.Model):
	from_hr = models.TimeField(null=True, blank=True)
	to_hr = models.TimeField(null=True, blank=True)
	# many to one relationship
	rig = models.ForeignKey(Rig, null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.rig.sasrigname.name


class HSD_balance(models.Model):
	tank1 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	tank2 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	# many to one relationship
	rig = models.ForeignKey(Rig, null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.rig.sasrigname.name
