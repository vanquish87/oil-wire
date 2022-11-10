from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='upload'),
    path('view-pdf/<path:ocrfilepath>/', views.pdfView, name='pdfView'),
    path('viewer/<path:ocrfilepath>/', views.viewer, name='viewer'),
]