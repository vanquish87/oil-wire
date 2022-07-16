from django.db import models

# Create your models here.
class LogFile(models.Model):
    file = models.FileField(upload_to ='science/')


class LogColumn(models.Model):
    # many to one relationship
    logfile = models.ForeignKey(LogFile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)