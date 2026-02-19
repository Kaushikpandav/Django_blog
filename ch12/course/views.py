from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# filter
def leanrn_django(request):
    context = {
        "name":'Django for Beginners',
        "desc":'earn jango ith Greeky Shows'
    }

    return render(request, 'course/django.html', context=context, status=200, using=None)


# datetime
# def learn_fastapi(request):
#     d = datetime.now()
#     context = {
#         'version': '0.68.0',
#         'name': 'FastAPI for Beginners',
#         'dt': d
#     }
#     return render(request, 'course/fastapi.html', context=context, status=200, using=None)


# float_formate
# def learn_fastapi(request):
#     context = {
#         'p1': 2.00000,
#         'p2': 232.00032,
#         'p3': 1234.56789
#     }
#     return render(request, 'course/fastapi.html', context=context, status=200, using=None)

# # if
# def learn_fastapi(request):
#     context = {
#         'p1': True,
#         'p2': False,
#         'p3': True
#     }
#     return render(request, 'course/fastapi.html', context=context, status=200, using=None)

# # for loop
# def learn_fastapi(request):
#     context = {
#         'p1': ['Python', 'Django', 'FastAPI' ],
#         'p2': False,
#         'p3': True
#     }
#     return render(request, 'course/fastapi.html', context=context, status=200, using=None)

# for loop
def learn_fastapi(request):
    context = {
        'st1': {
            'name': 'John Doe',
            'age': 25,
            'course': 'Python'
        },
        'st2': {
            'name': 'Jane Smith',
            'age': 30,
            'course': 'Django'
        },
        'st3': {
            'name': 'Alice Johnson',
            'age': 28,
            'course': 'FastAPI'
        }
    }

    hard = {"student_1" : context}
    return render(request, 'course/fastapi.html', context=hard, status=200, using=None)