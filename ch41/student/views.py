import datetime
from django.shortcuts import render
from django.views.decorators.cache import cache_page


#cookie

# def setcookie(request):
#   response = render(request, 'student/setcookie.html')
#   response.set_cookie('name', 'Django')
#   # response.set_cookie('token', '123456', max_age=3600)
#   # response.set_cookie('name', 'Django', expires=datetime.now() + datetime.timedelta(days=1))
#   return response

# def getcookie(request):
#   cookie_name = request.COOKIES['name']
#   cookie_token = request.COOKIES['token']

#   total = {
#     'name': cookie_name,
#     'token': cookie_token
#   }

#   return render(request, 'student/getcookie.html', total)

# def deletecookie(request):
#   response = render(request, 'student/deletecookie.html')
#   response.delete_cookie('name')
#   return response

# def setsignedcookie(request):
#   response = render(request, 'student/setsignedcookie.html')
#   response.set_signed_cookie('name', 'Django', salt='secret')
#   return response

# def getsignedcookie(request):
#   name = request.get_signed_cookie('name', salt='secret', default='Guest')
#   return render(request, 'student/getsignedcookie.html', {'name': name})ookie(request):
#   response = render(request, 'student/setcookie.html')
#   response.set_cookie('name', 'Django')
#   # response.set_cookie('token', '123456', max_age=3600)
#   # response.set_cookie('name', 'Django', expires=datetime.now() + datetime.timedelta(days=1))
#   return response

# def getcookie(request):
#   cookie_name = request.COOKIES['name']
#   cookie_token = request.COOKIES['token']

#   total = {
#     'name': cookie_name,
#     'token': cookie_token
#   }

#   return render(request, 'student/getcookie.html', total)

# def deletecookie(request):
#   response = render(request, 'student/deletecookie.html')
#   response.delete_cookie('name')
#   return response

# def setsignedcookie(request):
#   response = render(request, 'student/setsignedcookie.html')
#   response.set_signed_cookie('name', 'Django', salt='secret')
#   return response

# def getsignedcookie(request):
#   name = request.get_signed_cookie('name', salt='secret', default='Guest')
#   return render(request, 'student/getsignedcookie.html', {'name': name})




#session
# def setsession(request):
#   request.session['token'] = f'{datetime.datetime.now()}'
#   request.session['name'] = 'Django'
#   # request.session.set_expiry(60)
#   # request.session.set_expiry(0) # expiry at browser close

#   return render(request, 'student/setsession.html')

# def getsession(request):
#   token = request.session['token']
#   name = request.session['name']

#   ses = {
#     'token': token,
#     'name': name
#   }
#   return render(request, 'student/getsession.html', ses)

# def deletesession(request):
#   if 'name' in request.session:
#     del request.session['token']
#   # del request.session['name']
#   return render(request, 'student/deletesession.html')

# def flushsession(request):
#   request.session.flush()
#   return render(request, 'student/flushsession.html')

# def sessionmethodsinview(request):
#   keys = request.session.keys()
#   print(keys)

#   for key, value in request.session.items():
#     print(key, value)

#   age = request.session.setdefault('age',21)
#   print(age)

#   session_age = request.session.get_session_cookie_age()
#   print("session cookie age: ", session_age)

#   expiry_date = request.session.get_expiry_date()
#   print("expiry date: ", expiry_date)

#   expiry_age = request.session.get_expiry_age()
#   print("expiry age: ", expiry_age)

#   expiry_at_browser_close = request.session.get_expire_at_browser_close()
#   print("browser close: ", expiry_at_browser_close)

#   request.session['token'] = f'{datetime.datetime.now()}'
#   request.session['name'] = 'Django'
#   return render(request, 'student/sessionmethodsinview.html')


# def clearsession(request):
#   request.session.clear_expired()
#   return render(request, 'student/clearsession.html')


# def sessionmethodsintemplate(request):
#   for key, value in request.session.items():
#     print(key, value)
#     value = {
#       'key': key,
#       'value': value
#     }
#   return render(request, 'student/sessionmethodsintemplate.html', value)

# def settestcookie(request):
#   response = render(request, 'student/settestcookie.html')
#   request.session.set_test_cookie()
#   return response

# def checktestcookie(request):
#   print(request.session.test_cookie_worked()) # true or false
#   return render(request, 'student/checktestcookie.html')

# def deltestcookie(request):
#   response = render(request, 'student/deltestcookie.html')
#   request.session.delete_test_cookie()
#   return response


# # in seeting

# SESSION_COOKIE_AGE = 60 * 60 * 24 * 7
# SESSION_COOKIE_NAME = 'sessionid'
# SESSION_COOKIE_PATH = '/home'


@cache_page(timeout = 60 * 15, key_prefix='test')
def home(request):
  return render(request, 'student/home.html')

def about(request):
  return render(request, 'student/about.html')
