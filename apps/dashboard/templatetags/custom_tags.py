import requests
import json
import os
from django import template
from apps.common.models_products import Download
from django.conf import settings
from django.template.loader import get_template
from django.template.exceptions import TemplateDoesNotExist
from django.contrib.auth import get_user_model
from apps.common.models import FileInfo
from apps.common.models_products import Products
from helpers.util import h_label

User = get_user_model()

register = template.Library()


@register.filter
def check_new_version(download_id):
    download = Download.objects.get(pk=download_id)

    if download.product.release_date and download.downloaded_at:
        if download.product.release_date > download.downloaded_at.date():
            return True
    
    return False


@register.filter
def product_details(product_id):
    url = f"https://api.gumroad.com/v2/products/{product_id}"
    params = {
        "access_token": getattr(settings, 'GUMROAD_ACCESS_TOKEN'),
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        json_response = response.json()

        print(json.dumps(json_response, indent=4))
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


@register.filter
def template_exists(template_name):
    try:
        get_template(template_name)
        return True
    except TemplateDoesNotExist:
        return False

@register.filter
def label(aLabel):
    return h_label(aLabel)

@register.filter
def total_downloads(product):
    return Download.objects.filter(product=product).count()

@register.filter
def username_by_id(id):
    user = User.objects.filter(pk=id).first()
    if user:
        return user.username
    else:
        return 'Guest'
    
@register.filter
def pretty_json(value):
    try:
        parsed = json.loads(value) if isinstance(value, str) else value
        return json.dumps(parsed, indent=4)
    except (json.JSONDecodeError, TypeError):
        return value


@register.filter
def file_extension(value):
    _, extension = os.path.splitext(value)
    return extension.lower()


@register.filter
def encoded_file_path(path):
    return path.replace('/', '%slash%')

@register.filter
def encoded_path(path):
    return path.replace('\\', '/')


@register.filter
def info_value(path):
    file_info = FileInfo.objects.filter(path=path)
    if file_info.exists():
        return file_info.first().info
    else:
        return ""
    
@register.filter
def h_product_card(aProdCanonical):
    
    product = Products.objects.filter(canonical=aProdCanonical).first()

    if not product:
        return '' #f"aProdCanonical '{aProdCanonical}' not found in DB"
    
    prod_card = f'''
                <div class="md:col-span-1 col-span-2 mb-5">
                  <div class="relative bg-white shadow-lg rounded-lg group mb-5">
                      <img src="/static/{ product.canonical }top.png" alt="{ product.seo_description }" class="rounded-lg">
                      <div class="absolute inset-0 bg-black bg-opacity-50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg"></div>
                      <button 
                          class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                          <a href="{ product.url_demo }" target="_blank" class="px-4 py-2 bg-white text-gray-900 font-medium rounded ">
                              Demo
                          </a>
                      </button>
                  </div>
                  <div class="px-3">
                      <div class="flex justify-between items-center">
                          <h2 class="text-xl text-black font-medium">
                            <a href="/{ product.canonical }">{ product.name }</a>
                          </h2>
                          <p class="text-gray-700">
                              <strike><span class="text-blue-600">${ product.price }</span></strike>
                          </p>
                      </div>
                      <p class="text-gray-700">
                          { product.card_info } 
                      </p>
                  </div>
                </div>
    '''
    return prod_card
