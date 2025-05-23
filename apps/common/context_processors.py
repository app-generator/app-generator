from apps.common.models import Profile, RoleChoices, Props
from django.conf import settings
from datetime import datetime

def profile_context(request):
    is_company = False
    # request might don't have a user object
    #if request.user.is_authenticated:
    #    is_company = Profile.objects.filter(user=request.user, role=RoleChoices.COMPANY).exists()
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

def price_cust_dev_hour(request):
    return {
        'price_cust_dev_hour': getattr(settings, 'CUST_DEV_HOUR_PRICE')
    }

def price_onboarding_kit(request):
    return {
        'price_onboarding_kit': getattr(settings, 'ONBOARDING_KIT_PRICE')
    }

def price_bundle(request):
    return {
        'price_bundle': getattr(settings, 'BUNDLE_PRICE')
    }

def price_bundle2(request):
    return {
        'price_bundle2': getattr(settings, 'BUNDLE_PRICE2')
    }

def props_context(request):

    props = {}

    try: 
        props = {prop.category: prop.data for prop in Props.objects.all()}

        promo_end_date_str = props.get('PROMO_END_DATE')
        if promo_end_date_str:
            try:
                promo_end_date = datetime.strptime(promo_end_date_str, "%Y-%m-%d")
                props['PROMO_END_DATE'] = promo_end_date
            except ValueError:
                pass
    except:
        props = {}

    return {
        'props': props
    }


def google_tag(request):
    tag = getattr(settings, 'GOOGLE_TAG', None)
    return { 'google_tag': tag }