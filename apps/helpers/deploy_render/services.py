# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import requests, json

from .common   import *
from .helpers  import *
from .owners   import *

def list_services():
    """
    Referance: https://api-docs.render.com/reference/get-services
    This endpoint lists all services that are owned by your Render user and any teams you're a part of.
    """

    url = f"{URL}/v1/services"

    try:
        response = requests.get(url, headers=HEADERS)

        if 200 != response.status_code:
            raise Exception( response.text )

        json_data = json.loads( response.text )

        if DEBUG:
            print( pp_json( json_data ) ) 

        return json_data

    except Exception as e:
        print(e)
        return None

def retrieve_service( aServiceID ):
    """
    Referance: https://api-docs.render.com/reference/get-service
    """

    url = f"{URL}/v1/services/{aServiceID}"

    try:
        response = requests.get(url, headers=HEADERS)
        return response
    except Exception as e:
        print(e)
        return False

def update_service( aServiceID ):
    """
    Referance: https://api-docs.render.com/reference/update-service
    Update service allows you to update the configuration details of service, such as start commands and branches.
    Changes will not be deployed automatically. Instead you must call the deploy API to have changes pushed out to your service, irrespective of the autoDeploy option set on the service.
    """

    url = f"{URL}/v1/services/{aServiceID}"

    payload = {
        "autoDeploy": "yes",
        "branch": "main",
        "name": "react-dash-board"
    }

    try:
        response = requests.patch(url, json=payload, headers=HEADERS)
        return response
    except Exception as e:
        print(e)
        return False

def delete_service( aServiceID ):
    """
    Referance: https://api-docs.render.com/reference/delete-service
    """

    url = f"{URL}/v1/services/{aServiceID}" 

    try:
        response = requests.delete(url, headers=HEADERS)
        return response
    except Exception as e:
        print(e)
        return False
