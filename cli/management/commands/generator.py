import os, json, uuid
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.common.models import *
from apps.generator import * 

class Command(BaseCommand):
    help = 'Generate Code'

    def handle(self, *args, **kwargs):

        print(' > Here, we generate code')    
        DIR_ID  =  uuid.uuid4().hex   
        SRC_DIR = os.path.join( DIR_GEN_APPS, DIR_ID )

        reset_sources( SRC_DIR )

        JSON_PATH = os.path.join( FILE_INPUT_JSON_DATTA )

        JSON_DATA = json_load( JSON_PATH )

        print( JSON_DATA['design'] )

        input_design = JSON_DATA['design']

        # DASHBOARDs
        if 'volt' == input_design:
            product_volt( SRC_DIR )
        elif 'soft-dashboard' == input_design :
            product_soft( SRC_DIR )
            product_corporate( SRC_DIR )
        else:
            product_datta( SRC_DIR )          

        #dir_delete( SRC_DIR )