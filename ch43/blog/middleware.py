
from logging import config

from django.http import HttpResponse
from django.shortcuts import render
from decouple import config




# function based
# def function_middle(get_response):

#   print("one time initialization")
#   def middleware(request):
#     print("Before View")
#     response = get_response(request)
#     print("After View")
#     return response
#   return middleware

# def function_middle(get_response):

#   print("one time initialization")
#   def middleware(request):
#     print("Before View")
#     # response = get_response(request)
#     # response = HttpResponse("Middle ware")
#     response = render(request, 'blog/home.html')
#     print("After View")
#     return response
#   return middleware

















# Class based
# class function_middle:
#   def __init__(self, get_response):
#       print("one time initialization")
#       self.get_response = get_response

#   def __call__(self, request):
#       print("Before View")
#       response = self.get_response(request)
#       print("After View")
#       return response

# class function_middle:
#   def __init__(self, get_response):
#       print("one time initialization")
#       self.get_response = get_response

#   def __call__(self, request):
#       print("Before View")
#       response = self.get_response(request)
#       print("After View")
#       return response

#   def process_view(request, *args, **kwargs):
#     print("process view")
#     return None
#   # here if return is None, then view will able to execute else view will not able to execute


# class function_middle:
#   def __init__(self, get_response):
#       print("one time initialization")
#       self.get_response = get_response

#   def __call__(self, request):
#       print("Before View")
#       response = self.get_response(request)
#       print("After View")
#       return response

#   def process_exception(self, request, exception):
#     print("process exception")
#     msg = exception
#     class_name = exception.__class__.__name__
#     return render(request, 'blog/exception.html', {'msg': msg, 'class_name': class_name})
#   # Note: it's run when any exception occur



#   class function_middle:
#   def __init__(self, get_response):
#       print("one time initialization")
#       self.get_response = get_response

#   def __call__(self, request):
#       print("Before View")
#       response = self.get_response(request)
#       print("After View")
#       return response

#   def process_templates_response(self, request, response):
#     print("process templates response")
#     response.context_data['name'] = 'Django'
#     return response
  # Note: it's run when template render




# ===============================================


# custom middleware


# this is casuall way but for more feature and admin panel interface we use 2nd option
# class function_middle:
#     def __init__(self, get_response):
#         print("one time initialization")
#         self.get_response = get_response

#     def __call__(self, request):
#         print("Before View")
#         response = render(request, 'blog/home.html') # for under construction
#         print("After View")
#         return response

from .models import underconstruction
class function_middle:
    def __init__(self, get_response):
        print("one time initialization")
        self.get_response = get_response

    def __call__(self, request):


        # admin logout issue fix
        secret_key = config('SECRET_KEY')
        if 'u' in request.GET and request.GET['u'] == secret_key:
            request.session['dynamic_bypass'] = True
        if request.session.get('dynamic_bypass'):
            return self.get_response(request)

        # admin able to get view
        if request.user.is_staff:
            return self.get_response(request)
        try:
            uc = underconstruction.objects.first()
            if uc and uc.is_under_construction:
                return render(request, 'blog/underconstruction.html', {'note': uc.note, 'duration': uc.duration})
        except Exception as e:
            print(e)
            return render(request, 'blog/exception.html', {'msg': e, 'class_name': e.__class__.__name__})

        return self.get_response(request)