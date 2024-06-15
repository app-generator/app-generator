# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import requests, json

from .common   import *

def list_authorized_users_and_teams():
    """
    Referance: https://api-docs.render.com/reference/get-owners
    This endpoint lists all users and teams that your API key has access to. This can be helpful for getting the correct ownerId to use for creating new resources, such as services.
    """

    url = f"{URL}/v1/owners"

    try:

        # url="https://api.render.com/v1/owners"

        if DEBUG:
            print( ' ')
            print( 'URL     > ' + str( url     ) )
            print( 'HEADERS > ' + str( HEADERS ) )

        # Warn: do not use PARAMS input 
        response = requests.get(url, headers=HEADERS)

        if 200 != response.status_code:
            raise Exception( response.text )

        if DEBUG:
            print( response.text ) 

        return json.loads( response.text )

    except Exception as e:
        print(e)
        return None

def retrieve_user_or_team(d_obj):
    """
    Referance: https://api-docs.render.com/reference/get-owner
    This endpoint gets information for a specific user or team that your API key has permission to access, based on ownerId.
    """

    url = f"{URL}/v1/owners/{d_obj['owner_id']}"

    try:
        response = requests.get(url, headers=HEADERS)
        return response
    except Exception as e:
        print(e)
        return False

def list_owners():

    # JSON 
    autz_users = list_authorized_users_and_teams()

    if not autz_users:
        return None 

    retVal = []

    try:

        for item in autz_users:
            retVal.append( item['owner']['id'] )

        #if DEBUG:
        print( str( retVal ) )

        return retVal

    except Exception as e:
        print(e)
        return None

def get_owner():

    # If present in ENV, return the value
    if RENDER_OWNER_ID:
        return RENDER_OWNER_ID

    all_owners = list_owners()

    if not all_owners or len( all_owners ) == 0:
        return None 

    # pick the first one
    retVal = all_owners[0]

    #if DEBUG:
    print( str( retVal ) )

    # return the first one
    return retVal
