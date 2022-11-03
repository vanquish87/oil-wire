from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class Upload(models.Model):
	pdf = models.FileField(null=False,
						blank=True,
						validators=[FileExtensionValidator( ['pdf'] ) ], upload_to ='ocr/')
