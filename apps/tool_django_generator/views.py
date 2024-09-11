import requests, base64
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse
from django.utils.safestring import mark_safe

# Create your views here.

def index(request):
    return HttpResponse('DevTools -> Django Generator')
