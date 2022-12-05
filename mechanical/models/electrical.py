from django.db import models
from mechanical.equip_list import ELECTRIC_EQUIP_NAME
from django.core.validators import MaxValueValidator


#ELECTRICAL DAILY LOG SHEET
class ElectricalRig(models.Model):
	# null=True: db can have null value, blank:True, it can be left blank in form
	rig_name = models.CharField(max_length=255, null=True, blank=False)
	well = models.CharField(max_length=255, null=True, blank=True)
	location = models.CharField(max_length=255, null=True, blank=False)
	date = models.DateTimeField(null=True, blank=True)
	doc_no= models.CharField(max_length=255, null=True, blank=False)
   

	def __str__(self):
		return self.rig_name
	

class ElectricalShift(models.Model):
	SHIFTS = (
		('Day Shift', 'First Shift'),
		('Night Shift', 'Second Shift'),
	)

	STATUS = (
		('OK', 'OK'),
		('NOT OK', 'NOT OK'),
	)

	rig = models.ForeignKey(ElectricalRig, null=True, blank=True, on_delete=models.SET_NULL)
	shifttype = models.CharField(max_length=50, choices=SHIFTS, default='Day', null=True, blank=True)

	equipdetails= models.CharField(max_length=255, choices=ELECTRIC_EQUIP_NAME, null=True, blank=True)
	equipstatus = models.CharField(max_length=50, choices=STATUS, default='OK', null=True, blank=True)

	runninghours_prev = models.PositiveIntegerField(default=0, null=True, blank=True) 
	runninghours = models.PositiveIntegerField(default=0, null=True, blank=True, validators=[MaxValueValidator(24)])

	breakfrom = models.TimeField(null=True, blank=True)
	breakto = models.TimeField(null=True, blank=True)
	
	totalcummulative = models.PositiveIntegerField(default=0, null=True, blank=True)

	remarks = models.TextField(null=True, blank=True)
	equipment = models.TextField(null=True, blank=True)
	job = models.TextField(null=True, blank=True)

	energydg1 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	energydg2 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	energydg3 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	energydg4 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	safetyreport = models.TextField(null=True, blank=True)
	
	def __str__(self):
		return self.rig.rig_name