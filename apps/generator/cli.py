# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import subprocess

from .common  import *
from .helpers import *

def exec_cmd( full_cmd ):

    retcode = COMMON.OK
    stdout  = ''
    stderr  = ''

    try:

        # create project in src
        result = subprocess.run( full_cmd.split(' '))

        retcode = result.check_returncode() 

    except Exception as e:

        retcode = COMMON.ERR

    return retcode

# Might be buggy
def exec_cmd_full( full_cmd ):

    retcode = COMMON.OK
    stdout  = ''
    stderr  = ''

    try:

        # create project in src
        result = subprocess.run( full_cmd.split(' '), check=True)

        retcode = result.returncode 
        stdout  = result.stdout 
        stderr  = result.stderr         

    except Exception as e:

        retcode = COMMON.ERR

    return retcode, stdout, stderr
