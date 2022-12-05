from django.contrib import admin
from django.http import HttpResponse
import csv, datetime
from mechanical.models import *


# Register your models here.
def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;' 'filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)

    return response

export_to_csv.short_description = 'Export to CSV'  #short description


class CsvAdmin(admin.ModelAdmin):
    actions = [export_to_csv] 


admin.site.register(Rig, CsvAdmin)
admin.site.register(Equipment, CsvAdmin)
admin.site.register(EquipmentService, CsvAdmin)
admin.site.register(RigDown, CsvAdmin)

admin.site.register(DrillRig, CsvAdmin)
admin.site.register(DrillShift, CsvAdmin)
admin.site.register(DrillLaboratory, CsvAdmin)
admin.site.register(HydraulicData, CsvAdmin)
admin.site.register(DrillMudChemicalReport, CsvAdmin)
admin.site.register(DrillMudVolume, CsvAdmin)
admin.site.register(DrillSolidControl, CsvAdmin)

admin.site.register(Drilldata, CsvAdmin)
admin.site.register(ElectricalRig, CsvAdmin)
admin.site.register(ElectricalShift, CsvAdmin)

