from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
  return render(request, 'pages/starter.html')


def support(request):
  context = {
    'segment': 'support'
  }
  return render(request, 'pages/support.html', context)