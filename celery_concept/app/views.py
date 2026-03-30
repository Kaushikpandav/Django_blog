from celery.result import AsyncResult
from django.shortcuts import render
from celery_concept.celery_main import add
from .tasks import sub

#simple
# def index(request):
#   print("index")
#   add.delay(1,2)
#   res = sub.delay(2,1)
#   print(res.get())
#   return render(request, 'index.html')

# async
# def index(request):
  # res1 = add.apply_async(args=[1,2])
  # print(res1.get())
  # res = sub.apply_async(args=[2,1])
  # print(res.get())
  # return render(request, 'index.html')

# Display after delay
def home(request, ):
  print("index")
  # add.delay(1,2)
  res = sub.delay(2,1)
  print("ready: ", res.ready())
  print("success: ", res.successful())
  print("failled: ", res.failed())
  return render(request, 'index.html', {'res': res})

def index(request, task_id=None):
  print("index")
  # Convert UUID to string for AsyncResult
  res = AsyncResult(str(task_id))
  print("ready: ", res.ready())
  print("success: ", res.successful())
  print("failled: ", res.failed())
  # print("get: ", res.get()) # it's blocking and act as syncronous..

  return render(request, 'check.html', {'res': res, 'task_id': task_id})

def about(request):
  print("about")
  return render(request, 'about.html')

def contact(request):
  print("contact")
  return render(request, 'contact.html')