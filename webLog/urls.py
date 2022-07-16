from django.urls import path
from . import views

urlpatterns = [
    path('view-DLIS/', views.viewDlis, name='view-DLIS'),
    path('create-LAS/', views.createLas, name='create-LAS'),
    path('view-LAS/<str:logcolumn_name>/', views.viewLas, name='view-LAS-image'),
]