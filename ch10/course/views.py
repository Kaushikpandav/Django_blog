from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def leanrn_django(request):
    return render(request, 'course/django.html', context={'course_name': 'Django for Beginners'}, content_type='text/html', status=200, using=None)

def learn_fastapi(request):
    return render(request, 'course/fastapi.html', context={'course_name': 'FastAPI for Beginners'}, content_type='text/html', status=200, using=None)
