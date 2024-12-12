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
    # Create OUTPUT Directory
    SRC_DIR = os.path.join(DIR_GEN_APPS, task_id)
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

    logger.info( '*** GENERATE Code ' )

    reset_sources( SRC_DIR )

    # ######################################################
    # GH Upload 

    update_task_json( task_json, COMMON.GITHUB_UPLOAD, 'Upload sources to GITHUB', COMMON.RUNNING )
    save_task_json( task_id, task_json)
    self.update_state( state=COMMON.STARTING, meta=task_json )

    logger.info( '*** Upload sources to GITHUB' )
    repo_uploaded = False
    try:
        
        repo_name = repo_create( SRC_DIR, settings.GITHUB_API_KEY )
        if repo_name:
            logger.info( '*** ...done ' )
            repo_uploaded = True
            task_json['gh_repo'] = settings.GITHUB_API_ACCOUNT + repo_name
        else:
            logger.info( '*** Error Saving sources on GITHUB' )
                 
    except:
        logger.info( '*** Error Saving sources on GITHUB' )

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

    if sources_zipped:
        logger.info( '*** SOURCES > delete (already ZIPPED) ' )
        shutil.rmtree( SRC_DIR )
        logger.info( '*** ...done ' )

    update_task_json( task_json, COMMON.CLOSING, 'Task is closing', COMMON.SUCCESS )
    save_task_json( task_id, task_json)
    self.update_state( state=COMMON.CLOSING, meta=task_json )

    # ######################################################
    # Task is FINISHED 

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