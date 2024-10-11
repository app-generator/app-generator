import requests, base64
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


def index(request):
    return render(request, "tools/django-generator.html")


class StatusView(APIView):
    def post(self, request):
        response_data = {"status": "200", "info": "DJango Template is generating "}
        return Response(response_data, status=status.HTTP_200_OK)
