import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BulletinBoard.settings')

app = Celery('BulletinBoard')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'BB.tasks.week_email_sending',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}

app.autodiscover_tasks()