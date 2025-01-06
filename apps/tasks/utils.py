# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, json, glob, fnmatch, shutil
from datetime import datetime

from helpers.generator.common import *
from helpers.util import *

def get_task_json( task_id ):

    logfile_dir  = os.path.join(DIR_GEN_APPS, task_id)
    logfile      = os.path.join(DIR_GEN_APPS, task_id + '.json')

    # if output dir for task does not exist
    if not os.path.exists(logfile_dir):
        return None

    # if log file for task does not exist
    if not os.path.exists(logfile):
        return None

    with open(logfile, "r") as f:

        return json.loads( f.read() )

    return None     

def save_task_json( task_id, aJSON ):

    logfile_dir  = os.path.join(DIR_GEN_APPS, task_id)
    logfile      = os.path.join(DIR_GEN_APPS, task_id + '.json')

    # create output directory
    dir_create(logfile_dir)

    with open(logfile, 'w') as f:
        f.write( json.dumps( aJSON, indent=4, sort_keys=True ) )

def update_task_json(aJSON, aState, aInfo=None, aResult=None ):

    aJSON['task_state'] = aState

    if COMMON.STARTING == aState:
        aJSON['task_ts_start' ] = h_ts_full()     
        aJSON['task_info'     ] = 'NA'
        aJSON['task_result'   ] = 'NA'
    else:
        aJSON['task_ts_end' ] = h_ts_full()     

    if aInfo:
        aJSON['task_info'   ] = aInfo

    if aResult:    
        aJSON['task_result' ] = aResult

def get_task_start_ts( task_id ):

    logfile_dir  = os.path.join(DIR_GEN_APPS, task_id)
    logfile      = os.path.join(logfile_dir, task_id + '.json')

    # if output dir for task does not exist
    if not os.path.exists(logfile_dir):
        return "None"

    # if log file for task does not exist
    if not os.path.exists(logfile):
        return "None"

    # check if TASK STARTED entry exists in log file
    start_time = ""
    with open(logfile, "r") as f:

        json_log = json.loads( f.read() )
        
        try:
            return json_log['task_ts_start']
        except Exception as e:
            pass 

    return ""

def get_active_tasks( aCeleryApp ):

    if not aCeleryApp:
        return None

    inspect_celery = aCeleryApp.control.inspect()
    active_tasks   = inspect_celery.active()

    celery_groups = [] # tasks are defined under groups
    task_list     = [] 

    if active_tasks:

        for key in active_tasks.keys():
            celery_groups.append( key )

        for grp_name in celery_groups :

            for task in active_tasks[ grp_name ]: 

                _task_status   = aCeleryApp.AsyncResult(task["id"]).status
                _task_start_ts = aCeleryApp.AsyncResult(task["id"]).info.get('ts_start', 'NA')

                #_task_details = {"id"       : task["id"],
                #                "status"   : _task_status,
                #                "ts_start" : _task_start_ts }

                _task_details = get_task_json( task["id"] ) 

                task_list.append(_task_details)

    return task_list
