# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, random, string
from github import Github

from .common   import *
from .helpers  import *

def repo_create( SRC_DIR, GH_TOKEN, GH_REPOSITORY=None ):

    files = list_files( SRC_DIR )

    if not GH_TOKEN:
        print(' > GH Credentials not found, exit')
        return None

    # Check input
    if not GH_REPOSITORY:
        GH_REPOSITORY = 'appseed-generated-' + h_random_ascii(5)

    g = Github( GH_TOKEN )
    user = g.get_user()
    repo = user.create_repo( GH_REPOSITORY, description='Generated Starter | App-Generator.dev ' )

    print( '*** Create GIT Repo = ' + GH_REPOSITORY + ', user: ' + str(user) ) 

    idx = 1
    for f in files:

        # Report Status
        if idx % 10 == 0:

            task_completion = int( ( idx * 100 ) / len( files ) )
            print( '  >>> uploaded [' + str(task_completion) + '%] - ' + str( len ( files) ) + ' files (total)' )

        idx += 1

        # Fix for Windows     
        f_name = f.replace( SRC_DIR, '' ).replace('\\', '/') 
        f      = f.replace('\\', '/')

        #print( '*** > ['+str( idx )+'] ' + f_name + ' -> [content]: ' + f )

        repo.create_file( f_name, "initial commit", file_load( f ) )

    print( '  ...done' ) 
    return GH_REPOSITORY
