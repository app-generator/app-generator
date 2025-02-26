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

class CloneProgress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        if message:
            print(message)

def reset_sources( aDest, aSource='django' ):

    print(' > Copy Sources ...')

    DIR_SRC = os.path.join(DIR_ROOT, 'sources', aSource)
    
    # Delete if exist
    dir_delete( aDest )

    return dir_copy( DIR_SRC, aDest)

def reset_sources_zip( aDest ):

    print(' > Reset Sources ...')

    ZIP_FILE = 'src.zip'

    with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
        zip_ref.extractall( aDest )
    
    print( '  ...done' ) 

def update_readme(SRC_DIR, aDict):
    
    FILE_README = os.path.join( SRC_DIR , FILE_README_s      )
    content  = file_load( FILE_README )

    # replace content 
    for key in aDict.keys():
        content = content.replace(key, aDict[key]) 

    # save file 
    file_write(FILE_README, content) 

    return COMMON.OK

