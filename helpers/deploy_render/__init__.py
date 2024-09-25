# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from .common   import *  # Constants and ENV vars
from .helpers  import *  # Global helpers

from .owners   import *  # Wraps 'owners'   API
from .services import *  # Wraps 'services' API
from .deploys  import *  # Wraps 'deploys'  API

def repo_deploy( aRepoName ):

    # None on failure
    response_json = deploy_django( aRepoName )

    #if response_json:
    #    deploy_id  = response_json["deployId"]
    #    deploy_url = response_json["service"]["serviceDetails"]["url"]

    return response_json 
