import os, json, subprocess, time, shutil
from django.conf import settings
from datetime import datetime

from celery import shared_task
from celery.utils.log import get_task_logger
from core.celery import celery_app

from helpers import *
from .utils import *

logger = get_task_logger(__name__)

def log_to_file(task_name, task_path, log_message):
    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M')
    log_filename = os.path.join(task_path, 'logs', f'{timestamp}-{task_name}.log')
    with open(log_filename, 'a') as log_file:
        log_file.write(f'[{timestamp}] {log_message}\n')

# task used for tests
@celery_app.task(name="task_generator", bind=True)
def task_generator( self, task_input ):

    # ######################################################
    # Handle Task Input

    # Read input
    task_json = task_input

    logger.info( '*** START, using input: ' + str( task_json ) )

    # Get current task id
    task_id               = celery_app.current_task.request.id
    task_json['task_id']  = task_id
    task_ts_start         = h_ts_full()
    task_json['err_code'] = COMMON.ERR_NA

    # ######################################################
    # Validate Input

    input_backend      = task_json['backend']
    input_design       = task_json['design']
    input_name         = task_json['project_name']
    input_docker       = True  if ( task_json['deploy']['docker' ] == True     ) else False
    input_cicd         = True  if ( task_json['deploy']['ci_cd'  ] == True     ) else False
    input_live         = True  if ( task_json['deploy']['go_live'] == True     ) else False
    input_celery       = True  if ( task_json['tools']['celery'  ] == True     ) else False
    input_auth_github  = True  if ( task_json['auth']['github'   ] == True     ) else False
    input_db_mysql     = True  if ( task_json['db']['driver'     ] == 'mysql'  ) else False
    input_db_pgsql     = True  if ( task_json['db']['driver'     ] == 'pgsql'  ) else False
    
    input_api_gen = False 
    if 'api_generator' in task_json['tools']: 
        input_api_gen = True if ( len( task_json['tools']['api_generator'] ) > 0 ) else False

    logger.info( '*** Validate Input ')
    logger.info( '    |-- backend       : ' + str( input_backend.upper() ))
    logger.info( '    |-- design        : ' + str( input_design ))
    logger.info( '    |-- auth_github   : ' + str( input_auth_github ))
    logger.info( '    |-- db_mysql      : ' + str( input_db_mysql ))
    logger.info( '    |-- db_pgsql      : ' + str( input_db_pgsql ))
    logger.info( '    |-- docker        : ' + str( input_docker ))
    logger.info( '    |-- ci/cd         : ' + str( input_cicd ))
    logger.info( '    |-- go_live       : ' + str( input_live ))
    logger.info( '    |-- celery        : ' + str( input_celery ))
    logger.info( '    |-- api_generator : ' + str( input_api_gen ))

    # ######################################################
    # Create OUTPUT Directory
    SRC_DIR   = os.path.join(DIR_GEN_APPS, task_id)
    REPO_NAME = f"{input_backend}-{input_design}-{get_ts_unix()}"

    v_ret = dir_create( SRC_DIR )

    if COMMON.ERR == v_ret:
        update_task_json( task_json, COMMON.FINISHED, f"ERR Create output DIR: {SRC_DIR}", COMMON.FAILURE )
        task_json['err_code'] = COMMON.ERR_INPUT
        save_task_json( task_id, task_json)
        self.update_state( state=COMMON.FINISHED, meta=task_json )
        return task_json        

    logger.info( '*** TARGET DIR creation ' + str( SRC_DIR ) )

    # ######################################################
    # Task is STARTING (task set up)

    update_task_json( task_json, COMMON.STARTING, 'Task is starting', COMMON.SUCCESS )
    save_task_json( task_id, task_json)
    self.update_state( state=COMMON.STARTING, meta=task_json )

    logger.info( '*** GENERATE Code (DJANGO) - ' + SRC_DIR )

    reset_sources( SRC_DIR )

    if 'soft' == input_design :
        product_soft( SRC_DIR )
    elif 'argon' == input_design :
        product_argon( SRC_DIR )
    elif 'material' == input_design:
        product_material( SRC_DIR )        
    elif 'corporate' == input_design:
        product_corporate( SRC_DIR )          
    elif 'black' == input_design:
        product_black( SRC_DIR )          
    elif 'berry' == input_design:
        product_berry( SRC_DIR )          
    elif 'datta' == input_design:
        product_datta( SRC_DIR )          
    elif 'gradient' == input_design:
        product_gradient( SRC_DIR )          
    elif 'volt' == input_design:
        product_volt( SRC_DIR )
    elif 'adminlte' == input_design:
        product_adminlte( SRC_DIR )          
    elif 'tabler' == input_design:
        product_tabler( SRC_DIR )          

    ## KITs
    elif 'soft-kit' == input_design:
        product_soft_kit( SRC_DIR )
    elif 'material-kit' == input_design:
        product_material_kit( SRC_DIR )
    elif 'pixel' == input_design:
        product_pixel( SRC_DIR )

    else:
        update_task_json( task_json, COMMON.UNKNOWN_DESIGN, 'Unsupported Design: ' + input_design, COMMON.FAILURE )
        task_json['err_code'] = COMMON.ERR_INPUT
        save_task_json( task_id, task_json)
        self.update_state( state=COMMON.FINISHED, meta=task_json )
        return task_json     

    # DB Driver
    if input_db_mysql or input_db_pgsql: 
        retCode = customize_db( SRC_DIR, task_json ) 
        if COMMON.OK != retCode:
            update_task_json( task_json, COMMON.ERR_CUSTOMIZE_DB, 'Error customize DB Driver', COMMON.FAILURE )
            task_json['err_code'] = COMMON.ERR_INPUT
            save_task_json( task_id, task_json)
            self.update_state( state=COMMON.FINISHED, meta=task_json )
            return task_json    
    
    # Extended User Model
    retCode = custom_user_gen( SRC_DIR, task_json ) 
    if COMMON.OK != retCode:
        update_task_json( task_json, COMMON.ERR_EXTENDED_USER, 'Error customize extended user', COMMON.FAILURE )
        task_json['err_code'] = COMMON.ERR_INPUT
        save_task_json( task_id, task_json)
        self.update_state( state=COMMON.FINISHED, meta=task_json )
        return task_json  

    # Add Models
    retCode = models_gen( SRC_DIR, task_json )
    if COMMON.OK != retCode:
        update_task_json( task_json, COMMON.ERR_CUSTOMIZE_MODELS, 'Error customize DB Models', COMMON.FAILURE )
        task_json['err_code'] = COMMON.ERR_INPUT
        save_task_json( task_id, task_json)
        self.update_state( state=COMMON.FINISHED, meta=task_json )
        return task_json  

    # Added Render Support  
    if input_cicd:
        api_gen_render(SRC_DIR, REPO_NAME)

    # Generate Celery, if TRUE == input_celery
    api_gen_celery(SRC_DIR, input_celery)
    
    if input_auth_github:
        deps_add(SRC_DIR, 'django-allauth', '0.58.1')
        urls_add_rule(SRC_DIR, "path('accounts/', include('allauth.urls'))" )
        settings_apps_add(SRC_DIR, 'allauth')
        settings_apps_add(SRC_DIR, 'allauth.account')
        settings_apps_add(SRC_DIR, 'allauth.socialaccount')
        settings_apps_add(SRC_DIR, 'allauth.socialaccount.providers.github')
        settings_middleware_add(SRC_DIR, 'allauth.account.middleware.AccountMiddleware')

    # Process OAuth Section 
    api_gen_outh_github(SRC_DIR, input_auth_github)

    # Added API via Generator
    if input_api_gen:
        deps_add(SRC_DIR, 'django-dynamic-api', '1.0.4')
        settings_apps_add(SRC_DIR, 'django_dyn_api')
        settings_apps_add(SRC_DIR, 'rest_framework')
        settings_apps_add(SRC_DIR, 'rest_framework.authtoken')
        api_gen_sources(SRC_DIR, task_json)
        #api_gen_script(SRC_DIR) # no need
        api_gen_docker(SRC_DIR)
    else:
        print( ' > API GEN: No INPUT' ) 

    # ######################################################
    # Update Readme links
    
    aDict = {}
    aDict['__REPO_NAME__'] = REPO_NAME
    aDict['__PROJECT_NAME__'] = input_name
    aDict['__DESIGN__'] = input_design.title()

    # apply changes 
    update_readme(SRC_DIR, aDict)

    # ######################################################
    # GH Upload 

    update_task_json( task_json, COMMON.GITHUB_UPLOAD, 'Upload sources to GITHUB', COMMON.RUNNING )
    save_task_json( task_id, task_json)
    self.update_state( state=COMMON.STARTING, meta=task_json )

    logger.info( '*** Upload sources to GITHUB' )
    repo_uploaded = False

    try:
        
        # works only in production (DEBUG=False)
        #if not settings.DEBUG:

        repo_name = repo_create( SRC_DIR, settings.GITHUB_API_KEY, REPO_NAME, aDict )
        if repo_name:
            logger.info( '*** ...done ' )
            repo_uploaded = True
            task_json['gh_repo'] = settings.GITHUB_API_ACCOUNT + repo_name
        else:
            logger.info( '*** Error Saving sources on GITHUB' )
        
        #else:
        #    logger.info( '*** Skip over GITHUB upload (development mode)' )

    except:
        logger.info( '*** Error Saving sources on GITHUB' )

    task_json['repo_uploaded'] = str(repo_uploaded)

    # ######################################################
    # ZIP sources

    sources_zipped = False 
    try:

        logger.info( '*** SOURCES > ZIP Sources ' )

        shutil.make_archive(SRC_DIR, 'zip', SRC_DIR)

        task_json['task_output'] = task_id + '.zip'
        task_json['download_link'] = '/download/app/' + task_id

        save_task_json( task_id, task_json)

        logger.info( '*** ...done ' )
        sources_zipped = True

    except:

        logger.info( '*** Error ZIP-ing sources' )
        
        update_task_json( task_json, COMMON.FINISHED, 'Error ZIP-ing sources', COMMON.FAILURE )
        task_json['err_code'] = COMMON.ERR_SAVE_ZIP
        save_task_json( task_id, task_json)
        self.update_state( state=COMMON.FINISHED, meta=task_json )
        return task_json  
    
    # ######################################################
    # Task is CLOSING (task cleanUP)

    logger.info( '*** CLOSING (clean up)' )

    if not settings.DEBUG and sources_zipped :

        logger.info( '*** SOURCES > delete (already ZIPPED) ' )
        shutil.rmtree( SRC_DIR )
        logger.info( '*** ...done ' )

    else:
        logger.info( '*** SOURCES not deleted (development mode)' )

    # Finish the task
    update_task_json( task_json, COMMON.CLOSING, 'Task is closing', COMMON.SUCCESS )
    save_task_json( task_id, task_json)
    self.update_state( state=COMMON.CLOSING, meta=task_json )

    # ######################################################
    # Task is FINISHED 

    # Trace the event 
    logger.info( '*** FINISHED' )

    update_task_json( task_json, COMMON.FINISHED, 'Task is finished', COMMON.SUCCESS )
    save_task_json( task_id, task_json)
    self.update_state( state=COMMON.FINISHED, meta=task_json )

    ## Task is done, return the FINAL result
    return task_json            

