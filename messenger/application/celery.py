import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')

app = Celery('application')

app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://localhost:6379/0'

app.conf.beat_schedule = {
    'receive-every-10-minutes': {
    'task': 'users.tasks.user_login_count',
    'schedule': 600.0,
    'args': ()
    },
}

'''

app.conf.beat_schedule = {
    'count-login-users-every-day': {
    'task': 'users.tasks.user_login_count',
    'schedule': crontab(hour=0, minute=0),
    'args': ()
    },
}

'''

app.conf.timezone = 'Europe/Moscow'


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()