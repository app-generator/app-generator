# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, json, glob, fnmatch, shutil, re

from .common  import *
from .helpers import *
from .cli     import *

def json_load( aPath=INPUT_JSON ):

    if file_exists( aPath ):
        return json.loads( file_load( aPath ) ) 

    #print( ' > Err: JSON not found: ' + aPath )
    return None 

def json_parse_key( aKey ):

    retCode    = COMMON.NA
    data_value = None 

    try:

        aJSON = json_load()

        data_value = aJSON[ aKey ]

        print ( ' > ' + aKey + ': ' + data_value )
        retCode = COMMON.OK

    except Exception as e:
        print( ' > Err parsing JSON: ' +str( e ) )
        retCode = COMMON.ERR

    return retCode, data_value

def parse_key(aJSON, aKey ):

    retCode    = COMMON.NA
    data_value = None 

    try:

        data_value = aJSON[ aKey ]

        print ( ' > ' + aKey + ': ' + data_value )
        retCode = COMMON.OK

    except Exception as e:
        print( ' > Err parsing JSON: ' +str( e ) )
        retCode = COMMON.ERR

    return retCode, data_value

def parse_db( aJSON=None ):

    retCode = COMMON.NA
    data = {}

    db_driver = None
    db_name   = None
    db_user   = None
    db_pass   = None
    db_host   = None 
    db_port   = None

    try:

        if not aJSON:
            aJSON = json_load()

        data['driver']   = aJSON['db']['driver']
        data['name']     = aJSON['db']['name']
        data['user']     = aJSON['db']['user']
        data['password'] = aJSON['db']['pass']
        data['host']     = aJSON['db']['host']
        data['port']     = aJSON['db']['port']

        print ( ' > DB Settings ' )
        print ( '    |-- driver : ' + data['driver']   )
        print ( '    |-- db_name: ' + data['name']     )
        print ( '    |-- db_user: ' + data['user']     )
        print ( '    |-- db_pass: ' + data['password'] )
        print ( '    |-- db_host: ' + data['host']     )
        print ( '    |-- db_port: ' + data['port']     )

        retCode = COMMON.OK

    except Exception as e:
        print( ' > Err parsing JSON: ' +str( e ) )
        retCode = COMMON.ERR

    return retCode, data

def parse_models( aJSON=None ):

    retCode = COMMON.OK
    data = {}

    try: 

        if not aJSON:
            aJSON = json_load()

        print ( ' > Models ' )
        for model in aJSON['models']:
            model_d = {}

            print ( '    |-- ' + model )
            for field in aJSON['models'][model]:
                field_t = aJSON['models'][model][field]

                model_d[field] = field_t
                print ( '    |    > ' + field + ', ' + field_t )

            # All good, save the model
            data[model] = model_d

        #retCode = COMMON.OK

    except Exception as e:
        print( ' > Err parsing JSON: ' +str( e ) )
        retCode = COMMON.ERR

    # We can have zero definitions
    # if 0 == len( data ):
    #    retCode = COMMON.NOT_FOUND

    return retCode, data

def parse_custom_user( aJSON=None ):

    retCode = COMMON.OK
    data = {}

    try: 

        if not aJSON:
            aJSON = json_load()
            if not aJSON: 
                print ( ' > Error loading JSON ' )
                return COMMON.NOT_FOUND, None
        
        # list of dicts
        print ( ' > Custom User ' )
        for field_dict in aJSON['custom_user']:
            
            f_name = field_dict['fieldName']
            f_type = field_dict['fieldType']

            data[f_name] = f_type
            print ( '    |-- ' + f_name + ', ' + f_type )

    except Exception as e:
        print( ' > Err parsing JSON: ' +str( e ) )
        retCode = COMMON.ERR

    return retCode, data

def parse_auth( aJSON=None ):

    retCode = COMMON.NA
    data = {}

    try: 

        if not aJSON:
            aJSON = json_load()

        print ( ' > AUTH ' )
        for field in aJSON['auth']:
            field_t = aJSON['auth'][field]

            data[field] = field_t
            print ( '    |-- ' + field + ' ' + field_t )

        retCode = COMMON.OK

    except Exception as e:
        print( ' > Err parsing JSON: ' +str( e ) )
        retCode = COMMON.ERR

    if 0 == len( data ):
        retCode = COMMON.NOT_FOUND

    return retCode, data

def parse_deploy( aJSON=None ):

    retCode = COMMON.NA
    data = {}

    try: 

        if not aJSON:
            aJSON = json_load()

        print ( ' > DEPLOY ' )
        for field in aJSON['deploy']:
            field_t = aJSON['deploy'][field]

            data[field] = field_t
            print ( '    |-- ' + field + ' ' + field_t )

        retCode = COMMON.OK

    except Exception as e:
        print( ' > Err parsing JSON: ' +str( e ) )
        retCode = COMMON.ERR

    if 0 == len( data ):
        retCode = COMMON.NOT_FOUND

    return retCode, data

def parse_api_generator( aJSON=None ):

    retCode = COMMON.NA
    data = {}

    try: 

        if not aJSON:
            aJSON = json_load()

        print ( ' > API Generator ' )
        for api_path in aJSON['tools']['api_generator']:

            api_model = aJSON['tools']['api_generator'][api_path]

            print ( '  |-- ' + api_path + ' -> ' + api_model)

            # All good, save the model
            data[api_path] = api_model

        retCode = COMMON.OK

    except Exception as e:
        print( ' > Err parsing JSON: ' +str( e ) )
        retCode = COMMON.ERR

    if 0 == len( data ):
        retCode = COMMON.NOT_FOUND

    return retCode, data

def parse_json( aJsonFile='input.json' ):
    
    # check app exists 
    JSON_PATH = os.path.join(DIR_ROOT, aJsonFile )

    JSON = json_load( JSON_PATH )

    if not JSON:
        print('ERR: ' + aJsonFile + ' not found')
        return None   

    # Parse Name
    retCode, project_name = parse_key( JSON, 'project_name' )
    if COMMON.OK != retCode:
        print( ' > ERR Parsing JSON [project_name]' ) 

    # Parse Design
    retCode, project_design = parse_key( JSON, 'design' )
    if COMMON.OK != retCode:
        print( ' > ERR Parsing JSON [design]' ) 

    # Parse DB (connection string, driver ..)
    retCode, db_data = parse_db( JSON )
    if COMMON.OK != retCode:
        print( ' > ERR Parsing JSON DB Settings' ) 

    # Parse Models 
    retCode, db_models = parse_models( JSON )
    if COMMON.OK != retCode:
        print( ' > ERR Parsing JSON DB Models' ) 

    # Parse Custom User
    retCode, custom_user = parse_custom_user( JSON )
    if COMMON.OK != retCode:
        print( ' > ERR Parsing JSON Custom_USER' )         

    # Parse AUTH
    retCode, auth = parse_auth( JSON )
    if COMMON.OK != retCode:
        print( ' > ERR Parsing JSON AUTH' )  

    # Parse Deploy
    retCode, deploy = parse_deploy( JSON )
    if COMMON.OK != retCode:
        print( ' > ERR Parsing JSON AUTH' )          

    # Parse API generator
    retCode, api_gen_rules = parse_api_generator( JSON )
    if COMMON.OK != retCode:
        print( ' > ERR Parsing API Generator' )  

    print(' > JSON, all good ')
