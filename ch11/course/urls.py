from django.contrib import admin
from django.urls import path
from course.views import leanrn_django, learn_fastapi

urlpatterns = [
    path('django/', leanrn_django, name='learn-django'),
    path('fastapi/', learn_fastapi, name='learn-fastapi'),
]