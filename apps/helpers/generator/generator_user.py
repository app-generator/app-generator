# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import sys

from git import Repo, RemoteProgress
import wget, zipfile

from .common         import *
from .helpers        import *
from .cli            import *
from .parser_common  import *
from .parser_json    import *

def custom_user_save( SRC_DIR, aContent ):

    # Use project prefix 
    FILE_DJ_MODELS = os.path.join( SRC_DIR, FILE_DJ_MODELS_s )

    MARKER   = '__PROFILE_FIELDS__'

    retcode, content = cfg_load( FILE_DJ_MODELS )

    if COMMON.OK != retcode:
        print( ' > ERR, cfg_load( FILE_DJ_MODELS ) failed' )
        return retcode
    
    file_c = []

    MARKER_BEGIN = '#' + MARKER
    MARKER_END   = '#' + MARKER + 'END'
    processing   = False 

    for line in content:

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
                added_content += aContent           

                file_c.append( added_content )

            else:

                file_c.append( line )                      

    return cfg_save( FILE_DJ_MODELS, file_c )

def custom_user_gen( SRC_DIR, aDict ):

    retCode, data = parse_custom_user( aDict )
    
    if COMMON.OK != retCode:
        print( ' > ERR, parse_custom_user() failed' )
        return retCode

    custom_user_c = ''

    for f_name in data:
        
        f_type = data[ f_name ]

        if COMMON.TYPE_STRING == f_type:

            custom_user_c += COMMON.TAB + f_name.lower() + ' = models.CharField(max_length=255, null=True, blank=True)' + '\n'

        elif COMMON.TYPE_TEXT == f_type:

            custom_user_c += COMMON.TAB + f_name.lower() + ' = models.TextField(max_length=255, null=True, blank=True)' + '\n'
 
        elif COMMON.TYPE_INT == f_type:

            custom_user_c += COMMON.TAB + f_name.lower() + ' = models.IntegerField(null=True, blank=True)' + '\n'  

        else:    
            # unsupported
            print( ' > WARN: unsupported ['+f_type+'] (ignored)' )

    return custom_user_save( SRC_DIR, custom_user_c )
