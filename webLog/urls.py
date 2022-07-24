from django.urls import path
from . import views

urlpatterns = [
    path('create-DLIS/', views.createDlis, name='create-DLIS'),
    path('create-LAS/', views.createLas, name='create-LAS'),
    path('view-LAS/<str:logcolumn_name>/', views.viewLas, name='view-LAS-image'),
]