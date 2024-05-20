from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
  return render(request, 'pages/home.html')

def support(request):
  context = {
    'segment': 'support'
  }
  return render(request, 'pages/support.html', context)

def custom_development(request):
  context = {
    'segment': 'custom_development'
  }
  return render(request, 'pages/custom-development.html', context)

def terms(request):
  context = {
    'segment': 'terms'
  }
  return render(request, 'pages/terms.html', context)

def about(request):
  context = {
    'segment': 'about'
  }
  return render(request, 'pages/about.html', context)