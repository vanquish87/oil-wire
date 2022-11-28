from django.db import models
from mechanical.equip_list import EQUIP_NAME


# Create your models here.
class Rig(models.Model):
	SHIFTS = (
		('Day Shift', 'Shift-I'),
		('Night Shift', 'Shift-II'),
	)
	# null=True: db can have null value, blank:True, it can be left blank in form
	rig_name = models.CharField(max_length=255, null=True, blank=False)
	well = models.CharField(max_length=255, null=True, blank=True)
	shift = models.CharField(max_length=50, choices=SHIFTS, default='Day', null=True, blank=True)
	date = models.DateTimeField(null=True, blank=True)
	requirements = models.TextField(null=True, blank=True)
	mech_engineer = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.rig_name


class Equipment(models.Model):
	equip_name = models.CharField(max_length=255, choices=EQUIP_NAME, null=True, blank=True)
	water_temp = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	oil_temp = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	oil_pressure = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	equip_working_hour = models.TimeField(null=True, blank=True)
	equip_avail_hour = models.TimeField(null=True, blank=True)
	equip_oil_used = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	# many to one relationship
	rig = models.ForeignKey(Rig, null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.rig.rig_name


class EquipmentService(models.Model):
	equip_serv_name = models.CharField(max_length=255, choices=EQUIP_NAME, null=True, blank=True)
	working_hour = models.TimeField(null=True, blank=True)
	avail_hour = models.TimeField(null=True, blank=True)
	oil_used = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	intstructions = models.TextField(null=True, blank=True)
	# many to one relationship
	rig = models.ForeignKey(Rig, null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.rig.rig_name


class RigDown(models.Model):
	from_hr = models.TimeField(null=True, blank=True)
	to_hr = models.TimeField(null=True, blank=True)
	# many to one relationship
	rig = models.ForeignKey(Rig, null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.rig.rig_name
