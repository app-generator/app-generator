import os, json, uuid
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.common.models import *
from apps.generator import * 

class Command(BaseCommand):

    help = 'Generate Code'

    def add_arguments(self, parser):
        
        parser.add_argument('-i', '--info'      , action='store_true', help='Prin Help'            )
        parser.add_argument('-f',                 type=str,            help='JSON Input File'      )
        parser.add_argument('-p', '--print'     , action='store_true', help='Print INPUT infos'    )
        parser.add_argument('-s', '--simulate'  , action='store_true', help='Simulate the process' )

    def handle(self, *args, **kwargs):

        ARG_HELP   = kwargs[ 'info' ]
        ARG_JSON   = kwargs[ 'f'    ]
        ARG_PRINT  = kwargs[ 'print' ]
        ARG_SIMU   = kwargs[ 'simulate' ]

        if ARG_HELP:
            print(f"")
            print(f" > HELP: Generator (CLI version)")
            print(f"    -i (or --info)      : Print this help, and exit")
            print(f"    -f <INPUT.json>     : Specify JSON to use as input")
            print(f"    -p (or --print)     : Print INPUT infos, and exit")
            print(f"    -s (or --simulate)  : Simulate the generation (no output code), and exit")
            print(f"")

            return  

        # print(' > Using input: ' + json_file )                    

        JSON_PATH = os.path.join( INPUT_JSON_VOLT )

        if ARG_JSON:
            JSON_PATH = ARG_JSON    
            
        # load data
        JSON_DATA = json_load( JSON_PATH )

        if not JSON_DATA:
            print( ' > Err loading JSON: ' + JSON_PATH )            
            return

        print( ' > Processing ' + JSON_PATH ) 
    
        ### Start Processing 

        DIR_ID  =  uuid.uuid4().hex   
        SRC_DIR = os.path.join( DIR_GEN_APPS, DIR_ID )

        input_design  = JSON_DATA['design']
        input_docker  = True if ( JSON_DATA['deploy']['docker'] == '1'  ) else False
        input_cicd    = True if ( JSON_DATA['deploy']['cicd'  ] == '1'  ) else False
        input_live    = True if ( JSON_DATA['deploy']['live'  ] == '1'  ) else False
        input_api_gen = True if ( len( JSON_DATA['tools']['api_generator'] ) > 0 ) else False

        if ARG_PRINT:
            print(f"")
            print(f" > Print Generator Input")
            print(f"    design        : " + input_design )
            print(f"    api_generator : " + str(input_api_gen) )
            print(f"")

            return               

        reset_sources( SRC_DIR )

        # Inject UI
        # DASHBOARDs
        if 'volt' == input_design:
            product_volt( SRC_DIR )
        elif 'soft-dashboard' == input_design :
            product_soft( SRC_DIR )
        elif 'material' == input_design:
            product_material( SRC_DIR )        
        elif 'datta' == input_design:
            product_datta( SRC_DIR )          
        elif 'adminlte' == input_design:
            product_adminlte( SRC_DIR )          

        ## KITs
        elif 'soft-kit' == input_design:
            product_soft_kit( SRC_DIR )
        elif 'material-kit' == input_design:
            product_material_kit( SRC_DIR )
        elif 'pixel' == input_design:
            product_pixel( SRC_DIR )

        else:
            print( 'ERROR: Unsupported Design: ' + input_design )
            print( '     |- Expected: volt, datta, material, pixel, adminlte ' )
            return            
      
        retCode = custom_user_gen( SRC_DIR, JSON_DATA ) 
        if COMMON.OK != retCode:
            print( 'ERROR: generate CUSTOM USER' )   
            return

        # Add the new models
        retCode = models_gen( SRC_DIR, JSON_DATA )
        if COMMON.OK != retCode:
            print( 'ERROR: generate MODELS' )   
            return
    
        # Added API 
        if input_api_gen:
            deps_add(SRC_DIR, 'django-api-generator')
            settings_apps_add(SRC_DIR, 'django_api_gen')
            settings_apps_add(SRC_DIR, 'rest_framework')
            settings_apps_add(SRC_DIR, 'rest_framework.authtoken')
            api_gen_sources(SRC_DIR, JSON_DATA)
            api_gen_script(SRC_DIR)
            api_gen_docker(SRC_DIR)
        else:
            print( ' > API GEN: No INPUT' ) 

        #dir_delete( SRC_DIR )