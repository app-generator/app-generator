# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

class COMMON:

    NULL                = None # not set
    NA                  = -1   # not set
    OK                  =  0   # All good   (unix style)
    ERR                 =  1   # Err bumped (unix style)
    NOT_FOUND           =  2   # file or directory not found
    ERR_INPUT           =  3   # file or directory not found
    DIR_EXIST           =  4   # DIR Exists
    ERR_ENCODING        =  5   # Encoding/Decoding Error 
    ERR_NA              =  6
    ERR_GENERIC         =  7
    ERR_DESIGN          =  8
    ERR_GEN_CODE        =  9
    ERR_SAVE_GH         = 10
    ERR_SAVE_DISK       = 11
    ERR_SAVE_ZIP        = 12
    ERR_CUST_DB         = 13
    ERR_CUST_DOCKER     = 14    
    ERR_CUST_HEROKU     = 15
    ERR_CUST_FRONTEND   = 16   

    TYPE_REACT          = 'react'
    TYPE_NEXT_JS        = 'next.js'
    TYPE_NODE_JS        = 'node.js'
    TYPE_FLASK          = 'flask'
    TYPE_DJANGO         = 'django'
    TYPE_LARAVEL        = 'laravel'

    # Tasks RESULTS (for current operations)
    SUCCESS             = 'SUCCESS'
    FAILURE             = 'FAILURE'
    RUNNING             = 'RUNNING'
    PENDING             = 'PENDING'
    CANCELLED           = 'CANCELLED'    
    FINISHED            = 'FINISHED'
    CLOSING             = 'CLOSING'

    # Tasks STATEs/OPERATIONS
    STARTING            = 'STARTING'
    GENERATE_CODE       = 'GENERATE_CODE'
    GITHUB_UPLOAD       = 'GITHUB_UPLOAD'

def errInfo( aErrorCode ):

    if COMMON.NULL          == aErrorCode: return 'Not Set'
    if COMMON.NA            == aErrorCode: return 'Not Set'
    if COMMON.OK            == aErrorCode: return 'OK'
    if COMMON.ERR           == aErrorCode: return 'Generic Error'
    if COMMON.NOT_FOUND     == aErrorCode: return 'Not Found'
    if COMMON.ERR_INPUT     == aErrorCode: return 'Input error'
    if COMMON.DIR_EXIST     == aErrorCode: return 'DIR Exists'
    if COMMON.ERR_ENCODING  == aErrorCode: return 'Encoding/Decoding Error'

    return str( aErrorCode )

