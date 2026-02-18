from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


def my_view(request):
  return HttpResponse('Hello, world!')

def my_viewfdf(request):
  data ={
    "name": "John",
    "age": 30
  }
  return JsonResponse(data)

def my_view(request):
  x = 20+212
  return HttpResponse(x)

def my_view(request):
  x = '<h1>hello</h1>'
  return HttpResponse(x)

def my_viewfdcsdcf(request):
  return render(request, "index.html")
