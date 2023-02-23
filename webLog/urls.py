from django.urls import path
from . import views

urlpatterns = [
    path('create-DLIS/', views.createDlis, name='create-DLIS'),
    path('create-LAS/', views.createLas, name='create-LAS'),
    path('view-LAS/<str:logcolumn_name>/<path:unique_filename>/', views.viewLas, name='view-LAS-image'),
    path(
        'view-DLIS/<int:logfile_id>/<int:frame_id>/<str:logcolumn_name>/',
        views.viewDLIS,
        name='view-DLIS-image'
        ),
]