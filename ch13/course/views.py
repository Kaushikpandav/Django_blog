from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def leanrn_django(request):
    return render(request, 'course/django.html')

def learn_fastapi(request):
    return render(request, 'course/fastapi.html')