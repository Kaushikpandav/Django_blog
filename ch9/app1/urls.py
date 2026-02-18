from django.urls import path
from app1.views import learn
urlpatterns = [
    path("/", learn, name="learn"),
    path('learn/', learn, {'status': 'active'})
]
