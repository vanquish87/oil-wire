from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='upload'),
    path('view-pdf/<str:ocrfilepath>/', views.pdfView, name='view-pdf'),
]