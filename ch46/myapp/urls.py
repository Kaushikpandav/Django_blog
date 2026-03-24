from django.urls import path
from . import views

urlpatterns = [
  path('create/', views.StudentCreateView.as_view(), name='student_create'),
  path('list/', views.StudentSuccessView.as_view(), name='student_success'),
  path('detail/<int:pk>/', views.StudentDetailView.as_view(), name='student_details'),
  path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),
  path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
]