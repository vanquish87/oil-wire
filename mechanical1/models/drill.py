from django.db import models
from mechanical.models.sas_db import SasWellName, SasRigName
from django.conf import settings
from django.utils import timezone
#Drilling Mud Report
class DrillRig(models.Model):
	SHIFTS = (
		('Day Shift', 'First Shift'),
		('Night Shift', 'Second Shift'),
	)
	shifttype = models.CharField(max_length=50, choices=SHIFTS, default='Day Shift', null=True, blank=True)
	
	sasrigname=models.ForeignKey(SasRigName,on_delete=models.CASCADE)
	saswellname=models.ForeignKey(SasWellName,on_delete=models.CASCADE)

	asset = models.CharField(max_length=255, null=True, blank=False)
	date = models.DateTimeField(null=True, blank=True)

	user_drill = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	daterig_drill = models.DateTimeField(default=timezone.now)
	today_rig_drill = models.DateField(default=timezone.now)

	def __str__(self):
		return self.sasrigname.name

class DrillShift(models.Model):
	# null=True: db can have null value, blank:True, it can be left blank in form
	drillfrom= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	drillto = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	timefrom = models.TimeField(null=True, blank=True)
	timeto = models.TimeField(null=True, blank=True)
	operation = models.TextField(null=True, blank=True)
	spgrade= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	visc= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	gel= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	ph= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	rig = models.ForeignKey(DrillRig, null=True, blank=True, on_delete=models.SET_NULL)

	drill_shift_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	drill_shift_date = models.DateTimeField(default=timezone.now)
	drill_shift_equip = models.DateField(default=timezone.now)
	def __str__(self):
		return self.rig.sasrigname.name

class DrillLaboratory(models.Model):
	SAMPLE = (
		('Sample-I', 'Sample-I'),
		('Sample-II', 'Sample-II'),
	)
	sample = models.CharField(max_length=50, choices=SAMPLE, default='Sample-I', null=True, blank=True)

	time= models.TimeField(null=True, blank=True)
	depth = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	apifilter = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	cakethickness = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	ph = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	sand = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	apparentvisc = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	plasticvisc = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	yieldpoint = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	gelzero = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	gelten = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	oilcontent = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	solidcontent = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	watercontent = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	mbc = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	filtersalinity = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	flowlinetemp = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	rig = models.ForeignKey(DrillRig, null=True, blank=True, on_delete=models.SET_NULL)

	drill_lab_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	drill_lab_date = models.DateTimeField(default=timezone.now)
	drill_lab_service = models.DateField(default=timezone.now)
	def __str__(self):
		return self.rig.sasrigname.name


class HydraulicData(models.Model):
	pumplinersize = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	strokelength = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	discharge = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	stroke = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	standpipepressure = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	dpsize = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	dcsize = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	stabilizers = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	ohdc = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	ohdp = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	casdp = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	lastcasingsize = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	lastlength = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	csgvol = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	mudhole = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	sandtrap = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	pitvol = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	totalcirc = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	lagtime = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	cycletime = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	ECD = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	presslosses = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	rig = models.ForeignKey(DrillRig, null=True, blank=True, on_delete=models.SET_NULL)

	hyd_data_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	hyd_data_date = models.DateTimeField(default=timezone.now)
	hyd_data_rigdown = models.DateField(default=timezone.now)
	def __str__(self):
		return self.rig.sasrigname.name


class Drilldata(models.Model):
	SAMPLE = (
		('Sample-I', 'Sample-I'),
		('Sample-II', 'Sample-II'),
	)
	# null=True: db can have null value, blank:True, it can be left blank in form
	bitsize= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	jetsize= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	onbit= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	rotaryrpm= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	bhalengths= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	sample = models.CharField(max_length=50, choices=SAMPLE, default='Sample-I', null=True, blank=True)
	rig = models.ForeignKey(DrillRig, null=True, blank=True, on_delete=models.SET_NULL)
	drill_data_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	drill_data_date = models.DateTimeField(default=timezone.now)
	drill_data_hsdbal = models.DateField(default=timezone.now)
	def __str__(self):
		return self.rig.sasrigname.name


class DrillMudChemicalReport(models.Model):
	chemical=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	unit=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	opening= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	receipt= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	consumption= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	closing= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	total= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	rig = models.ForeignKey(DrillRig, null=True, blank=True, on_delete=models.SET_NULL)
	drill_mud_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	drill_mud_date = models.DateTimeField(default=timezone.now)
	drill_mud_hsdbal = models.DateField(default=timezone.now)
	def __str__(self):
		return self.rig.sasrigname.name


class DrillMudVolume(models.Model):

	shalevole= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	shalespgr=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	settingvole= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	settingspgr=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	intervole= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	interspgr=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	suctionvole= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	suctionspgr=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	tank1vole= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	tank1spgr=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	tank2vole= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	tank2spgr=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	rig = models.ForeignKey(DrillRig, null=True, blank=True, on_delete=models.SET_NULL)

	drill_vol_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	drill_vol_date = models.DateTimeField(default=timezone.now)
	drill_vol_hsdbal = models.DateField(default=timezone.now)
	def __str__(self):
		return self.rig.sasrigname.name


class DrillSolidControl(models.Model):

	shaleshaker= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	desander=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	desilter= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	degasser=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

	mudlcleaner= models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	remarks=models.TextField(null=True, blank=True)

	rig = models.ForeignKey(DrillRig, null=True, blank=True, on_delete=models.SET_NULL)

	drill_solid_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	drill_solid_date = models.DateTimeField(default=timezone.now)
	drill_solid_hsdbal = models.DateField(default=timezone.now)
	def __str__(self):
		return self.rig.sasrigname.name
