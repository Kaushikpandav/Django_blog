from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def my_view2(request):
  return HttpResponse('Hhome  dsds')

def about2(request):
  return HttpResponse('about dsdd')
