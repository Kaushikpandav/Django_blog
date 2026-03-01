
from django.urls import path, include
from .views import register
urlpatterns = [

    # base api
    path('register/', register.as_view(), name='register'),
]
