from django.shortcuts import render
from .models import student



def index(request):
  st = student.students.all()
  st = student.objects.passout()
  return render(request, 'index.html', {'st': st})
