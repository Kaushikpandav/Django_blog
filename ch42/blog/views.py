from django.shortcuts import render
from .signals import notification
# Create your views here.


def index(request):
  notification.send(sender=index, request=request, user = [1,2,3])
  return render(request, 'blog/index.html')
