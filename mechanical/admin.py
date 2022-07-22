from django.contrib import admin
from mechanical.models import Equipment, EquipmentService, Rig, RigDown


# Register your models here.
admin.site.register(Rig)
admin.site.register(Equipment)
admin.site.register(EquipmentService)
admin.site.register(RigDown)
