from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from apps.common.models import Products, Profile

# Create your views here.

# LOGGER 
from inspect import currentframe
from helpers.logger import *

def index(request):

  # Logger
  func_name  = sys._getframe().f_code.co_name 
  logger( f'[{__name__}->{func_name}(), L:{currentframe().f_lineno}] ' + 'Begin' )
  products = Products.objects.all()
  context = {
    'segment'        : 'home',
    'page_title'     : 'Generate Code, AI-Tools, Deployment Automation, and Custom Development Services',
    'page_info'      : 'Modern tools for developers and Companies, Generated Digital Products (Dashboards, eCommerce, Websites)',
    'page_keywords'  : 'app generator, dashboards, web apps, generated products, custom development, ai tools, dev tools, tools for developers and companies',
    'page_canonical' : '',
    'products'        : products 
  }

  return render(request, 'pages/home.html', context)


def show_dashboard(request):
  products = Products.objects.all()
  products_list = list(products.values())
  return JsonResponse({'products': products_list})

def support(request):

  # Logger
  func_name  = sys._getframe().f_code.co_name 
  logger( f'[{__name__}->{func_name}(), L:{currentframe().f_lineno}] ' + 'Begin' )

  context = {
    'segment'        : 'support',
    'page_title'     : 'Premium Support via email (support@appseed.us) and Discord',
    'page_info'      : 'Get Support for Dashboards, eCommerce, Presentation Websites',
    'page_keywords'  : 'support, email support, Discord support, Tickets, app generator, dashboards, web apps, generated products, custom development',
    'page_canonical' : 'support/',
  }

  return render(request, 'pages/support.html', context)

def custom_development(request):

  # Logger
  func_name  = sys._getframe().f_code.co_name 
  logger( f'[{__name__}->{func_name}(), L:{currentframe().f_lineno}] ' + 'Begin' )

  context = {
    'segment'        : 'custom_development',
    'page_title'     : 'Custom Development - Need help Coding an MVP or a Complete Solution? ',
    'page_info'      : 'Get Custom Development Services from a team of experts.',
    'page_keywords'  : 'custom development, custom tools, custom generators, app generator, dashboards, web apps, generated products',
    'page_canonical' : 'custom-development/',
  }

  return render(request, 'pages/custom-development.html', context)

def terms(request):

  # Logger
  func_name  = sys._getframe().f_code.co_name 
  logger( f'[{__name__}->{func_name}(), L:{currentframe().f_lineno}] ' + 'Begin' )

  context = {
    'segment'        : 'terms',
    'page_title'     : 'Terms - Learn how to use the service ',
    'page_info'      : 'AppSee/App-generator Terms of Use',
    'page_keywords'  : 'terms, service terms, AppSeed terms, App-Generator Terms',
    'page_canonical' : 'terms/',
  }

  return render(request, 'pages/terms.html', context)

def about(request):

  # Logger
  func_name  = sys._getframe().f_code.co_name 
  logger( f'[{__name__}->{func_name}(), L:{currentframe().f_lineno}] ' + 'Begin' )

  context = {
    'segment'        : 'about',
    'page_title'     : 'About US - Learn more about the team and the mission ',
    'page_info'      : 'More inputs regarding AppSee/App-generator service',
    'page_keywords'  : 'about, about AppSeed, about App-Generator',
    'page_canonical' : 'about/',
  }

  return render(request, 'pages/about.html', context)


def user_profile(request, username):
  profile = get_object_or_404(Profile, user__username=username)
  context = {
    'profile': profile
  }
  return render(request, 'pages/profile.html', context)