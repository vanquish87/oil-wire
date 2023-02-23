from django.db import models
from mechanical.equip_list import ELECTRIC_EQUIP_NAME
from django.core.validators import MaxValueValidator
from mechanical.models.sas_db import SasWellName, SasRigName
from django.conf import settings
from django.utils import timezone

#ELECTRICAL DAILY LOG SHEET
class ElectricalRig(models.Model):
	# null=True: db can have null value, blank:True, it can be left blank in form

	sasrigname=models.ForeignKey(SasRigName,on_delete=models.CASCADE)
	saswellname=models.ForeignKey(SasWellName,on_delete=models.CASCADE)

	location = models.CharField(max_length=255, null=True, blank=False)
	date = models.DateTimeField(null=True, blank=True)
	doc_no= models.CharField(max_length=255, null=True, blank=False)

	user_electric = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	daterig_electric = models.DateTimeField(default=timezone.now)
	today_rig_electric = models.DateField(default=timezone.now)
	def __str__(self):
		return self.sasrigname.name


class ElectricalShift(models.Model):
	SHIFTS = (
		('Day Shift', 'First Shift'),
		('Night Shift', 'Second Shift'),
	)

	STATUS = (
		('OK', 'OK'),
		('NOT OK', 'NOT OK'),
	)

	DG_UNIT = (
		('kWh', 'kWH'),
		('Wh', 'Wh'),
	)

	rig = models.ForeignKey(ElectricalRig, null=True, blank=True, on_delete=models.SET_NULL)
	shifttype = models.CharField(max_length=50, choices=SHIFTS, default='Day Shift', null=True, blank=True)

	equipdetails= models.CharField(max_length=255, choices=ELECTRIC_EQUIP_NAME, null=True, blank=True)
	equipstatus = models.CharField(max_length=50, choices=STATUS, default='OK')

	runninghours_prev = models.PositiveIntegerField(default=0, null=True, blank=True)
	runninghours = models.PositiveIntegerField(default=0, null=True, blank=True, validators=[MaxValueValidator(24)])

	breakfrom = models.TimeField(null=True, blank=True)
	breakto = models.TimeField(null=True, blank=True)

	totalcummulative = models.PositiveIntegerField(default=0, null=True, blank=True)

	remarks = models.TextField(null=True, blank=True)
	equipment = models.TextField(null=True, blank=True)
	job = models.TextField(null=True, blank=True)

	energydg1 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	dg1_unit = models.CharField(max_length=50, choices=DG_UNIT, default='kWh')

	energydg2 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	dg2_unit = models.CharField(max_length=50, choices=DG_UNIT, default='kWh')

	energydg3 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	dg3_unit = models.CharField(max_length=50, choices=DG_UNIT, default='kWh')

	energydg4 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	dg4_unit = models.CharField(max_length=50, choices=DG_UNIT, default='kWh')

	safetyreport = models.TextField(null=True, blank=True)

	electric_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	electric_date = models.DateTimeField(default=timezone.now)
	electric_today = models.DateField(default=timezone.now)
	def __str__(self):
		return self.rig.sasrigname.name