from django.urls import path
from .views import home, user, math
urlpatterns = [
    path('home/', home, name='homepage'),
    path('user/', user, name='userpage'),
    path('math/', math, name='mathpage'),
]