# task used for tests
@celery_app.task(name="task_generator_flask", bind=True)
def task_generator_flask( self, task_input ):

    # ######################################################
    # Handle Task Input

    # Read input
    task_json = task_input

    logger.info( '*** START, using input: ' + str( task_json ) )

    # Get current task id
    task_id               = celery_app.current_task.request.id
    task_json['task_id']  = task_id
    task_ts_start         = h_ts_full()
    task_json['err_code'] = COMMON.ERR_NA

    # ######################################################
    # Validate Input

    input_backend      = task_json['backend']
    input_design       = task_json['design']
    input_name         = task_json['project_name']
    input_docker       = True  if ( task_json['deploy']['docker' ] == True     ) else False
    input_cicd         = True  if ( task_json['deploy']['ci_cd'  ] == True     ) else False
    input_live         = True  if ( task_json['deploy']['go_live'] == True     ) else False
    input_celery       = True  if ( task_json['tools']['celery'  ] == True     ) else False
    input_auth_github  = True  if ( task_json['auth']['github'   ] == True     ) else False
    input_db_mysql     = True  if ( task_json['db']['driver'     ] == 'mysql'  ) else False
    input_db_pgsql     = True  if ( task_json['db']['driver'     ] == 'pgsql'  ) else False
    
    input_api_gen = False 
    #if 'api_generator' in task_json['tools']: 
    #    input_api_gen = True if ( len( task_json['tools']['api_generator'] ) > 0 ) else False

    input_dyn_dt = False 
    if 'dynamic_dt' in task_json['tools']: 
        input_dyn_dt = True if ( len( task_json['tools']['dynamic_dt'] ) > 0 ) else False

    logger.info( '*** Validate Input ')
    logger.info( '    |-- backend       : ' + str( input_backend.upper() ))
    logger.info( '    |-- design        : ' + str( input_design ))
    logger.info( '    |-- auth_github   : ' + str( input_auth_github ))
    logger.info( '    |-- db_mysql      : ' + str( input_db_mysql ))
    logger.info( '    |-- db_pgsql      : ' + str( input_db_pgsql ))
    logger.info( '    |-- docker        : ' + str( input_docker ))
    logger.info( '    |-- ci/cd         : ' + str( input_cicd ))
    logger.info( '    |-- go_live       : ' + str( input_live ))
    logger.info( '    |-- celery        : ' + str( input_celery ))
    logger.info( '    |-- api_generator : ' + str( input_api_gen ))
    logger.info( '    |-- dynamic_dt    : ' + str( input_dyn_dt ))

    # ######################################################
    # Create OUTPUT Directory
    SRC_DIR   = os.path.join(DIR_GEN_APPS, task_id)
    REPO_NAME = f"{input_backend}-{input_design}-{get_ts_unix()}"

    v_ret = dir_create( SRC_DIR )

    if COMMON.ERR == v_ret:
        update_task_json( task_json, COMMON.FINISHED, f"ERR Create output DIR: {SRC_DIR}", COMMON.FAILURE )
        task_json['err_code'] = COMMON.ERR_INPUT
        save_task_json( task_id, task_json)
        self.update_state( state=COMMON.FINISHED, meta=task_json )
        return task_json        

    logger.info( '*** TARGET DIR creation ' + str( SRC_DIR ) )

    # ######################################################
    # Task is STARTING (task set up)

    update_task_json( task_json, COMMON.STARTING, 'Task is starting', COMMON.SUCCESS )
    save_task_json( task_id, task_json)
    self.update_state( state=COMMON.STARTING, meta=task_json )

    logger.info( '*** GENERATE Code (FLASK) - ' + SRC_DIR )

    retCode = reset_sources( SRC_DIR, input_backend )
    if COMMON.OK != retCode:
        update_task_json( task_json, COMMON.ERR_CUSTOMIZE_DB, 'Error reset_sources()', COMMON.FAILURE )
        task_json['err_code'] = COMMON.ERR_INPUT
        save_task_json( task_id, task_json)
        self.update_state( state=COMMON.FINISHED, meta=task_json )
        return task_json    

    retCode = flask_custom_user_gen( SRC_DIR, task_json ) 
    if COMMON.OK != retCode:
        update_task_json( task_json, COMMON.ERR_CUSTOMIZE_DB, 'Error flask_custom_user_gen()', COMMON.FAILURE )
        task_json['err_code'] = COMMON.ERR_INPUT
        save_task_json( task_id, task_json)
        self.update_state( state=COMMON.FINISHED, meta=task_json )
        return task_json    
    
    # Process Models
    retCode = flask_models_gen( SRC_DIR, task_json )
    if COMMON.OK != retCode:
        update_task_json( task_json, COMMON.ERR_CUSTOMIZE_DB, 'Error flask_models_gen()', COMMON.FAILURE )
        task_json['err_code'] = COMMON.ERR_INPUT
        save_task_json( task_id, task_json)
        self.update_state( state=COMMON.FINISHED, meta=task_json )
        return task_json   
      
    # Dynamic DT
    if input_dyn_dt:
        retCode = dyn_dt_sources(SRC_DIR, task_json)
        if COMMON.OK != retCode:
            update_task_json( task_json, COMMON.ERR_CUSTOMIZE_DB, 'Error dyn_dt_sources()', COMMON.FAILURE )
            task_json['err_code'] = COMMON.ERR_INPUT
            save_task_json( task_id, task_json)
            self.update_state( state=COMMON.FINISHED, meta=task_json )
            return task_json           

    # Process Docker
    if not input_docker:
        # remove files
        file_delete( os.path.join( SRC_DIR, 'Dockerfile'         ) )
        file_delete( os.path.join( SRC_DIR, 'docker-compose.yml' ) )
        file_delete( os.path.join( SRC_DIR, 'gunicorn-cfg.py'    ) )
        file_delete( os.path.join( SRC_DIR, '.dockerignore'      ) )
        dir_delete(  os.path.join( SRC_DIR, 'nginx'              ) )

    # Process CI/CD
    if not input_cicd:
        # remove files
        file_delete( os.path.join( SRC_DIR, 'build.sh'    ) )
        file_delete( os.path.join( SRC_DIR, 'render.yaml' ) )

    # Process celery
    if not input_celery:
        # remove files  
        pass 

    # Process auth_github
    if not input_auth_github:
        # remove files
        pass 

    # Enable MySql
    if input_db_mysql:
        # add deps & ENV
        deps_add( SRC_DIR, 'flask-mysqldb', '2.0.0')

    # Enable PgSql
    if input_db_pgsql:
        # add deps & ENV
        #deps_add( SRC_DIR, 'psycopg2', '2.9.9')
        deps_add( SRC_DIR, 'psycopg2-binary', '2.9.10')

    # ######################################################
    # Update Readme links
    
    aDict = {}
    aDict['__REPO_NAME__'] = REPO_NAME
    aDict['__PROJECT_NAME__'] = input_name
    aDict['__DESIGN__'] = input_design.title()

    # apply changes 
    update_readme(SRC_DIR, aDict)

    # ######################################################
    # GH Upload 

    update_task_json( task_json, COMMON.GITHUB_UPLOAD, 'Upload sources to GITHUB', COMMON.RUNNING )
    save_task_json( task_id, task_json)
    self.update_state( state=COMMON.STARTING, meta=task_json )

    logger.info( '*** Upload sources to GITHUB' )
    repo_uploaded = False

    try:
        
        # works only in production (DEBUG=False)
        #if not settings.DEBUG:

        repo_name = repo_create( SRC_DIR, settings.GITHUB_API_KEY, REPO_NAME, aDict )
        if repo_name:
            logger.info( '*** ...done ' )
            repo_uploaded = True
            task_json['gh_repo'] = settings.GITHUB_API_ACCOUNT + repo_name
        else:
            logger.info( '*** Error Saving sources on GITHUB' )
        
        #else:
        #    logger.info( '*** Skip over GITHUB upload (development mode)' )

    except:
        logger.info( '*** Error Saving sources on GITHUB' )

    task_json['repo_uploaded'] = str(repo_uploaded)

    # ######################################################
    # ZIP sources

    sources_zipped = False 
    try:

        logger.info( '*** SOURCES > ZIP Sources ' )

        shutil.make_archive(SRC_DIR, 'zip', SRC_DIR)

        task_json['task_output'] = task_id + '.zip'
        task_json['download_link'] = '/download/app/' + task_id

        save_task_json( task_id, task_json)

        logger.info( '*** ...done ' )
        sources_zipped = True

    except:

        logger.info( '*** Error ZIP-ing sources' )
        
        update_task_json( task_json, COMMON.FINISHED, 'Error ZIP-ing sources', COMMON.FAILURE )
        task_json['err_code'] = COMMON.ERR_SAVE_ZIP
        save_task_json( task_id, task_json)
        self.update_state( state=COMMON.FINISHED, meta=task_json )
        return task_json  
    
    # ######################################################
    # Task is CLOSING (task cleanUP)

    logger.info( '*** CLOSING (clean up)' )

    if not settings.DEBUG and sources_zipped :

        logger.info( '*** SOURCES > delete (already ZIPPED) ' )
        shutil.rmtree( SRC_DIR )
        logger.info( '*** ...done ' )

    else:
        logger.info( '*** SOURCES not deleted (development mode)' )

    # Finish the task
    update_task_json( task_json, COMMON.CLOSING, 'Task is closing', COMMON.SUCCESS )
    save_task_json( task_id, task_json)
    self.update_state( state=COMMON.CLOSING, meta=task_json )

    # ######################################################
    # Task is FINISHED 

    # Trace the event 
    logger.info( '*** FINISHED' )

    update_task_json( task_json, COMMON.FINISHED, 'Task is finished', COMMON.SUCCESS )
    save_task_json( task_id, task_json)
    self.update_state( state=COMMON.FINISHED, meta=task_json )

    ## Task is done, return the FINAL result
    return task_json            

