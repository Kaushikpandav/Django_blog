from django.urls import path
from .converter import restrrictions
from django.urls import register_converter
# register_converter(restrrictions, 'restrrictions')

from .views import home, about , profile

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('profile/<pk>/', profile, name='profile'), # deafult is string
    path('profile/<int:pk>/', profile, name='profile'),
    path('profile/<slug:pk>/', profile, name='profile'), #'title-could-be-slug'
    path('profile/<str:pk>/', profile, name='profile'), #'title-could-be-string'
    path('profile/<uuid:pk>/<str:profile_id>/', profile, name='profile'), #'title-could-be-uuid'
    # path('profile/<restrrictions:pk>/', profile, name='profile'), #'title-could-be-regex'
]