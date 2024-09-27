import os, json, uuid, shutil
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.common.models import *
from helpers.docker_generator import * 

class Command(BaseCommand):

    help = 'Generate Docker Files for repos'

    def add_arguments(self, parser):
        
        parser.add_argument('-i', '--info'      , action='store_true', help='Prin Help'            )
        parser.add_argument('-r',                 type=str,            help='Repository URL'       )
    def handle(self, *args, **kwargs):

        ARG_HELP   = kwargs[ 'info' ]
        ARG_REPO   = kwargs[ 'r'    ]

        if ARG_HELP:
            print(f"")
            print(f" > HELP: Generator (CLI version)")
            print(f"    -i (or --info)      : Print this help, and exit")
            print(f"    -r <REPOSITORY>     : The Repository URL")
            print(f"")

            return  

        detector = ApplicationDetector(ARG_REPO)
        app_type = detector.detect()

        print(' > REPO: ' + ARG_REPO )                
        print('     |- (type): ' + app_type )                

        if COMMON.NA != app_type:
            dockerizer = Dockerizer(ARG_REPO, app_type)
            dockerizer.generate_files()
            self.stdout.write(self.style.SUCCESS(f'Generated Docker files for {app_type.upper()} application'))
        else:
            self.stdout.write(self.style.ERROR('Could not detect application type'))
