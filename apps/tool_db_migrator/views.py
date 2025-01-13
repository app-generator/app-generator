from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json, pprint
from helpers.db_migrator import *
# Create your views here.

def db_migrator(request):
  
    context = {
        'segment'        : 'db_migrator',
        'parent'         : 'tools',
        'page_title'     : 'DataBase Migrator - SQLite to MySql, MySql to PostgreSQL, PostgreSQL to SQLite',
        'page_info'      : 'Migrate databases with ease, all DBMS supported: PostgreSQL, MySql, MariaDB, SQLite',
        'page_keywords'  : 'db migrator, sqlite to mysql, mysql to postgresql, database tools, db tool, custom development, ai tools, dev tools, tools for developers and companies',
        'page_canonical' : 'tools/db-migrator',        
    }    
    return render(request, "tools/db-migrator.html", context)


@api_view(['POST'])
def check_connect_view(request):
    pprint.pprint(request.data)
    response_data = {
        "status": 200,
        "message": "Connect successfully"
    }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
def db_migrate_view(request):
    # pprint.pprint(request.data)

    source_db = request.data.get('sourceDB', {})
    target_db = request.data.get('targetDB', {})

    migrator = DatabaseMigrator(source_db, target_db)
    source_conn, source_engine, target_conn, target_engine = migrator.connect()

    if not source_conn:
        print("Failed to connect to SOURCE DB. Aborting.")

    if not target_conn:
        print("Failed to connect to TARGET DB. Aborting.")

    source_tables = migrator.get_tables(migrator.source_conn, source_engine)
    target_tables = migrator.get_tables(migrator.target_conn, target_engine)

    print(' > SRC  Tables: ' + str(source_tables) )
    print(' > DEST Tables: ' + str(target_tables) )

    identical_tables = migrator.compare_schemas(source_tables, target_tables)

    if len( identical_tables.keys() ) == 0:
        print("No identical tables found between the databases.")
    else:
        print("Identical tables that can be migrated:")
        for src_table in identical_tables.keys():
            dest_table = identical_tables[src_table]
            print(f"- {src_table} -> {dest_table}")

        migrator.migrate_tables(identical_tables, 1000)

    migrator.close()

    response_data = {
        "status": 200,
        "message": "Data migrated successfully"
    }
    return Response(response_data, status=status.HTTP_200_OK)