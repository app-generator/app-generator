from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json, pprint
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
    pprint.pprint(request.data)
    response_data = {
        "status": 200,
        "message": "Analyzed Data"
    }
    return Response(response_data, status=status.HTTP_200_OK)