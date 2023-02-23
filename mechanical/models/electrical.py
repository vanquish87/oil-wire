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

	location = models.CharField(max_length=255, null=False, blank=False)
	date = models.DateTimeField(null=True, blank=True, default=timezone.now)
	doc_no= models.CharField(max_length=255, null=False, blank=False)

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

	rig = models.ForeignKey(ElectricalRig, null=True, blank=True, on_delete=models.SET_NULL)
	shifttype = models.CharField(max_length=50, choices=SHIFTS, default='Day Shift', null=False, blank=False)

	equipdetails= models.CharField(max_length=255, choices=ELECTRIC_EQUIP_NAME, null=True, blank=True)
	equipstatus = models.CharField(max_length=50, choices=STATUS, default='OK')

	runninghours_prev = models.PositiveIntegerField(default=0, null=False, blank=False)
	runninghours = models.PositiveIntegerField(default=0, null=False, blank=False, validators=[MaxValueValidator(24)])

	breakfrom = models.TimeField(null=True, blank=True)
	breakto = models.TimeField(null=True, blank=True)

	totalcummulative = models.PositiveIntegerField(default=0, null=False, blank=False)

	remarks = models.TextField(null=False, blank=False)
	equipment = models.TextField(null=False, blank=False)
	job = models.TextField(null=False, blank=False)

	energydg1 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	energydg2 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	energydg3 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	energydg4 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	safetyreport = models.TextField(null=False, blank=False)

	electric_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	electric_date = models.DateTimeField(default=timezone.now)
	electric_today = models.DateField(default=timezone.now)
	def __str__(self):
		return self.rig.sasrigname.name
