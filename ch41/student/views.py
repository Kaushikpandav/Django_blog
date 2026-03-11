import datetime

from django.shortcuts import render

# Create your views here.


def setcookie(request):
  response = render(request, 'student/setcookie.html')
  response.set_cookie('name', 'Django')
  # response.set_cookie('token', '123456', max_age=3600)
  # response.set_cookie('name', 'Django', expires=datetime.now() + datetime.timedelta(days=1))
  return response

def getcookie(request):
  cookie_name = request.COOKIES['name']
  cookie_token = request.COOKIES['token']

  total = {
    'name': cookie_name,
    'token': cookie_token
  }

  return render(request, 'student/getcookie.html', total)

def deletecookie(request):
  response = render(request, 'student/deletecookie.html')
  response.delete_cookie('name')
  return response

def setsignedcookie(request):
  response = render(request, 'student/setsignedcookie.html')
  response.set_signed_cookie('name', 'Django', salt='secret')
  return response

def getsignedcookie(request):
  name = request.get_signed_cookie('name', salt='secret', default='Guest')
  return render(request, 'student/getsignedcookie.html', {'name': name})