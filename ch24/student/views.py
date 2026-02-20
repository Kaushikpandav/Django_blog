from django.shortcuts import render
from .models import profile
# Create your views here.


def all_data(request):
    data = profile.objects.all()
    print(f"Data: {list(data)}")
    return render(request, 'students/all_data.html', {'data': data})


def single_data(request):
    student = profile.objects.get(pk=1)
    # student = profile.objects.get(id=1)
    # student = profile.objects.get(name="akash")
    print(f"Data: {student}")
    return render(request, 'students/single.html', {'data': student})