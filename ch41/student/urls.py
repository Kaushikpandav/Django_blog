from django.urls import path
from .views import setsession, getsession, deletesession, flushsession, sessionmethodsinview, sessionmethodsintemplate, clearsession, settestcookie, checktestcookie, deltestcookie


urlpatterns = [
  # path('set/', setcookie, name='setcookie'),
  # path('get/', getcookie, name='getcookie'),
  # path('del/', deletecookie, name='deletecookie'),
  # path('setsigned/', setsignedcookie, name='setsignedcookie'),
  # path('getsigned/', getsignedcookie, name='getsignedcookie'),

  path('set/', setsession, name='setsession'),
  path('get/', getsession, name='getsession'),
  path('del/', deletesession, name='deletesession'),
  path('flush/', flushsession, name='flushsession'),
  path('inview/', sessionmethodsinview, name='inview'),
  path('intemplate/', sessionmethodsintemplate, name='intemplate'),
  path('clear/', clearsession, name='clearsession'),
  path('settest/', settestcookie, name='settestsession'),
  path('checktest/', checktestcookie, name='checktestsession'),
  path('deltest/', deltestcookie, name='deltestsession'),


]
