# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, sys, wget, zipfile

from .common         import *
from .helpers        import *
from .cli            import *
from .parser_common  import *
from .parser_json    import *
from .parser_deps    import *

def api_gen_outh_github( SRC_DIR, aGenerate=False ):

    MARKER   = '__OAUTH_GITHUB__'

    FILE_DJ_SETTINGS          = os.path.join( SRC_DIR , FILE_DJ_SETTINGS_s    )
    FILE_GITHUB_SETTINGS_TMPL = os.path.join( DIR_TMPL, 'outh-github.tmpl')

    FILE_README               = os.path.join( SRC_DIR , FILE_README_s      )
    FILE_GITHUB_HELP_TMPL     = os.path.join( DIR_TMPL, 'outh-github-help.tmpl' )

    if not aGenerate:

        # Delete Marker 
        content  = file_load( FILE_README ) 
        template = file_load( FILE_GITHUB_HELP_TMPL )
        content = content.replace(MARKER, '') 
        file_write(FILE_README, content) 

        return COMMON.OK        

    # (1) Update Settings 
    content  = file_load( FILE_DJ_SETTINGS ) 
    template = MARKER + '\n' + file_load( FILE_GITHUB_SETTINGS_TMPL )
    content = content.replace(MARKER, template) 
    file_write(FILE_DJ_SETTINGS, content) 

    # (2) Update README 
    content  = file_load( FILE_README )
    template = file_load( FILE_GITHUB_HELP_TMPL )
    content = content.replace(MARKER, template) 
    file_write(FILE_README, content) 

    return COMMON.OK
