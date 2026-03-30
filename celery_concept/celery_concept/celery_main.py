import os
from celery import Celery
from datetime import timedelta
from celery.schedules import crontab, solar

# In celery_setup.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_concept.settings')
app = Celery('celery_concept', broker='redis://localhost:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks from installed apps
app.autodiscover_tasks(['app'])


@app.task(name='add')
def add(x, y):
    print(f"x : {x}, y : {y}")
    return x + y

# Use this for tasks defined in this file
app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'app.tasks.clear_session_cache',
        'schedule': 10.0,
        'args': (16, 16)
    },
}

# using timedelta
app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'add',
        'schedule': timedelta(seconds=10),
        'args': (16, 16)
    },
}

# using crontab
app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'add',
        'schedule': crontab(hour='7', minute='32', day_of_week='1'),
        'args': (16, 16)
    },
}

# solar schedule
app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'add',
        'schedule': solar('sunset', -23.4343, 133.1234),
        'args': (16, 16)
    },
}


# we can use custom schedule : django-celery-beat: it use to store the schedule in database and we can manage it from admin panel

# pip install django-celery-beat

# in settings.py
CEELERY_BEAT_SCHEDULE = 'django_celery_beat.schedulers:DatabaseScheduler'


# in tasks.py

from django_celery_beat.models import PeriodicTask
from celery import shared_task

@shared_task
def clear_cache(key):
    print(f"Clearing cache for key: {key}")
    # logic to clear cache
    return key
