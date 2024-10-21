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
        'segment': 'django_generator',
        'parent': 'tools'
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