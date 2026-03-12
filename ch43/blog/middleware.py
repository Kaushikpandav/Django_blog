
from django.http import HttpResponse
from django.shortcuts import render





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
class function_middle:
  def __init__(self, get_response):
      print("one time initialization")
      self.get_response = get_response

  def __call__(self, request):
      print("Before View")
      response = self.get_response(request)
      print("After View")
      return response

class function_middle:
  def __init__(self, get_response):
      print("one time initialization")
      self.get_response = get_response

  def __call__(self, request):
      print("Before View")
      response = self.get_response(request)
      print("After View")
      return response

  def process_view(request, *args, **kwargs):
    print("process view")
    return None
  # here if return is None, then view will able to execute else view will not able to execute


class function_middle:
  def __init__(self, get_response):
      print("one time initialization")
      self.get_response = get_response

  def __call__(self, request):
      print("Before View")
      response = self.get_response(request)
      print("After View")
      return response

  def process_exception(self, request, exception):
    print("process exception")
    msg = exception
    class_name = exception.__class__.__name__
    return render(request, 'blog/exception.html', {'msg': msg, 'class_name': class_name})
  # Note: it's run when any exception occur



  class function_middle:
  def __init__(self, get_response):
      print("one time initialization")
      self.get_response = get_response

  def __call__(self, request):
      print("Before View")
      response = self.get_response(request)
      print("After View")
      return response

  def process_templates_response(self, request, response):
    print("process templates response")
    response.context_data['name'] = 'Django'
    return response
  # Note: it's run when template render