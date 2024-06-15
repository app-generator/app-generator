# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
#from decouple import config

NODE_12="12.0.0"
NODE_14="14.0.0"
NODE_16="16.10.0"
NODE_18="18.0.0"

# Render authentication API
DEBUG = False

# Render authentication API
RENDER_BUILDER = 'yarn'

DEPLOY_READY = False

# Render authentication API
RENDER_API_KEY = None #config('RENDER_API_KEY' , None)

# Render authentication API
RENDER_OWNER_ID = None #config('RENDER_OWNER_ID', None)

if RENDER_API_KEY and RENDER_OWNER_ID:
    DEPLOY_READY = True

# Entry points 
ENTRY_POINT_DJANGO     = 'core.wsgi:application' # AppSeed specific
ENTRY_POINT_FLASK      = 'run:app'               # AppSeed specific 
ENTRY_POINT_NODEJS     = 'build/index.js'        # AppSeed specific 
ENTRY_POINT_NODEJS_APP = 'app.js'

# api header
HEADERS = {
    'accept': 'application/json',
    'authorization': f'Bearer {RENDER_API_KEY}',
}

# api url
URL="https://api.render.com"
