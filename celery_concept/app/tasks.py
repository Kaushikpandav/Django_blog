import json

from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask, IntervalSchedule
@shared_task(name='app.tasks.sub')
def sub(x, y):
  sleep(8)
  print(f"x : {x}, y : {y}")
  return x - y

@shared_task(name='app.tasks.clear_session_cache')
def clear_session_cache(id):
  print(f"Clearing session cache for id: {id}")
  return id

@shared_task
def clear_cache(key):
    print(f"Clearing cache for key: {key}")
    # logic to clear cache
    return key


# ==========

# IF WE DONT WANT TO CREATE  INTERVAL AND PERIODIC TASK MANUALLY IN ADMIN THEN WE CAN CREATE IT PROGRAMMATICALLY

schedule , created = IntervalSchedule.objects.get_or_create(
  every=30,
  period=IntervalSchedule.SECONDS
)

PeriodicTask.objects.get_or_create(
  name='Clear session cache every 30 seconds',
  task='app.tasks.clear_session_cache',
  interval=schedule,
  args=json.dumps([16])
)

# celery -A celery_concept.celery_main beat -l info