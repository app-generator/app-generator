from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

# LOGGER 
from inspect import currentframe
from util.logger import *

def index(request):

  # Logger
  func_name  = sys._getframe().f_code.co_name 
  logger( f'[{__name__}->{func_name}(), L:{currentframe().f_lineno}] ' + 'Begin' )

  return render(request, 'pages/home.html')

def support(request):

  # Logger
  func_name  = sys._getframe().f_code.co_name 
  logger( f'[{__name__}->{func_name}(), L:{currentframe().f_lineno}] ' + 'Begin' )

  context = {
    'segment': 'support'
  }
  return render(request, 'pages/support.html', context)

def custom_development(request):

  # Logger
  func_name  = sys._getframe().f_code.co_name 
  logger( f'[{__name__}->{func_name}(), L:{currentframe().f_lineno}] ' + 'Begin' )

  context = {
    'segment': 'custom_development'
  }
  return render(request, 'pages/custom-development.html', context)

def terms(request):

  # Logger
  func_name  = sys._getframe().f_code.co_name 
  logger( f'[{__name__}->{func_name}(), L:{currentframe().f_lineno}] ' + 'Begin' )

  context = {
    'segment': 'terms'
  }
  return render(request, 'pages/terms.html', context)

def about(request):

  # Logger
  func_name  = sys._getframe().f_code.co_name 
  logger( f'[{__name__}->{func_name}(), L:{currentframe().f_lineno}] ' + 'Begin' )

  context = {
    'segment': 'about'
  }
  return render(request, 'pages/about.html', context)