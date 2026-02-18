from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def my_view(request):
  return HttpResponse('Hhome')

def about(request):
  return HttpResponse('about')
