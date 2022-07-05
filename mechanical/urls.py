from django.urls import path
from . import views

urlpatterns = [
    path('equipment-log/', views.equipmentLog, name='equipment-log'),
]