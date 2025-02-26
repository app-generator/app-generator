# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import sys

from git import Repo, RemoteProgress
import wget, zipfile

import pdb;

from .common         import *
from .helpers        import *
from .cli            import *
from .parser_common  import *
from .parser_json    import *
from .parser_urls    import *

# Template loader
def load_dyn_dt_settings():

    TMPL_FILE = os.path.join( DIR_TMPL_FLASK, 'dyn-dt-settings.tmpl')
    
    # as list
    file_c = file_load( TMPL_FILE, True ) 

    # print( file_c )
    return file_c

def dyn_dt_add_rules( SRC_DIR, aDict ):

    MARKER            = '__RULES__'
    retCode, DT_RULES = parse_dyn_dt( aDict ) # input is JSON

    if COMMON.OK != retCode:
        print( ' > ERR, parse_dyn_dt( ) failed' )
        return COMMON.ERR

    # load as list
    settings_c = load_dyn_dt_settings() # template loader

    if not settings_c:
        print( ' > ERR, load_dyn_dt_settings( ) failed' )
        return COMMON.ERR
    
    file_c = []
    
    MARKER_BEGIN = '#' + MARKER
    MARKER_END   = '#' + MARKER + 'END'
    processing   = False 

    for line in settings_c:

        if processing:

            if MARKER_END in line:

                processing = False
                file_c.append( COMMON.TAB2 + MARKER_END )

            continue 

        else:

            if MARKER_BEGIN in line:

                processing = True 

                added_content  = ''
                added_content += COMMON.TAB2 + MARKER_BEGIN + '\n'

                # Explode API Rules
                for a_path in DT_RULES:

                    a_model = DT_RULES[ a_path ]

                    # 'books'  : "app1.models.Book",

                    added_content += COMMON.TAB2 + "'{}' : '{}',".format(a_path, a_model) + '\n'

                file_c.append( added_content )

            else:

                file_c.append( line )                      

    return list_to_s( file_c, '\n' )

# Template saver
def save_dyn_dt_settings( SRC_DIR, aContent ):

    print( 'save_dyn_dt_settings() - Begin' )

    MARKER   = '__DYNAMIC_DATATB__'

    # Use project prefix 
    FILE_FL_CONFIG = os.path.join( SRC_DIR, FILE_FL_CONFIG_s )

    retcode, content = cfg_load( FILE_FL_CONFIG )

    if COMMON.OK != retcode:
        print( ' > ERR, cfg_load( FILE_FL_CONFIG ) failed' )
        return retcode
    
    file_c = []

    MARKER_BEGIN = '# ' + MARKER         # Extra space because of 'Black' Formatter
    MARKER_END   = '# ' + MARKER + 'END' # Extra space because of 'Black' Formatter 
    processing   = False 

    for line in content:

        #print( '> LINE: ' + line )

        if processing:

            if MARKER_END in line:
                processing = False
                #file_c.append( MARKER_END )
                #print( ' ------> ADD Marker END ' + MARKER_END )    

            continue 

        else:

            if MARKER_BEGIN in line:

                #print( ' ------> Marker Detected ' + MARKER_BEGIN )    

                processing = True 

                added_content  = ''
                #added_content += MARKER_BEGIN + '\n'
                added_content += aContent           

                #print( ' ------> Added CONTENT ') 
                #print( MARKER_BEGIN ) 

                file_c.append( added_content )

            else:

                file_c.append( line )                      

    return cfg_save( FILE_FL_CONFIG, file_c )

def dyn_dt_sources( SRC_DIR, aDict ):

    print( 'dyn_dt_sources() - Begin' ) 

    dyn_dt_rules = dyn_dt_add_rules( SRC_DIR, aDict )

    aContent  = ''
    aContent += dyn_dt_rules

    print( aContent ) 

    save_dyn_dt_settings( SRC_DIR, aContent )
