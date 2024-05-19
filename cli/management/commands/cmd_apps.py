from django.core.management.base import BaseCommand
from django.utils import timezone

from django.apps import apps

class Command(BaseCommand):
    help = 'Displays registered apps'

    def handle(self, *args, **kwargs):
        for app in apps.get_app_configs():
            self.stdout.write(" APP -> %s" % app.verbose_name)
        