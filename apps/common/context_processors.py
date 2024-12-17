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


def price_subscription_pro(request):
    return {
        'price_subscription_pro': getattr(settings, 'PRO_SUBSCRIPTION_PRICE')
    }

def price_subscription_company(request):
    return {
        'price_subscription_company': getattr(settings, 'PRO_SUBSCRIPTION_COMPANY_PRICE')
    }

def price_cust_dev_week(request):
    return {
        'price_cust_dev_week': getattr(settings, 'CUST_DEV_WEEK_PRICE')
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