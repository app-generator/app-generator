# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from django.apps import apps
from django.contrib import admin

# Register your models here.

app_models = apps.get_app_config('home').get_models()
for model in app_models:
    try:    

        # Special processing for UserProfile
        if 'UserProfile' == model.__name__:

            # The model is registered only if has specific data
            # 1 -> ID
            # 2 -> User (one-to-one) relation 
            if len( model._meta.fields ) > 2:
                admin.site.register(model)
        
        # Register to Admin 
        else:
            admin.site.register(model)

    except Exception:
        pass
