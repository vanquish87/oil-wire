from django.db import models


class SasWellName(models.Model):
	name = models.CharField(max_length=255, null=True, blank=False)

	def __str__(self):
		return self.name


class SasRigName(models.Model):
	name = models.CharField(max_length=255, null=True, blank=False)
	saswellname = models.ManyToManyField(SasWellName)

	def __str__(self):
			return self.name