@shared_task
def run_critical_task():
    task_path = getattr(settings, 'CELERY_SCRIPTS_DIR')
    hourly_task = os.path.join(task_path, 'critical', 'critical_task.py')
    result = subprocess.run(['python', hourly_task], capture_output=True, text=True)
    log_to_file('critical_task', task_path, f'{result.stdout}')

@shared_task
def run_hourly_task():
    task_path = getattr(settings, 'CELERY_SCRIPTS_DIR')
    hourly_task = os.path.join(task_path, 'hourly', 'hourly_task.py')
    result = subprocess.run(['python', hourly_task], capture_output=True, text=True)
    log_to_file('hourly_task', task_path, f'{result.stdout}')

@shared_task
def run_daily_task():
    task_path = getattr(settings, 'CELERY_SCRIPTS_DIR')
    daily_task = os.path.join(task_path, 'daily', 'daily_task.py')
    result = subprocess.run(['python', daily_task], capture_output=True, text=True)
    log_to_file('daily_task', task_path, f'{result.stdout}')

@shared_task
def run_weekly_task():
    task_path = getattr(settings, 'CELERY_SCRIPTS_DIR')
    weekly_task = os.path.join(task_path, 'weekly', 'weekly_task.py')
    result = subprocess.run(['python', weekly_task], capture_output=True, text=True)
    log_to_file('weekly_task', task_path, f'{result.stdout}')

@shared_task
def run_monthly_task():
    task_path = getattr(settings, 'CELERY_SCRIPTS_DIR')
    monthly_task = os.path.join(task_path, 'monthly', 'monthly_task.py')
    result = subprocess.run(['python', monthly_task], capture_output=True, text=True)
    log_to_file('monthly_task', task_path, f'{result.stdout}')