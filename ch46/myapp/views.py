from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student
from django.shortcuts import redirect

# Create your views here.
class StudentCreateView(CreateView):
  model = Student
  fields = ['name', 'email', 'roll', 'city']
  template_name = 'create.html'
  # success_url = '/student_success/'

  def get_success_url(self):
    return reverse('student_success')


class StudentSuccessView(ListView):
  model = Student
  template_name = 'success.html'
  context_object_name = 'data'

  # if we want to change queryset
  # def get_queryset(self):
  #   return Student.objects.all()


class StudentDetailView(DetailView):
  model = Student
  template_name = 'details.html'
  context_object_name = 'data'

  # def get_queryset(self):
  #     return Student.objects.all()

class StudentUpdateView(UpdateView):
  model = Student
  fields = ['name', 'email', 'roll', 'city']
  template_name = 'update.html' # not need of templates
  context_object_name = 'data'

  def get_success_url(self):
    return reverse('student_success')

class StudentDeleteView(DeleteView):
  model = Student
  template_name = 'delete.html'
  context_object_name = 'data'

  def get_success_url(self):
    return reverse('student_success')