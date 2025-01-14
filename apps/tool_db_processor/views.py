from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json, pprint
from helpers.db_processor import *
# Create your views here.

def db_processor(request):

    context = {
        'segment'        : 'db_processor',
        'parent'         : 'tools',
        'page_title'     : 'DataBase Processor - Analyze and Unload Data for SQLite, PostgreSQL, MySql',
        'page_info'      : 'Process your database information with ease - unload, analyze schema, download in different formats',
        'page_keywords'  : 'db processor, unload db data, sql to json, database tools, db tool, custom development, ai tools, dev tools, tools for developers and companies',
        'page_canonical' : 'tools/db-migrator',        
    }     
    return render(request, "tools/db-processor.html", context)


@api_view(['POST'])
def check_connect_view(request):
    pprint.pprint(request.data)
    response_data = {
        "status": 200,
        "message": "Connect successfully"
    }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
def db_analyze_view(request):
    source_db = request.data.get('sourceDB', {})

    v_db_driver = source_db[ 'driver' ]
    v_db_name   = source_db[ 'name'   ]
    v_db_sqlite = True

    v_db_host   = None
    v_db_port   = None
    v_db_user   = None
    v_db_pass   = None

    if 'sqlite' not in v_db_driver.strip().lower():
        v_db_sqlite = False
        v_db_host   = source_db[ 'host' ]
        v_db_port   = source_db[ 'port' ]
        v_db_user   = source_db[ 'user' ]
        v_db_pass   = source_db[ 'pass' ]

    print( '> Processing ' )
    # print( '    |-- type      : ' + v_type )
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

    response_data = {
        "status": 200,
        "message": "Analyzed Data"
    }
    return Response(response_data, status=status.HTTP_200_OK)