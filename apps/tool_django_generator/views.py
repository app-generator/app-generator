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
from django.contrib.sessions.models import Session
import os, json, pprint

from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

from apps.common.models import *
from helpers.generator import *
from helpers.util import get_client_ip

from apps.tasks.tasks import *
from celery.result import AsyncResult
from core.celery import celery_app
from apps.common.models_generator import *

# Create your views here.


# @ratelimit(key='user_or_ip', rate='3/m')
def index(request):

    context = {
        "segment": "django_generator",
        "parent": "tools",
        "page_title": "Django App Generator - Select Design, DataBase, Auth and Tools",
        "page_info": "Generate Django projects and customize the database, APIs, deployment and authentication",
        "page_keywords": "Django generator, app generator, generate Django starters, generate Django APIs, custom development, ai tools, dev tools, tools for developers and companies",
        "page_canonical": "tools/django-generator",
    }

    return render(request, "tools/django-generator.html", context)


class StatusView(APIView):

    # @method_decorator(ratelimit(key='user_or_ip', rate='3/m'))
    def _get_sessionid(self, request):
        return request.COOKIES.get("sessionid")

    def _unauthorized_response(self):
        return Response(
            '{"status": "400", "info": "Unauthorized User. Please login first"}',
            content_type="application/json",
        )

    def post(self, request):

        result = task_generator.delay(request.data)

        app = GeneratedApp()
        app.task_id = result.id
        app.user_ip = get_client_ip(request)

        try:

            sessionid = self._get_sessionid(request)
            if sessionid:
                session = Session.objects.get(session_key=sessionid)
                session_data = session.get_decoded()
                uid = session_data.get('_auth_user_id')
                user = User.objects.get(id=uid)            
                app.user = user
                print(" > User " + str(user))
            else:
                print(" > Guest User ")
        
        except:
            print(" > Error Getting Auth User ")

        # Save the creation
        app.save()

        task_result = result.get()

        app.task_log = json.dumps(task_result)
        if "gh_repo" in task_result:
            app.gh_repo = task_result["gh_repo"]

        # Save the update
        app.task_state = task_result["task_state"]
        app.task_result = task_result["task_result"]
        app.save()

        task_result["status"] = (
            task_result["task_state"] + ", " + task_result["task_result"]
        )
        task_result["info"] = (
            task_result["task_info"] + ", result: " + task_result["task_output"]
        )

        return Response(task_result, status=status.HTTP_200_OK)


class DesignView(APIView):

    def get(self, request):
        data_file_path = os.path.join(
            settings.MEDIA_ROOT, "generator/django", "data.json"
        )

        # Check if the file exists
        if not os.path.exists(data_file_path):
            return Response(
                {"error": "Data file not found."}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            # Open and read the JSON file
            with open(data_file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            # Return the JSON data
            return Response(data, status=status.HTTP_200_OK)

        except json.JSONDecodeError:
            return Response(
                {"error": "Invalid JSON format in data file."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
