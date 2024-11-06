from apps.common.models import Profile, RoleChoices, Props
from django.conf import settings
from datetime import datetime

def profile_context(request):
    is_company = False
    if request.user.is_authenticated:
        is_company = Profile.objects.filter(user=request.user, role=RoleChoices.COMPANY).exists()
    return {'is_company': is_company}


def version_context(request):
    return {
        'version': getattr(settings, 'VERSION')
    }


def props_context(request):
    props = {prop.category: prop.data for prop in Props.objects.all()}

    promo_end_date_str = props.get('PROMO_END_DATE')
    if promo_end_date_str:
        try:
            promo_end_date = datetime.strptime(promo_end_date_str, "%Y-%m-%d")
            props['PROMO_END_DATE'] = promo_end_date
        except ValueError:
            pass

    return {
        'props': props
    }