import os, json, uuid
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.helpers.generator     import *
from apps.helpers.csv_processor import *
import requests, pprint
from tabulate import tabulate
from apps.helpers.db_processor import *

DIR_TMP = os.path.join(settings.BASE_DIR, 'tmp')

class Command(BaseCommand):

    help = 'Inspect DATA Sources'

    def add_arguments(self, parser):
        
        parser.add_argument('-i', '--info'      , action='store_true', help='Prin Help'            )
        parser.add_argument('-f',                 type=str,            help='JSON Input File'      )
        parser.add_argument('-p', '--print'     , action='store_true', help='Print INPUT infos'    )

    def handle(self, *args, **kwargs):

        ARG_HELP   = kwargs[ 'info' ]
        ARG_JSON   = kwargs[ 'f'    ]
        ARG_PRINT  = kwargs[ 'print' ]

        if ARG_HELP:
            print(f"")
            print(f" > HELP: DS Inspector (CLI version)")
            print(f"    -i (or --info)      : Print this help, and exit")
            print(f"    -f <INPUT.json>     : Specify JSON to use as input")
            print(f"    -p (or --print)     : Print INPUT infos, and exit")
            print(f"")

            return  

        if not ARG_JSON:
            print( ' > Err: JSON file not specified (use -f JSON_FILE)' )            
            return

        # load data
        JSON_DATA = json_load( ARG_JSON )

        if not JSON_DATA:
            print( ' > Err loading JSON: ' + ARG_JSON )            
            return

        v_file = ARG_JSON
        v_type = JSON_DATA[ 'type' ]
        v_db_driver = JSON_DATA[ 'db_driver' ]
        v_db_name   = JSON_DATA[ 'db_name'   ]
        v_db_sqlite = True

        v_db_host   = None
        v_db_port   = None
        v_db_user   = None
        v_db_pass   = None

        if 'sqlite' not in v_db_driver.strip().lower():
            v_db_sqlite = False
            v_db_host   = JSON_DATA[ 'db_host' ]
            v_db_port   = JSON_DATA[ 'db_port' ]
            v_db_user   = JSON_DATA[ 'db_user' ]
            v_db_pass   = JSON_DATA[ 'db_pass' ]

        print( '> Processing ' + ARG_JSON )
        print( '    |-- type      : ' + v_type )
        print( '    |-- DB driver : ' + v_db_driver )
        print( '    |-- DB name   : ' + v_db_name )
        print( '    |-- DB host   : ' + str(v_db_host) )
        print( '    |-- DB port   : ' + str(v_db_port) )
        print( '    |-- DB user   : ' + str(v_db_user) )
        print( '    |-- DB pass   : ' + str(v_db_pass) )
        print( '\n')
        
        db_conn = DbWrapper()
        db_conn.driver = v_db_driver 
        db_conn.db_name = v_db_name
        
        if not v_db_sqlite:
            db_conn.db_host = v_db_host
            db_conn.db_port = int(v_db_port)
            db_conn.db_user = v_db_user
            db_conn.db_pass = v_db_pass

        if not db_conn.connect():
            print( ' > Err Connect to DB' )            
            return            

        db_conn.load_models()
        db_conn.dump_tables()    
        db_conn.dump_tables_data() 
