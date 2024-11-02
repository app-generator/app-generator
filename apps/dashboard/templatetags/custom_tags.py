import requests
import json
from django import template
from apps.common.models_products import Download
from django.conf import settings
from django.template.loader import get_template
from django.template.exceptions import TemplateDoesNotExist


register = template.Library()


@register.filter
def check_new_version(download_id):
    download = Download.objects.get(pk=download_id)
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