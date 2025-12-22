from django.shortcuts import render
from django.http import JsonResponse
from students.models import students



def studentsView(request):
    # return HttpResponse("Students View")
    students = students.objects.all()
    print(students)
    return JsonResponse(students)