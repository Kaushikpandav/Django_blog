from django.shortcuts import render

# Create your views here.

def home(request):
  print("home")
  return render(request, 'blog/home.html')

def user(request):
  print("user")
  return render(request, 'blog/user.html')

def math(request):
  print("math")
  a = 100/0
  return render(request, 'blog/math.html', {'a': a})
