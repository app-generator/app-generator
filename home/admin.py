from django.contrib import admin
from django.apps import apps


for app in apps.get_app_config('home').get_models():
    try:
        admin.site.register(app)
    except admin.sites.AlreadyRegistered:
        pass
