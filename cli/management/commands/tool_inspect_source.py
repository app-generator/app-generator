import os, json, uuid
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.helpers.generator     import *
from apps.helpers.csv_processor import *

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

        print( ' > Processing ' + ARG_JSON )
        print( '       |-- file: ' + JSON_DATA['source'] )
        print( '       |-- type: ' + JSON_DATA['type'  ] )
        
        # @TBD-227: The source can be remote, [#227](https://github.com/app-generator/app-generator/issues/227) fix is needed
        # https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv 

        if not file_exists( JSON_DATA['source'] ):
            print( ' > Err loading SOURCE: ' + JSON_DATA['source'] )            
            return

        csv_types = parse_csv( JSON_DATA['source'] )
        print ( csv_types )

        csv_data = load_csv_data( JSON_DATA['source'] )
        
        idx = 0
        for l in csv_data:
            idx += 1
            print( '['+str(idx)+'] - ' + str(l) )  