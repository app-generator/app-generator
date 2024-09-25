import os, requests
from django.core.management.base import BaseCommand
from django.conf import settings
from helpers.generator     import *
from helpers.csv_processor import *
from tabulate import tabulate

DIR_TMP = os.path.join(settings.BASE_DIR, 'tmp')

class Command(BaseCommand):

    help = 'Inspect DATA Sources'

    def add_arguments(self, parser):
        
        parser.add_argument('-i', '--info'      , action='store_true', help='Prin Help'               )
        parser.add_argument('-f',                 type=str,            help='JSON Input File'         )
        parser.add_argument('-p', '--print'     , action='store_true', help='Print INPUT infos'       )
        parser.add_argument('-k',                 action='store_true', help='Print entire input file' )

    def handle(self, *args, **kwargs):

        ARG_HELP       = kwargs[ 'info' ]
        ARG_JSON       = kwargs[ 'f'    ]
        ARG_FULL_PRINT = kwargs[ 'k' ]

        if ARG_HELP:
            print(f"")
            print(f" > HELP: DS Inspector (CLI version)")
            print(f"    -i (or --info)      : Print this help, and exit")
            print(f"    -f <INPUT.json>     : Specify JSON to use as input")
            print(f"    -p (or --print)     : Print INPUT infos, and exit")
            print(f"")

            return  

        if ARG_FULL_PRINT:
            ARG_FULL_PRINT = True 
        else:
            ARG_FULL_PRINT = False

        if not ARG_JSON:
            print( ' > Err: JSON file not specified (use -f JSON_FILE)' )            
            return

        # load data
        JSON_DATA = json_load( ARG_JSON )

        if not JSON_DATA:
            print( ' > Err loading JSON: ' + ARG_JSON )            
            return

        print( '> Processing ' + ARG_JSON )
        print( '    |-- file: ' + JSON_DATA['source'] )
        print( '    |-- type: ' + JSON_DATA['type'  ] )
        print( '\n')
        
        tmp_file_path = None 

        if 'http' in JSON_DATA['source']:
            url = JSON_DATA['source']
            r = requests.get(url)
            tmp_file = h_random_ascii( 8 ) + '.csv'
            tmp_file_path = os.path.join( DIR_TMP, tmp_file )
            if not file_write(tmp_file_path, r.text ):
                return
            JSON_DATA['source'] = tmp_file_path
        else:    
            if not file_exists( JSON_DATA['source'] ):
                print( ' > Err loading SOURCE: ' + JSON_DATA['source'] )            
                return

        csv_types = parse_csv( JSON_DATA['source'] )
        
        #pprint.pp ( csv_types )
        
        table_headers = ['Field', 'CSV Type', 'Django Types']
        table_rows    = []
        
        for t in csv_types:
            t_type        = csv_types[t]['type']
            t_type_django = django_fields[ t_type ]
            table_rows.append( [t, t_type, t_type_django] )

        print(tabulate(table_rows, table_headers))
        print( '\n')
        
        csv_data = load_csv_data( JSON_DATA['source'] )
        
        idx = 0
        for l in csv_data:
            idx += 1
            print( '['+str(idx)+'] - ' + str(l) )  

            # Truncate output ..
            if not ARG_FULL_PRINT and idx == 10:
                print( ' ... (truncated output) ' ) 
                break            
            
        if tmp_file_path:
            file_delete( tmp_file_path )
     