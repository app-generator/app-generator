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

def api_gen_celery( SRC_DIR, aGenerate=True ):

    MARKER   = '__CELERY__'

    FILE_DJ_INIT              = os.path.join( SRC_DIR , FILE_DJ_INIT_s        )
    FILE_DJ_INIT_TMPL         = os.path.join( DIR_TMPL, 'celery-init.tmpl'    )
    FILE_DJ_SETTINGS          = os.path.join( SRC_DIR , FILE_DJ_SETTINGS_s    )
    FILE_CELERY_SETTINGS_TMPL = os.path.join( DIR_TMPL, 'celery-settings.tmpl')

    FILE_CELERY_CORE_TMPL   = os.path.join( DIR_TMPL, 'celery_core.tmpl' )
    FILE_CELERY_TASKS_TMPL  = os.path.join( DIR_TMPL, 'celery-tasks.tmpl')

    FILE_README             = os.path.join( SRC_DIR , FILE_README_s      )
    FILE_CELERY_HELP_TMPL   = os.path.join( DIR_TMPL, 'celery-help.tmpl' )

    # Remove README TAG
    if not aGenerate:
        content  = file_load( FILE_README ) 
        content = content.replace(MARKER, '') 
        file_write(FILE_README, content) 
        return COMMON.OK

    # (1) Add Deps 
    deps_add( SRC_DIR, 'celery', '5.3.4') 
    deps_add( SRC_DIR, 'redis', '5.0.1') 

    # (2) Update Settings 
    content  = file_load( FILE_DJ_SETTINGS ) 
    template = MARKER + '\n' + file_load( FILE_CELERY_SETTINGS_TMPL )
    content = content.replace(MARKER, template) 
    file_write(FILE_DJ_SETTINGS, content) 

    # (3) Edit Init 
    content  = file_load( FILE_DJ_INIT ) 
    template = MARKER + '\n' + file_load( FILE_DJ_INIT_TMPL )
    content = content.replace(MARKER, template) 
    file_write(FILE_DJ_INIT, content) 

    # (4) Add Celery core 
    shutil.copy( FILE_CELERY_CORE_TMPL, os.path.join( SRC_DIR, FILE_CELERY_CORE_s ) )

    # (5) Add Tasks 
    shutil.copy( FILE_CELERY_TASKS_TMPL, os.path.join( SRC_DIR, FILE_CELERY_TASKS_s ) )

    # (6) Update README 
    content  = file_load( FILE_README ) 
    template = file_load( FILE_CELERY_HELP_TMPL )
    content = content.replace(MARKER, template) 
    file_write(FILE_README, content) 

    return COMMON.OK
