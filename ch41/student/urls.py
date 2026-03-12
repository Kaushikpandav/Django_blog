from django.urls import path
from .views import setsession, getsession, deletesession, flushsession, sessionmethodsinview, sessionmethodsintemplate, clearsession, settestcookie, checktestcookie, deltestcookie
from django.views.decorators.cache import cache_page

urlpatterns = [
  # path('set/', setcookie, name='setcookie'),
  # path('get/', getcookie, name='getcookie'),
  # path('del/', deletecookie, name='deletecookie'),
  # path('setsigned/', setsignedcookie, name='setsignedcookie'),
  # path('getsigned/', getsignedcookie, name='getsignedcookie'),

  path('set/', setsession, name='setsession'),
  path('setss/', cache_page(60)(setsession), name='setsession'),
  path('setcc/', setsession, name='setsession'),

  path('get/', getsession, name='getsession'),
  path('del/', cache_page(60)(deletesession), name='deletesession'),
  path('flush/', flushsession, name='flushsession'),
  path('inview/', sessionmethodsinview, name='inview'),
  path('intemplate/', sessionmethodsintemplate, name='intemplate'),
  path('clear/', clearsession, name='clearsession'),
  path('settest/', settestcookie, name='settestsession'),
  path('checktest/', checktestcookie, name='checktestsession'),
  path('deltest/', deltestcookie, name='deltestsession'),


]
