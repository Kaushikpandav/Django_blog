from django.urls import path, include
from . import views

urlpatterns = [
    path('all/', views.all_data, name='all_data'),
    path('single/', views.single_data, name='single_data'),
]