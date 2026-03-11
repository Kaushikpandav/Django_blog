from django.urls import path
from .views import *


urlpatterns = [
  path('set/', setcookie, name='setcookie'),
  path('get/', getcookie, name='getcookie'),
  path('del/', deletecookie, name='deletecookie'),
  path('setsigned/', setsignedcookie, name='setsignedcookie'),
  path('getsigned/', getsignedcookie, name='getsignedcookie'),
]
