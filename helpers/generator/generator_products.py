# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import sys, os

from git import Repo, RemoteProgress
import wget, zipfile

from .common           import *
from .helpers          import *
from .parser_common    import *
from .parser_apps      import *
from .parser_deps      import *
from .parser_env       import *
from .parser_settings  import *
from .parser_urls      import *
from .generator        import *

# dashboards
def product_volt( SRC_DIR ):
    deps_add         (SRC_DIR, 'django-admin-volt')
    settings_apps_add(SRC_DIR, 'admin_volt.apps.AdminVoltConfig', COMMON.POS_FIRST)
    urls_add_rule    (SRC_DIR,  "path('', include('admin_volt.urls'))" )
    
def product_soft( SRC_DIR ):
    deps_add         (SRC_DIR, 'django-admin-soft-dashboard')
    settings_apps_add(SRC_DIR, 'admin_soft.apps.AdminSoftDashboardConfig', COMMON.POS_FIRST)
    urls_add_rule    (SRC_DIR,  "path('', include('admin_soft.urls'))" )

def product_material( SRC_DIR ):
    deps_add         (SRC_DIR, 'django-admin-material-dashboard')
    settings_apps_add(SRC_DIR, 'admin_material.apps.AdminMaterialDashboardConfig', COMMON.POS_FIRST)
    urls_add_rule    (SRC_DIR,  "path('', include('admin_material.urls'))" )

def product_argon( SRC_DIR ):
    deps_add         (SRC_DIR, 'django-admin-argon-dashboard')
    settings_apps_add(SRC_DIR, 'admin_argon.apps.AdminArgonConfig', COMMON.POS_FIRST)
    urls_add_rule    (SRC_DIR,  "path('', include('admin_argon.urls'))" )

def product_corporate( SRC_DIR ):
    deps_add         (SRC_DIR, 'django-admin-corporate')
    settings_apps_add(SRC_DIR, 'admin_corporate.apps.AdminCorporateConfig', COMMON.POS_FIRST)
    urls_add_rule    (SRC_DIR,  "path('', include('admin_corporate.urls'))" )

def product_datta( SRC_DIR ):
    deps_add         (SRC_DIR, 'django-admin-datta')
    settings_apps_add(SRC_DIR, 'admin_datta.apps.AdminDattaConfig', COMMON.POS_FIRST)
    urls_add_rule    (SRC_DIR,  "path('', include('admin_datta.urls'))" )

def product_adminlte( SRC_DIR ):
    deps_add         (SRC_DIR, 'django-admin-adminlte')
    settings_apps_add(SRC_DIR, 'admin_adminlte.apps.AdminAdminlteConfig', COMMON.POS_FIRST)
    urls_add_rule    (SRC_DIR,  "path('', include('admin_adminlte.urls'))" )

def product_tabler( SRC_DIR ):
    deps_add         (SRC_DIR, 'django-admin-tabler')
    settings_apps_add(SRC_DIR, 'admin_tabler.apps.AdminTablerConfig', COMMON.POS_FIRST)
    urls_add_rule    (SRC_DIR,  "path('', include('admin_tabler.urls'))" )
    
def product_berry( SRC_DIR ):
    deps_add         (SRC_DIR, 'django-admin-berry')
    settings_apps_add(SRC_DIR, 'admin_berry.apps.AdminBerryConfig', COMMON.POS_FIRST)
    urls_add_rule    (SRC_DIR,  "path('', include('admin_berry.urls'))" )

def product_black( SRC_DIR ):
    deps_add         (SRC_DIR, 'django-admin-black')
    settings_apps_add(SRC_DIR, 'admin_black.apps.AdminBlackConfig', COMMON.POS_FIRST)
    urls_add_rule    (SRC_DIR, "path('', include('admin_black.urls'))" )

def product_modernize( SRC_DIR ):
    deps_add         (SRC_DIR, 'django-admin-modernize')
    settings_apps_add(SRC_DIR, 'admin_modernize.apps.AdminModernizeConfig', COMMON.POS_FIRST)
    urls_add_rule    (SRC_DIR, "path('', include('admin_modernize.urls'))" )

def product_gradient( SRC_DIR ):
    deps_add         (SRC_DIR, 'django-admin-gradient')
    settings_apps_add(SRC_DIR, 'admin_gradient.apps.AdminGradientConfig', COMMON.POS_FIRST)
    urls_add_rule    (SRC_DIR, "path('', include('admin_gradient.urls'))" )

# themes 
def product_pixel( SRC_DIR ):
    deps_add         (SRC_DIR, 'django-theme-pixel')
    settings_apps_add(SRC_DIR, 'theme_pixel')
    urls_add_rule    (SRC_DIR, "path('', include('theme_pixel.urls'))" )

def product_soft_kit( SRC_DIR ):
    deps_add         (SRC_DIR, 'django-theme-soft-design')
    settings_apps_add(SRC_DIR, 'theme_soft_design')
    urls_add_rule    (SRC_DIR, "path('', include('theme_soft_design.urls'))" )

def product_material_kit( SRC_DIR ):
    deps_add         (SRC_DIR, 'django-theme-material-kit')
    settings_apps_add(SRC_DIR, 'theme_material_kit')
    urls_add_rule    (SRC_DIR, "path('', include('theme_material_kit.urls'))" )
