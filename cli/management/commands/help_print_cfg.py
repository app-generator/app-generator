from django.core.management.base import BaseCommand
from django.utils import timezone

from django.conf import settings

class Command(BaseCommand):
    help = 'Displays project config'

    def handle(self, *args, **kwargs):
        
        # type( settings ) => <class 'django.conf.LazySettings'>
        # settings.__dict__

        # Iterate over apps
        for key in settings.__dict__.keys():

            self.stdout.write(" Cfg Key: " + key + " -> %s" % settings.__dict__[ key ] )
        