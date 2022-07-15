from django.urls import path
from . import views

urlpatterns = [
    path('equipment-log/', views.equipmentLog, name='equipment-log'),
    path('electrical-log/', views.electricalLog, name='electrical-log'),
]