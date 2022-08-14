from django.urls import path
from . import views

urlpatterns = [
    path('equipment-log/', views.equipmentLog, name='equipment-log'),
    path('view-equipment-log/<int:rig_id>/', views.viewEquipmentLog, name='view-equipment-log'),
    path('view-drill-log/<int:rig_id>/', views.viewDrillLog, name='view-drill-log'),
    path('view-electric-log/<int:rig_id>/', views.viewElecticLog, name='view-electric-log'),
    path('electrical-log/', views.electricalLog, name='electrical-log'),
    path('drill-log/', views.drillLog, name='drill-log'),
]