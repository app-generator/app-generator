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
