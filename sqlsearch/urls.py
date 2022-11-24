from django.urls import path
from . import views

urlpatterns = [
    path('sqlsearch/dp/<str:search_query>/', views.sql_search_dp, name='sqlsearch-dp'),
    path('sqlsearch/dp/other/<str:search_query>/', views.sql_search_dp_other, name='sqlsearch-dp-other'),
    path('sqlsearch/nob/<str:search_query>/', views.sql_search_nob, name='sqlsearch-nob'),
    path('sqlsearch/nob/other/<str:search_query>/', views.sql_search_nob_other, name='sqlsearch-nob-other'),
]