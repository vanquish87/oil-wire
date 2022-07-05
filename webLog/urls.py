from django.urls import path
from . import views

urlpatterns = [
    path('view-DLIS/', views.viewDlis, name='view-DLIS'),
]