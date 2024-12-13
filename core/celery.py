# your_project/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

celery_app = Celery('celery_app')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'run-critical-task': {
        'task': 'apps.tasks.tasks.run_critical_task',
        'schedule': crontab(minute='*/5'),
    },
    'run-hourly-task': {
        'task': 'apps.tasks.tasks.run_hourly_task',
        'schedule': crontab(minute=0, hour='*/1'),
    },
    'run-daily-task': {
        'task': 'apps.tasks.tasks.run_daily_task',
        'schedule': crontab(minute=0, hour=0),
    },
    'run-weekly-task': {
        'task': 'apps.tasks.tasks.run_weekly_task',
        'schedule': crontab(minute=0, hour=0, day_of_week='sunday'),
    },
    'run-monthly-task': {
        'task': 'apps.tasks.tasks.run_monthly_task',
        'schedule': crontab(minute=0, hour=0, day_of_month='1'),
    },
}
