import asyncio
import time

from django.shortcuts import HttpResponse
import httpx
from django.http import JsonResponse

# def index(request):
#   # this is general view and execute syncronously
#   return HttpResponse("hello")

# async def task1(request):
#   # this is general view and execute syncronously
#   return HttpResponse("hello")

def sync_view(request):
  start = time.time()

  responses = []

  for _ in range(10):
    res = httpx.get("https://google.com")
    responses.append(res.json())
    print(time.time() - start)

  return JsonResponse(
    {
      "responses": responses,
      "time taken": time.time() - start
    }
)

async def async_view(request):
  start = time.time()

  async with httpx.AsyncClient() as client:
    # task = [client.get("https://google.com") for _ in range(10)]
    # responses = await asyncio.gather(*task)
    task1 = client.get("https://google.com")
    task2 = client.get("https://google.com")
    task3 = client.get("https://google.com")
    task4 = client.get("https://google.com")
    task5 = client.get("https://google.com")
    task6 = client.get("https://google.com")
    task7 = client.get("https://google.com")
    task8 = client.get("https://google.com")
    task9 = client.get("https://google.com")
    task10 = client.get("https://google.com")
    responses = await asyncio.gather(task1, task2, task3, task4, task5, task6, task7, task8, task9, task10)

  return JsonResponse(
    {
      "responses": responses,
      "time taken": time.time() - start
    }
  )

# ============================================================================================

from django.shortcuts import render
from asgiref.sync import sync_to_async, async_to_sync

# sync to async
# def callll(x):
#   return x**2

# async def callll(request):
#     res = await sync_to_async(callll)(2)
#     return res


# async to sync
async def callll(x):
  return x**2

def callll(request):
    res = async_to_sync(callll)(2)
    return res