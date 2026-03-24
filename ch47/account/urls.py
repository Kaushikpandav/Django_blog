from django.urls import path
from .views import *
from .view import register, login_view, activate, password_reset_confirm
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('register/', register.as_view(), name='register'),
  path('login/', login_view, name='login'),
  path('activate/<str:uidb64>/<str:token>/', activate.as_view(), name='activate'),
  # it redirect in admin to avoid add this in Settigs.py
  # LOGOUT_REDIRECT_URL = 'login',
  path('logout/', LogoutView.as_view(), name='logout'),

  path('password_reset_confirm/<uidb64>/<token>/', password_reset_confirm.as_view(), name='password_reset_confirm'),

]
