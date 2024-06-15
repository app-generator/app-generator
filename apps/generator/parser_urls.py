# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from .common        import *
from .helpers       import *
from .cli           import *
from .parser_common import *

def urls_load( SRC_DIR ):

    # Use project prefix 
    FILE_DJ_URLS = os.path.join( SRC_DIR, FILE_DJ_URLS_s )

    return cfg_load( FILE_DJ_URLS )

def urls_imports( SRC_DIR ):

    # Use project prefix 
    FILE_DJ_URLS = os.path.join( SRC_DIR, FILE_DJ_URLS_s )

    return cfg_imports( FILE_DJ_URLS )

def urls_sections( SRC_DIR ):

    # Use project prefix 
    FILE_DJ_URLS = os.path.join( SRC_DIR, FILE_DJ_URLS_s )

    return cfg_sections( FILE_DJ_URLS )

def urls_save( SRC_DIR, content ):

    # Use project prefix 
    FILE_DJ_URLS = os.path.join( SRC_DIR, FILE_DJ_URLS_s )

    return cfg_save( FILE_DJ_URLS, content )

def urls_format( SRC_DIR ):

    # Use project prefix 
    FILE_DJ_URLS = os.path.join( SRC_DIR, FILE_DJ_URLS_s )

    return cfg_format( FILE_DJ_URLS ) 

def urls_section_get( SRC_DIR ):

    # Use project prefix 
    FILE_DJ_URLS = os.path.join( SRC_DIR, FILE_DJ_URLS_s )

    return cfg_section_get( FILE_DJ_URLS, 'urlpatterns' )

def urls_list( SRC_DIR ):

    # Use project prefix 
    FILE_DJ_URLS = os.path.join( SRC_DIR, FILE_DJ_URLS_s )

    return cfg_section_list( FILE_DJ_URLS, 'urlpatterns' )

def urls_add_rule( SRC_DIR, aNewValue ):

    # Use project prefix 
    FILE_DJ_URLS = os.path.join( SRC_DIR, FILE_DJ_URLS_s )
    
    return cfg_section_add_item( FILE_DJ_URLS, 'urlpatterns', aNewValue, True )
