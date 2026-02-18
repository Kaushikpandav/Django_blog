from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def learn(req,):
  return HttpResponse(f"<h1>fbed jbdcvjn lj with status:</h1>")

def learn(req, **kwargs):
  status = kwargs.get('status')
  print(f"status: {status}")
  return HttpResponse(f"<h1>fbed jbdcvjn lj with status: {status}</h1>")