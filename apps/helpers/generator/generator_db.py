# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, sys,wget, zipfile

from .common         import *
from .helpers        import *
from .cli            import *
from .parser_common  import *
from .parser_json    import *
from .parser_deps    import *

def customize_db( SRC_DIR, JSON_DATA ):

    db_driver = JSON_DATA['db']['driver']

    # nothing to do here
    if db_driver == 'mysql':
        deps_add( SRC_DIR, 'mysqlclient', '2.2.4') 
    
    if db_driver == 'pgsql':
        deps_add( SRC_DIR, 'psycopg2', '2.9.9')

    return COMMON.OK
