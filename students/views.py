from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def student(request):
    student = [{
        'name': 'John',
        'age': 25,
        'city': 'New York'
    }]
    return HttpResponse(student)