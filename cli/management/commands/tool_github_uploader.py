import os, json, uuid
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.common.models import *
from apps.helpers.generator import * 

class Command(BaseCommand):
    
    help = 'Save Code on GITHUB'

    def add_arguments(self, parser):
        
        parser.add_argument('-i', '--info'      , action='store_true', help='Prin Help'                     )
        parser.add_argument('-d',                 type=str,            help='Dir to upload'                 )
        parser.add_argument('-k',                 type=str,            help='GITHUB Api Key (input or ENV)' )

    def handle(self, *args, **kwargs):

        ARG_HELP       = kwargs[ 'info' ]
        ARG_DIR        = kwargs[ 'd'    ]
        ARG_GITHUB_KEY = kwargs[ 'k'    ]

        if ARG_HELP:
            print(f"")
            print(f" > HELP: GitHub Uploader (CLI version)")
            print(f"    -i (or --info)    : Print this help, and exit")
            print(f"    -d <DIRECTORY>    : Specify DIR for upload"   )
            print(f"    -k <GITHUB_KEY>   : Api Key (input or ENV)"   )
            print(f"")

            return  

        if not ARG_GITHUB_KEY:
            ARG_GITHUB_KEY = os.environ.get('GITHUB_KEY')

        #print(f"")
        #print(f" > Input: ")
        #print(f"    DIRECTORY  : " + str(ARG_DIR       ) )
        #print(f"    GITHUB_KEY : " + str(ARG_GITHUB_KEY) )
        #print(f"")

        if not dir_exists( ARG_DIR ):
            print( ' > Err Input DIR: ' + ARG_DIR )            
            return

        if not ARG_GITHUB_KEY:
            print( ' > Err GITHUB_KEY: None' )            
            return
        
        retVal = repo_create( ARG_DIR, ARG_GITHUB_KEY )

        if retVal:
            print( ' > SUCCESS: Repo [ ' + retVal + ' ] saved on GitHub' )
        else:
            print( ' > Err Saving DIR on GitHub' )

        return
