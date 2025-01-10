from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db import connections
from django.db.utils import OperationalError
import json, pprint
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


def configure_connection(alias, db_config):
    connection_params = {
        "ENGINE": f"django.db.backends.{db_config.get('driver', 'sqlite')}",
        "NAME": db_config.get('name'),
        "USER": db_config.get('user'),
        "PASSWORD": db_config.get('pass'),
        "HOST": db_config.get('host', 'localhost'),
        "PORT": db_config.get('port', 5432),
        'ATOMIC_REQUESTS': False,
        'TIME_ZONE': 'UTC',
        'CONN_HEALTH_CHECKS': False,
        'CONN_MAX_AGE': 0,
        'AUTOCOMMIT': True,
        'OPTIONS': {
            'connect_timeout': 5,
        }
    }
    connections.databases[alias] = connection_params


@api_view(['POST'])
def check_connect_view(request):
    try:
        configure_connection('test_db', request.data)
        with connections['test_db'].cursor() as cursor:
            cursor.execute("SELECT 1;")
            cursor.fetchall()

        response_data = {
            "status": 200,
            "message": "Connection successful",
        }
        return Response(response_data, status=status.HTTP_200_OK)

    except OperationalError as e:
        response_data = {
            "status": 400,
            "message": f"Connection failed: {str(e)}",
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def db_migrate_view(request):
    data = request.data
    source_db = data.get('sourceDB')
    target_db = data.get('targetDB')

    if not source_db or not target_db:
        return Response({"status": 400, "message": "Invalid database configurations"}, status=status.HTTP_400_BAD_REQUEST)

    source_alias = 'source_db'
    target_alias = 'target_db'

    try:
        configure_connection(source_alias, source_db)
        configure_connection(target_alias, target_db)

        with connections[source_alias].cursor() as source_cursor, connections[target_alias].cursor() as target_cursor:
            source_cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public';
            """)
            tables = [row[0] for row in source_cursor.fetchall()]

            for table in tables:
                source_cursor.execute(f"SELECT * FROM {table}")
                rows = source_cursor.fetchall()
                columns = [col[0] for col in source_cursor.description]

                placeholders = ', '.join(['%s'] * len(columns))
                column_names = ', '.join(columns)
                insert_query = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})"

                for row in rows:
                    target_cursor.execute(insert_query, row)

        response_data = {
            "status": 200,
            "message": "Data migrated successfully",
        }
        return Response(response_data, status=status.HTTP_200_OK)

    except OperationalError as e:
        return Response(
            {"status": 400, "message": f"Database connection failed: {str(e)}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    except Exception as e:
        return Response(
            {"status": 500, "message": f"Data migration failed: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    finally:
        if source_alias in connections.databases:
            del connections.databases[source_alias]
        if target_alias in connections.databases:
            del connections.databases[target_alias]