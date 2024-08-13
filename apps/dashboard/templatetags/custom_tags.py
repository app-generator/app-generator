from django import template
from apps.common.models_products import Download

register = template.Library()


@register.filter
def check_new_version(download_id):
    download = Download.objects.get(pk=download_id)
    if download.product.release_date > download.downloaded_at.date():
        return True
    
    return False