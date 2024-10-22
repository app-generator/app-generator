import requests, base64
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import os, json, pprint

# Create your views here.

def index(request):
    context = {
        'segment'        : 'django_generator',
        'parent'         : 'tools',
        'page_title'     : 'Django App Generator - Select Design, DataBase, Auth and Tools',
        'page_info'      : 'Generate Django projects and customize the database, APIs, deployment and authentication',
        'page_keywords'  : 'Django generator, app generator, generate Django starters, generate Django APIs, custom development, ai tools, dev tools, tools for developers and companies',
        'page_canonical' : 'tools/django-generator',        
    }
    return render(request, "tools/django-generator.html", context)


class StatusView(APIView):

    def post(self, request):
        # Use pprint to print the incoming JSON data from the frontend
        pprint.pprint(request.data)

        response_data = {
            "status": "200",
            "info": "Django Template is generating"
        }
        return Response(response_data, status=status.HTTP_200_OK)


class DesignView(APIView):
    def get(self, request):
        data_file_path = os.path.join(settings.MEDIA_ROOT, 'generator/django', 'data.json')

        # Check if the file exists
        if not os.path.exists(data_file_path):
            return Response(
                {"error": "Data file not found."}, 
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            # Open and read the JSON file
            with open(data_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # Return the JSON data
            return Response(data, status=status.HTTP_200_OK)

        except json.JSONDecodeError:
            return Response(
                {"error": "Invalid JSON format in data file."}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )