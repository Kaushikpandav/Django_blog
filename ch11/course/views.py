from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def leanrn_django(request):

    couirse_name = 'Django for Beginners'
    return render(request, 'course/django.html', context={'course_name': couirse_name}, content_type='text/html', status=200, using=None)

def learn_fastapi(request):
    context = {
        'version': '0.68.0',
        'name': 'FastAPI for Beginners'
    }
    return render(request, 'course/fastapi.html', context=context, content_type='text/html', status=200, using=None)
