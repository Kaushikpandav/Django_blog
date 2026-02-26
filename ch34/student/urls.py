
from django.urls import path, include
from .views import register
urlpatterns = [
    path('student/', register, name='register'),
]
