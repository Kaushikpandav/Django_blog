from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('register/', register, name='register'),
  path('login/<int:uuid>/token/<str:token>/', activate, name='activate'),
  path('login/', login_view, name='login'),
  path('password_reset_confirm/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
  path('logout/', LogoutView.as_view(), name='logout'),
]
