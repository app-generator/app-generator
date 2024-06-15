# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from .common  import *
from .helpers import *
from .cli     import *

def deps_list( SRC_DIR ):
    
    # Use project prefix 
    FILE_DJ_DEPS = os.path.join( SRC_DIR, FILE_DJ_DEPS_s )

    # Check app exists 
    requirements = file_load( FILE_DJ_DEPS, True )

    # Check app exists
    if not requirements:
        print('ERR: ' + FILE_DJ_DEPS+ ' not found')
        return None   

    print( '> Dependencies:' )
    for line in requirements:
        print( '   |-- ' + line )

def deps_add( SRC_DIR, aModule, aVersion=None):

    # Use project prefix 
    FILE_DJ_DEPS = os.path.join( SRC_DIR, FILE_DJ_DEPS_s )

    # Check app exists 
    requirements = file_load( FILE_DJ_DEPS, True )

    # Check app exists
    if not requirements:
        print('ERR: ' + FILE_DJ_DEPS+ ' not found')
        return None   

    aModule = aModule.lower()
    found   = False  

    requirements_p = []
    for line in requirements:
        line = line.lower() 

        # module laready there, update version
        if aModule == line or ((aModule +'==') in line):

            found = True 
            if aVersion:
                line = aModule + '==' + aVersion
            else:    
                line = aModule

        requirements_p.append( line )

    if not found: 
        if aVersion:
            aModule += '==' + aVersion

        requirements_p.append( aModule )

    file_write( FILE_DJ_DEPS, requirements_p)

def deps_delete( SRC_DIR, aModule ):

    # Use project prefix 
    FILE_DJ_DEPS = os.path.join( SRC_DIR, FILE_DJ_DEPS_s )
    
    # Check app exists 
    requirements = file_load( FILE_DJ_DEPS, True )

    # Check app exists
    if not requirements:
        print('ERR: ' + FILE_DJ_DEPS+ ' not found')
        return None   

    aModule = aModule.lower()

    requirements_p = []
    for line in requirements:
        line = line.lower() 

        # module laready there, update version
        if aModule == line or ((aModule +'==') in line):
            pass
        else:                
            requirements_p.append( line )

    file_write( FILE_DJ_DEPS, requirements_p)
