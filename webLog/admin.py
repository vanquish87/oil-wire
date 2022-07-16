from django.contrib import admin
from .models import LogFile, LogColumn

# Register your models here.
admin.site.register(LogFile)
admin.site.register(LogColumn)