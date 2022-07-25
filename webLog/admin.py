from django.contrib import admin
from .models import LogFile, LogColumn, Frame

# Register your models here.
class LogColumnAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'frame',
        'logfile'
        )

admin.site.register(LogFile)
admin.site.register(LogColumn, LogColumnAdmin)
admin.site.register(Frame)