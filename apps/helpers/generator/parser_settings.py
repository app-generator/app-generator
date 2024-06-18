# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from .common        import *
from .helpers       import *
from .cli           import *
from .parser_common import *

def settings_load( SRC_DIR ):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( SRC_DIR, FILE_DJ_SETTINGS_s )

    return cfg_load( FILE_DJ_SETTINGS )

def settings_imports( SRC_DIR ):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( SRC_DIR, FILE_DJ_SETTINGS_s )

    return cfg_imports( FILE_DJ_SETTINGS )

def settings_sections( SRC_DIR ):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( SRC_DIR, FILE_DJ_SETTINGS_s )

    return cfg_sections( FILE_DJ_SETTINGS )

def settings_var_upd( SRC_DIR, aVarName, aVarValue):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( SRC_DIR, FILE_DJ_SETTINGS_s )

    return cfg_var_upd( FILE_DJ_SETTINGS, aVarName, aVarValue )

def settings_var_upd_bool( SRC_DIR, aVarName, aVarValue):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( SRC_DIR, FILE_DJ_SETTINGS_s )

    return cfg_var_upd( FILE_DJ_SETTINGS, aVarName, aVarValue, True )

def settings_var_print( SRC_DIR, aVarName ):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( SRC_DIR, FILE_DJ_SETTINGS_s )

    return cfg_var_print( FILE_DJ_SETTINGS, aVarName )

def settings_section_get( SRC_DIR, aSectionName ):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( SRC_DIR, FILE_DJ_SETTINGS_s )

    return cfg_section_get( FILE_DJ_SETTINGS, aSectionName )

def settings_section_update( SRC_DIR, aSectionName, aSectionContent ):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( SRC_DIR, FILE_DJ_SETTINGS_s )

    return cfg_section_update( FILE_DJ_SETTINGS, aSectionName, aSectionContent)

def settings_apps_list( SRC_DIR ):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( SRC_DIR, FILE_DJ_SETTINGS_s )

    return cfg_section_list( FILE_DJ_SETTINGS, 'INSTALLED_APPS')

def settings_apps_add( SRC_DIR, aNewApp, aPos=COMMON.POS_END ):

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( SRC_DIR, FILE_DJ_SETTINGS_s )
    
    if COMMON.POS_END == aPos:
        cfg_section_add_item( FILE_DJ_SETTINGS, 'INSTALLED_APPS', aNewApp )
    else: 
        cfg_section_add_item_first( FILE_DJ_SETTINGS, 'INSTALLED_APPS', aNewApp )
