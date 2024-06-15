# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, random, string
from github      import Github

from .common     import *
from .helpers    import *
from .api_deploy import *

def repo_deploy( aRepoName ):

    # None on failure
    response_json = deploy_django( aRepoName )

    #if response_json:
    #    deploy_id  = response_json["deployId"]
    #    deploy_url = response_json["service"]["serviceDetails"]["url"]

    return response_json 
