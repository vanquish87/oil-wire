from django.db import models

# Create your models here.
class Log(models.Model):
    file = models.FileField(upload_to ='science/')