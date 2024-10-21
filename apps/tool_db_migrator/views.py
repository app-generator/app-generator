from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json, pprint
# Create your views here.

def db_migrator(request):

    context = {
        'segment': 'db_migrator',
        'parent': 'tools'
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
    pprint.pprint(request.data)
    response_data = {
        "status": 200,
        "message": "Data migrated successfully"
    }
    return Response(response_data, status=status.HTTP_200_OK)