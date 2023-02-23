from django.db import models


class SasWellName(models.Model):
	name = models.CharField(max_length=255, null=True, blank=False)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class SasRigName(models.Model):
	name = models.CharField(max_length=255, null=True, blank=False)
	saswellname = models.ManyToManyField(SasWellName)

	def __str__(self):
			return self.name



# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# class SapDprDrlAqc(models.Model):
#     rigid = models.CharField(max_length=17, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     wellname = models.CharField(max_length=21, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     mlno = models.CharField(db_column='mlNo', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     summary2 = models.CharField(max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     summary3 = models.CharField(max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     summary4 = models.CharField(max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     reqdesc = models.CharField(max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     wellfluid = models.CharField(db_column='wellFluid', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     lithlogy = models.CharField(max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     objno = models.CharField(db_column='objNo', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     objname = models.CharField(db_column='objName', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     objint = models.CharField(db_column='objInt', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     btiadccd = models.CharField(db_column='btIadcCd', max_length=5, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     cname = models.CharField(max_length=12, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     cmddpr = models.CharField(db_column='cmdDpr', max_length=89, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     civilst = models.CharField(max_length=25, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     bittype = models.CharField(db_column='bitType', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     nextop = models.CharField(max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     aenam = models.CharField(max_length=12, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     wellid = models.CharField(max_length=16, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     expremark = models.CharField(max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     expremark1 = models.CharField(max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     nl1wellid = models.CharField(db_column='nl1Wellid', max_length=16, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     nl2wellid = models.CharField(db_column='nl2Wellid', max_length=16, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     nl1status = models.CharField(db_column='nl1Status', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     nl1remarks = models.CharField(db_column='nl1Remarks', max_length=7, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     nl2status = models.CharField(db_column='nl2Status', max_length=28, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     nl2remarks = models.CharField(db_column='nl2Remarks', max_length=80, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     mandt = models.CharField(max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     drlnr = models.CharField(max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     dprdt = models.CharField(db_column='dprDt', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     wellcat = models.CharField(db_column='wellCat', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     place = models.CharField(max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     pdepth = models.FloatField(db_column='pDepth', blank=True, null=True)  # Field name made lowercase.
#     dlymtr = models.FloatField(db_column='dlyMtr', blank=True, null=True)  # Field name made lowercase.
#     mudwt = models.FloatField(db_column='mudWt', blank=True, null=True)  # Field name made lowercase.
#     viscocity = models.FloatField(blank=True, null=True)
#     objstdt = models.CharField(db_column='objStDt', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     objendt = models.CharField(db_column='objEnDt', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     objstatus = models.CharField(db_column='objStatus', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     rigmode = models.CharField(db_column='rigMode', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     lotdepth = models.FloatField(db_column='lotDepth', blank=True, null=True)  # Field name made lowercase.
#     lotval = models.FloatField(db_column='lotVal', blank=True, null=True)  # Field name made lowercase.
#     compl = models.CharField(max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     compl1 = models.CharField(max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     amlmd = models.FloatField(db_column='amlMd', blank=True, null=True)  # Field name made lowercase.
#     amltvd = models.FloatField(db_column='amlTvd', blank=True, null=True)  # Field name made lowercase.
#     amlhd = models.FloatField(db_column='amlHd', blank=True, null=True)  # Field name made lowercase.
#     amldev = models.FloatField(db_column='amlDev', blank=True, null=True)  # Field name made lowercase.
#     amlaz = models.FloatField(db_column='amlAz', blank=True, null=True)  # Field name made lowercase.
#     btsize = models.FloatField(db_column='btSize', blank=True, null=True)  # Field name made lowercase.
#     btrothrs = models.FloatField(db_column='btRotHrs', blank=True, null=True)  # Field name made lowercase.
#     btmtrs = models.FloatField(db_column='btMtrs', blank=True, null=True)  # Field name made lowercase.
#     rechsd = models.FloatField(db_column='recHsd', blank=True, null=True)  # Field name made lowercase.
#     cnhsd = models.FloatField(db_column='cnHsd', blank=True, null=True)  # Field name made lowercase.
#     clhsd = models.FloatField(db_column='clHsd', blank=True, null=True)  # Field name made lowercase.
#     rectechwat = models.FloatField(db_column='recTechWat', blank=True, null=True)  # Field name made lowercase.
#     cntechwat = models.FloatField(db_column='cnTechWat', blank=True, null=True)  # Field name made lowercase.
#     cltechwat = models.FloatField(db_column='clTechWat', blank=True, null=True)  # Field name made lowercase.
#     recdrinkwat = models.FloatField(db_column='recDrinkWat', blank=True, null=True)  # Field name made lowercase.
#     cndrinkwat = models.FloatField(db_column='cnDrinkWat', blank=True, null=True)  # Field name made lowercase.
#     cldrinkwat = models.FloatField(db_column='clDrinkWat', blank=True, null=True)  # Field name made lowercase.
#     recbaryte = models.FloatField(db_column='recBaryte', blank=True, null=True)  # Field name made lowercase.
#     cnbaryte = models.FloatField(db_column='cnBaryte', blank=True, null=True)  # Field name made lowercase.
#     clbaryte = models.FloatField(db_column='clBaryte', blank=True, null=True)  # Field name made lowercase.
#     recbento = models.FloatField(db_column='recBento', blank=True, null=True)  # Field name made lowercase.
#     cnbento = models.FloatField(db_column='cnBento', blank=True, null=True)  # Field name made lowercase.
#     clbento = models.FloatField(db_column='clBento', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     summary1 = models.CharField(max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     cdate = models.CharField(max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     laeda = models.CharField(max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     lvorm = models.CharField(max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)
#     timestamp = models.FloatField(blank=True, null=True)
#     nl1wellcat = models.CharField(db_column='nl1Wellcat', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     nl1edc = models.CharField(db_column='nl1Edc', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     nl2wellcat = models.CharField(db_column='nl2Wellcat', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
#     nl2edc = models.CharField(db_column='nl2Edc', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         app_label = 'sas_db'
#         db_table = 'SAP_DPR_DRL_AQC'
		
#     def __str__(self):
#         return self.wellname
