# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from .common  import *
from .helpers import *
from .cli     import *

def app_list_files(SRC_DIR, appName ):
    
    # check app exists 
    APP_DIR = os.path.join(SRC_DIR, appName )

    # Check app exists
    if not dir_exists( APP_DIR ):
        print('ERR: ' + appName+ ' is not created')
        return None   

    # list `py` files
    return list_files( APP_DIR, 'py' )

def app_list_models(SRC_DIR, appName ):
    pass

def app_get_model(SRC_DIR, modelName ):
    pass 
