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

def reset_sources( aDest ):

    print(' > Copy Sources ...')

    DIR_SRC = os.path.join(DIR_ROOT, 'sources', 'django')

    dir_copy( DIR_SRC, aDest)

    print( '  ...done' ) 

def reset_sources_zip( aDest ):

    print(' > Reset Sources ...')

    ZIP_FILE = 'src.zip'

    with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
        zip_ref.extractall( aDest )
    
    print( '  ...done' ) 
        
def project_dw():

    if file_exists( FILE_DJ_MANAGE ):
        print('ERR: project exists, please delete first (runner.py delete)' )
        sys.exit(1)  
    
    ZIP_URL  = 'https://github.com/app-generator/core-django/archive/refs/heads/main.zip'
    ZIP_FILE = 'core-django-main.zip'

    DIR_TMP  = 'src_tmp'
    DIR_SRC  = os.path.join(DIR_TMP, 'core-django-main')
    DIR_DEST = 'src'

    wget.download(ZIP_URL)

    with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
        zip_ref.extractall( DIR_TMP )
    
    dir_copy( DIR_SRC, DIR_DEST)

    # CleanUP 
    dir_delete( DIR_TMP )
    os.remove ( ZIP_FILE )

    os.chdir( DIR_DEST )

    # Migrate db
    result = exec_cmd( 'python manage.py migrate' )

    if COMMON.OK != result:
        print('ERR: migrate DB')
        sys.exit(1)  

    print(os.linesep)
    print(' > Project Created (DW Zip)')

def project_clone():

    if file_exists( FILE_DJ_MANAGE ):
        print('ERR: project exists, please delete first (runner.py delete)' )
        sys.exit(1)  

    Repo.clone_from('https://github.com/app-generator/core-django.git', 'src', progress=CloneProgress())

    os.chdir( DIR_SRC )

    # Migrate db
    result = exec_cmd( 'python manage.py migrate' )

    if COMMON.OK != result:
        print('ERR: migrate DB ')
        sys.exit(1)  

    print(os.linesep)
    print(' > Project Created (GIT Clone)')

def project_create():

    if file_exists( FILE_DJ_MANAGE ):
        print('ERR: project exists, please delete first (runner.py delete)' )
        sys.exit(1)  

    if not dir_exists( 'src' ):
        dir_create( 'src' )

    os.chdir( DIR_SRC )

    # Create project (SRC folder)
    result = exec_cmd( 'django-admin startproject core .' )

    if COMMON.OK != result:
        print('ERR: creating project ')
        sys.exit(1)

    # Migrate db
    result = exec_cmd( 'python manage.py migrate' )

    if COMMON.OK != result:
        print('ERR: migrate DB')
        sys.exit(1)        

    print(os.linesep)
    print(' > Project Created (Django-Admin)')

def project_start():

    if not file_exists( FILE_DJ_MANAGE ):
        print(' Err: project not created, (execute runner.py create)')
        sys.exit(1)        

    os.chdir( DIR_SRC )

    # Install Dependencies
    result = exec_cmd( 'pip install -r requirements.txt' )

    if COMMON.OK != result:
        print('ERR: install deps ')
        sys.exit(1)        

    # Migrate db
    result = exec_cmd( 'python manage.py migrate' )

    if COMMON.OK != result:
        print('ERR: migrate DB: ')
        sys.exit(1)        

    # Start project
    result = exec_cmd( 'python manage.py runserver ' )

    if COMMON.OK != result:
        print('ERR: start the project')
        sys.exit(1)

    print(os.linesep)
    print(' > Project Started')

def project_create_app( appName ):

    #print( 'Create app: ' + appName )
    
    APP_DIR = os.path.join(DIR_SRC, appName )

    # Check app exists
    if dir_exists( APP_DIR ):
        print('ERR: app already exists')
        sys.exit(1)        

    os.chdir( DIR_SRC )

    # Create project (SRC folder)
    result = exec_cmd( 'django-admin startapp ' + appName )

    if COMMON.OK != result:
        print('ERR: creating app: ' + stderr)
        sys.exit(1)

    # Update settings
    retcode, section_content = settings_apps_add( appName )

    if COMMON.OK != result:
        print('ERR updating configuration ')
        sys.exit(1) 

    print(os.linesep)
    print(' > App [' + appName + '] CREATED')

def project_delete_app( appName ):

    #print( 'Create app: ' + appName )
    
    APP_DIR = os.path.join(DIR_SRC, appName )

    # Check app exists
    if not dir_exists( APP_DIR ):
        print('ERR: app not defined: ' + appName)
        sys.exit(1)

    dir_delete( APP_DIR )

    print(os.linesep)
    print(' > App [' + appName + '] DELETED')

