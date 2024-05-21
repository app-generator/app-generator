# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, random, string #, netaddr
import shutil
import fnmatch
import json
from   pathlib  import Path
from   datetime import datetime

from .common  import *

def hello():
    print(' > Test ' + errInfo( COMMON.OK ) )

def dir_exists( path ):

    try:

        if os.path.exists( path) and os.path.isdir( path) :
            return True
        else:
            return False
        
    except:
        #print ( ' *** DIR not found = ' + path )
        return False    

def dir_create( path ):

    if dir_exists( path ):
        #print ( ' *** DIR exists = ' + path )
        return False    

    try:

        os.mkdir(path)
        return True
        
    except Exception as e:
        #print ( ' *** Err creating DIR: ' + str(e) )
        return False    

def dir_copy(src, dst, symlinks=False, ignore=None):

    try:

        # Create destination 
        if not dir_exists( dst ):
            dir_create( dst )

        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)

        return True

    except Exception as e:
        #print ( ' *** Err copy DIR: ' + str(e) )
        return False 

def dir_delete( path ):

    if dir_exists( path ):
        shutil.rmtree( path )

    return True

def dir_subdirs( path ):

    # this includes also path
    all_dirs = [x[0] for x in os.walk( path )]    

    if path in all_dirs:
        all_dirs.remove( path )

    return all_dirs    

def file_exists( path ):

    try:

        if open( path, 'r'):
            #print ( ' *** File exists = ' + path )
            return True

    except:
        #print ( ' *** File not found = ' + path )
        return False    

def file_read( path, encoding='utf8' ):

    try:

        f = open( path, 'r', encoding=encoding)
        if f:

            content = f.read()    
            
            f.close()
            return content

    except UnicodeDecodeError as err:

        print(" *** UnicodeDecodeError: {0}".format(err))
        return None

    except Exception as e:

        print (' *** Err loading file: ' + str( e ) )
        return None

def file_delete( path ):

    try:
        
        os.remove( path )

        return True 

    except Exception as e:

        return None

def file_load( path, as_list=False ):

    try:

        f = open( path, 'r')
        if f:

            if as_list:
                content = f.read().splitlines()
            else:
                content = f.read()    
            
            f.close()
            return content

    except UnicodeDecodeError as err:

        print(" *** UnicodeDecodeError: {0}".format(err))

    except Exception as e:

        print (' *** Err loading file: ' + str( e ) )
        return None

def file_write( path, content, f_append=False ): 

    try:

        f = None

        if file_exists( path ):
            if f_append:    
                f = open( path, 'a+')
            else:
                f = open( path, 'w+')    
        else:
            f = open( path, 'w+')

        if not f:
            #'Err open file'
            return False

        if type(content) is list:
            content_p = ''
            for line in content:
                content_p += line + '\n'

            content = content_p

        f.seek(0) 
        f.write( content )
        f.truncate()

        f.close()
        return True

    except Exception as e:

        print( 'ERR file_write(): ' + str( e ) )
        return False

    except:

        print ( ' *** Err processing file ' + str(file_path) )
        return False

def file_create( path, content='' ):

    return file_write( path, content )

def file_append( file_path, new_content):

    #print ( 'append content to file ' + file_path )
    return file_write( file_path, new_content, True ) 

def file_print( file_path ):

    try:

        f = open( file_path, 'r')
        if f:
            for line in f.readlines():
                print ( line.rstrip() )

        return True

    except:

        print ( ' *** Err loading file ' + str(file_path) )
        return False

def file_find( aDir, aFileName ):

    retCode      = COMMON.OK
    errorInfo    = 'NA'
    file_content = None
    DIR_LIST     = []

    # Validate Input
    if not os.path.isdir( aDir ):
        return COMMON.INPUT_ERR, 'Input not DIR = ' + aDir, None

    # Get all subdirs
    DIR_LIST.extend( get_subdirs( aDir ) )

    # Iterate on Dirs
    for d in DIR_LIST:

        # Iterate on files
        for f in get_files(d, '*'):
            
            #print ( 'Compare [' + aFileName + '] -> [' + f + ']' )

            # Files muct match a FULL_PATH
            if f.endswith(aFileName):
                return COMMON.OK, errorInfo, file_load( f )            

    return COMMON.NOT_FOUND, 'File not found = ' + aFileName, None

def files_get(dir_to_scan, ext='*'):

    matches = []

    for root, dirnames, filenames in os.walk( dir_to_scan ):

        for filename in fnmatch.filter(filenames, '*.'+ ext):

            item = os.path.join(root, filename)

            #print ' **** type(item) = ' + str( type ( item ) )
            matches.append( item )

    return matches

def h_del_lsep( line ):

    if line:
        line = line.replace('\n', '').replace('\r', '')

    return line    

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text  

def list_files( aPath, aExt=None ):

    matches = []

    ignore_ENV = os.path.join( aPath, 'env' )

    #print( ' > DIR_SRC: ' + aPath)

    for root, dirnames, filenames in os.walk( aPath ):
        
        if aExt: 

            for filename in fnmatch.filter(filenames, '*.' + aExt ):

                item = os.path.join(root, filename)
                
                if item.startswith( ignore_ENV ) or '.pyc' in item or 'sqlite' in item:
                    continue

                #print( ' >  FILE:   ' + item)
                f = remove_prefix( item, aPath + os.path.sep )
                #print( ' >  FILE: ' + f)
                matches.append( f )
        else:

            for filename in filenames:

                item = os.path.join(root, filename)

                if item.startswith( ignore_ENV ) or '.pyc' in item or 'sqlite' in item:
                    continue

                #print( ' >  FILE:   ' + item)
                f = remove_prefix( item, aPath + os.path.sep )
                #print( ' >  FILE_p: ' + f)
                matches.append( f )

    return matches

def h_random(aLen=16):
    letters = string.ascii_letters
    digits  = string.digits
    chars   = '_<>,.+'
    return ''.join(random.choices( letters + digits + chars, k=aLen))

def h_random_ascii(aLen=16):
    letters = string.ascii_letters
    digits  = string.digits
    return ''.join(random.choices( letters + digits, k=aLen))

def h_ts():
    return datetime.today().strftime('%Y%m%d')

def list_to_s( aList, aDelim='' ):
    
    retVal = ''
    for k in aList:
        retVal += k + aDelim

    return retVal

def ipToINT(aIP):
    return -1 # int(netaddr.IPAddress(aIP))

def get_client_ip(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')

        # Convert to INT
        ip_v = ipToINT( ip )

        if isinstance(ip_v, int):
            return ip_v
        else:
            return -1 

    except:
        return -1
