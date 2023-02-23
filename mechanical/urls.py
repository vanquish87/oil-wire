from django.urls import path
from . import views
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('equipment-log/', views.equipmentLog, name='equipment-log'),
    path('view-equipment-log/<int:rig_id>/', views.viewEquipmentLog, name='view-equipment-log'),
    path('report-equipment', views.reportEquipmentLog, name='report-equipment'),
    #path('datereportequipment', views.datereportequipment, name='datewise-report-equipment'),
    
    path('view-electric-log/<int:rig_id>/', views.viewElecticLog, name='view-electric-log'),
    path('report-electrical', views.reportElectricalLog, name='report-electrical'),
    path('electrical-log/', views.electricalLog, name='electrical-log'),
    
    path('drill-log/', views.drillLog, name='drill-log'),
    path('view-drill-log/<int:rig_id>/', views.viewDrillLog, name='view-drill-log'),
    path('report-drill', views.reportDrillLog, name='report-drill'),
    path('ajax/load-rigs/', views.load_rigs, name='load-rigs'),
    path('save-well/', views.save_well, name='save-well'),
]
