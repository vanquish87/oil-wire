from django.urls import path
from . import views

urlpatterns = [
    path('equipment-log/', views.equipmentLog, name='equipment-log'),
    path('view-equipment-log/<int:rig_id>/', views.viewEquipmentLog, name='view-equipment-log'),
    path('electrical-log/', views.electricalLog, name='electrical-log'),
    path('drill-log/', views.drillLog, name='drill-log'),
]