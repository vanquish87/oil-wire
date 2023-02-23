from django.db import models
import uuid, os


# Create your models here.
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('science/', filename)


class LogFile(models.Model):
    file = models.FileField(upload_to=get_file_path)


class Frame(models.Model):
    # many to one relationship
    logfile = models.ForeignKey(LogFile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class LogColumn(models.Model):
    # many to one relationship
    logfile = models.ForeignKey(LogFile, null=True, blank=True, on_delete=models.CASCADE)
    frame = models.ForeignKey(Frame, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name