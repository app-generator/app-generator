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

                prefix = str(model.__module__ + '.' + model.__name__)
                self.stdout.write("\t |--> %s" % prefix )
                prefix = prefix.replace('.models', '')
                fields = model._meta.fields
                for f in fields:
                    f_type = str( type(f).__qualname__ )
                    f_name = str( f ).replace(prefix + '.', '')
                    f_info = f_name + ': ' + f_type
                    self.stdout.write("\t   |--> %s " % f_info ) 
        