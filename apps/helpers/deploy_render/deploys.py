# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import requests, json

from .common   import *
from .helpers  import *
from .owners   import *

def list_deploys(d_obj):
    """
    Referance: https://api-docs.render.com/reference/get-deploys
    """

    url = f"{URL}/v1/services/{d_obj['service_id']}"

    try:
        response = requests.patch(url, headers=HEADERS)
        return response
    except Exception as e:
        print(e)
        return False


def trigger_a_deploy():
    """
    Referance: https://api-docs.render.com/reference/create-deploy
    """

    url = f"{URL}/v1/services/{d_obj['service_id']}"

    payload = {
        "clearCache": "clear"
    }

    try:
        response = requests.patch(url, json=payload, headers=HEADERS)
        return response
    except Exception as e:
        print(e)
        return False

def deploy_django( aRepo ):
    """
    Referance: https://api-docs.render.com/reference/create-service
    """

    url     = f"{URL}/v1/services"

    try:

        ownerId      = get_owner()
        service_name = ''
        aEntryPoint  = ENTRY_POINT_DJANGO

        build_cmd    = './build.sh'
        start_cmd    =  f"gunicorn {aEntryPoint}"

        service_name = nameFromRepo( aRepo )

        if not ownerId:
            raise Exception( 'Error getting owner' )

        payload = {
            'autoDeploy': 'yes',
            'envVars': [
                {
                    "key": "DEBUG",
                    "value": "False"
                }
            ],            
            'serviceDetails': {
                'env':  'python',
                "envSpecificDetails":{
                    "buildCommand": build_cmd,
                    "startCommand": start_cmd
                },
            },
            'type': 'web_service',
            'name': service_name,
            'ownerId': ownerId,
            'repo': aRepo,
        }

        response = requests.post(url, json=payload, headers=HEADERS)

        # HTTP 201 = Resource Created
        if 201 != response.status_code:
            raise Exception( response.text )

        response_json = json.loads( response.text )

        #if DEBUG:
        #    print( ' > RESPONSE ' + str( response_json ) )        

        deploy_id  = response_json["deployId"]
        deploy_url = response_json["service"]["serviceDetails"]["url"]
        
        #if DEBUG:
        #   print(" > Deploy ID ["+deploy_id+"] -> " + deploy_url)

        return response_json

    except Exception as e:
        print(e)
        return None 
