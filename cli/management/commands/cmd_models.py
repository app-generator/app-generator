from django.core.management.base import BaseCommand
from django.utils import timezone

from django.apps import apps

class Command(BaseCommand):
    help = 'Displays registered apps and models'

    def handle(self, *args, **kwargs):
        
        # Iterate over apps
        for app in apps.get_app_configs():
            self.stdout.write(" APP -> %s" % app.verbose_name)

            # Iterate over models
            for model in app.get_models():
                self.stdout.write("\t |- (model) -> %s" % model)
        