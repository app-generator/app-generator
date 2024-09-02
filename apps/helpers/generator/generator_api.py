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
def load_api_gen_drf():

    TMPL_FILE = os.path.join( DIR_TMPL, 'api-gen-drf.tmpl')

    # as string    
    file_c = file_read( TMPL_FILE )
    # print( file_c )
    return file_c

# Template loader
def load_api_gen_settings():

    TMPL_FILE = os.path.join( DIR_TMPL, 'api-gen-settings.tmpl')
    
    # as list
    file_c = file_load( TMPL_FILE, True ) 
    # print( file_c )
    return file_c

def api_gen_add_rules( SRC_DIR, aDict ):

    MARKER             = '__RULES__'
    retCode, API_RULES = parse_api_generator( aDict ) # input is JSON

    if COMMON.OK != retCode:
        print( ' > ERR, parse_api_generator( ) failed' )
        return COMMON.ERR

    # load as list
    settings_c = load_api_gen_settings() # template loader

    if not settings_c:
        print( ' > ERR, load_api_gen_settings( ) failed' )
        return COMMON.ERR
    
    file_c = []

    
    MARKER_BEGIN = '#' + MARKER
    MARKER_END   = '#' + MARKER + 'END'
    processing   = False 

    for line in settings_c:

        if processing:

            if MARKER_END in line:

                processing = False
                file_c.append( COMMON.TAB + MARKER_END )

            continue 

        else:

            if MARKER_BEGIN in line:

                processing = True 

                added_content  = ''
                added_content += COMMON.TAB + MARKER_BEGIN + '\n'

                # Explode API Rules
                for api_path in API_RULES:
                    api_model = API_RULES[ api_path ]

                    # 'books'  : "app1.models.Book",

                    added_content += COMMON.TAB + "'{}' : '{}',".format(api_path, api_model) + '\n'

                file_c.append( added_content )

            else:

                file_c.append( line )                      

    return list_to_s( file_c, '\n' )

# Template saver
def save_api_settings( SRC_DIR, aContent ):

    MARKER   = '__API_GENERATOR__'

    # Use project prefix 
    FILE_DJ_SETTINGS = os.path.join( SRC_DIR, FILE_DJ_SETTINGS_s )

    retcode, content = cfg_load( FILE_DJ_SETTINGS )

    if COMMON.OK != retcode:
        print( ' > ERR, cfg_load( FILE_DJ_SETTINGS ) failed' )
        return retcode
    
    file_c = []

    MARKER_BEGIN = '# ' + MARKER         # Extra space because of 'Black' Formatter
    MARKER_END   = '# ' + MARKER + 'END' # Extra space because of 'Black' Formatter 
    processing   = False 

    for line in content:

        if processing:

            if MARKER_END in line:
                processing = False
                file_c.append( MARKER_END )

            continue 

        else:

            if MARKER_BEGIN in line:

                processing = True 

                added_content  = ''
                added_content += MARKER_BEGIN + '\n'
                added_content += aContent           

                file_c.append( added_content )

            else:

                file_c.append( line )                      

    return cfg_save( FILE_DJ_SETTINGS, file_c )

def api_gen_sources( SRC_DIR, aDict ):

    api_gen_drf_settings = load_api_gen_drf()
    api_gen_rules        = api_gen_add_rules( SRC_DIR, aDict )

    aContent  = ''
    aContent += api_gen_rules 
    aContent += '\n' 
    aContent += api_gen_drf_settings

    save_api_settings( SRC_DIR, aContent )

    # Add the new routing
    urls_add_rule( SRC_DIR, "path('login/jwt/', view=obtain_auth_token)" )

def api_gen_script( SRC_DIR ):

    # Use project prefix 
    FILE_CI_BUILD = os.path.join( SRC_DIR, FILE_CI_BUILD_s )

    # as list
    content = file_load( FILE_CI_BUILD, True ) 
    
    MARKER   = '__API_GENERATOR__'

    file_c = []

    MARKER_BEGIN = '#' + MARKER         
    MARKER_END   = '#' + MARKER + 'END'
    processing   = False 

    for line in content:

        if processing:

            if MARKER_END in line:
                processing = False
                file_c.append( MARKER_END )

            continue 

        else:

            if MARKER_BEGIN in line:

                processing = True 

                added_content  = ''
                added_content += MARKER_BEGIN + '\n'
                added_content += 'python manage.py generate-api -f'           

                file_c.append( added_content )

            else:

                file_c.append( line )                      

    return cfg_save( FILE_CI_BUILD, file_c )

def api_gen_docker( SRC_DIR ):

    # Use project prefix 
    FILE_DOCKER = os.path.join( SRC_DIR, FILE_DOCKER_s )

    # as list
    content = file_load( FILE_DOCKER, True ) 
    
    MARKER   = '__API_GENERATOR__'

    file_c = []

    MARKER_BEGIN = '#' + MARKER         
    MARKER_END   = '#' + MARKER + 'END'
    processing   = False 

    for line in content:

        if processing:

            if MARKER_END in line:
                processing = False
                file_c.append( MARKER_END )

            continue 

        else:

            if MARKER_BEGIN in line:

                processing = True 

                added_content  = ''
                added_content += MARKER_BEGIN + '\n'
                added_content += 'RUN python manage.py generate-api -f'           

                file_c.append( added_content )

            else:

                file_c.append( line )                      

    return cfg_save( FILE_DOCKER, file_c )

def api_gen_render( SRC_DIR, aTemplateFile ):

    # Use project prefix 
    FILE_RENDER = os.path.join( SRC_DIR, FILE_CI_RENDER_s )

    # as list
    content = file_load( FILE_RENDER ) 
    
    MARKER       = '__PROJECT_NAME__'
    project_name = aTemplateFile.split('_')[0] + '-django'

    content = content.replace(MARKER, project_name) 

    file_write(FILE_RENDER, content)
