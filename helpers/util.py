# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, random, string, shutil, fnmatch,json
from   pathlib  import Path
from   datetime import datetime

from .common  import *
from apps.common.models import Profile
from apps.common.models_products import Props

def dir_exists( path ):

    try:

        if os.path.exists( path) and os.path.isdir( path) :
            return True
        
    except:
        #print ( ' *** Err: ' + str(e) )
        return False
    
    return False

def dir_create( path ):

    if dir_exists( path ):

        #print ( ' *** DIR exists = ' + path )
        return COMMON.DIR_EXIST    

    try:

        os.mkdir(path)
        return COMMON.OK
        
    except Exception as e:
        #print ( ' *** Err: ' + str(e) )
        return COMMON.ERR

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

        return COMMON.OK

    except Exception as e:
        #print ( ' *** Err: ' + str(e) )
        return COMMON.ERR 

def dir_delete( path ):

    try:

        if dir_exists( path ):
            shutil.rmtree( path )

        return COMMON.OK

    except Exception as e:
        #print ( ' *** Err: ' + str(e) )
        return COMMON.ERR 

def dir_subdirs( path ):

    try:

        if not dir_exists( path ):
            #print ( ' *** DIR exists = ' + path )
            return COMMON.NOT_FOUND  
            
        # this includes also path
        all_dirs = [x[0] for x in os.walk( path )]    

        if path in all_dirs:
            all_dirs.remove( path )

        return all_dirs    

    except Exception as e:
        #print ( ' *** Err: ' + str(e) )
        return COMMON.ERR 

def file_exists( path ):

    try:

        if open( path, 'r'):
            #print ( ' *** File exists = ' + path )
            return COMMON.OK

    except:
        #print ( ' *** Err: ' + str(e) )
        return COMMON.ERR  

def file_read( path, encoding='utf8' ):

    try:

        f = open( path, 'r', encoding=encoding)
        if f:

            content = f.read()    
            
            f.close()
            return content

    except UnicodeDecodeError as err:

        #print(" *** UnicodeDecodeError: {0}".format(err))
        return COMMON.ERR_ENCODING

    except Exception as e:

        #print ( ' *** Err: ' + str(e) )
        return COMMON.ERR

def file_delete( path ):

    try:
        
        os.remove( path )

        return COMMON.OK 

    except Exception as e:
        #print ( ' *** Err: ' + str(e) )
        return COMMON.ERR 

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

        #print(" *** UnicodeDecodeError: {0}".format(err))
        return COMMON.ERR_ENCODING

    except Exception as e:

        #print ( ' *** Err: ' + str(e) )
        return COMMON.ERR

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
        return COMMON.OK

    except Exception as e:

        #print ( ' *** Err: ' + str(e) )
        return COMMON.ERR
    
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

        return COMMON.OK

    except:

        #print ( ' *** Err: ' + str(e) )
        return COMMON.ERR

def files_get(dir_to_scan, ext='*'):

    try:

        matches = []

        for root, dirnames, filenames in os.walk( dir_to_scan ):

            for filename in fnmatch.filter(filenames, '*.'+ ext):

                item = os.path.join(root, filename)

                #print ' **** type(item) = ' + str( type ( item ) )
                matches.append( item )

        return matches
    
    except:

        #print ( ' *** Err: ' + str(e) )
        return COMMON.ERR    

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

def file_process(aFilePath):
    
    file_dir     = None 
    file_name    = None 
    file_ext     = None 
    file_content = None 

    if file_exists( aFilePath ) != COMMON.OK:
        return COMMON.NOT_FOUND
    
    file_dir, file_name = os.path.split( aFilePath )

    file_name, file_ext = os.path.splitext( file_name )
    
    file_content = file_read( aFilePath )

    return COMMON.OK, file_dir, file_name, file_ext, file_content

def file_md_process(aFilePath):
    
    file_dir     = None 
    file_name    = None 
    file_ext     = None 
    file_content = None 
    file_header  = [] 
    md_content   = []

    if file_exists( aFilePath ) != COMMON.OK:
        return COMMON.NOT_FOUND
    
    file_dir, file_name = os.path.split( aFilePath )

    file_name, file_ext = os.path.splitext( file_name )
    
    file_lines = file_load( aFilePath, True )
    
    front_begin = False
    front_end   = False

    for line in file_lines:

        #print( '> LINE ' + line )

        if '---' in line and not front_begin:
            front_begin = True 
            continue
        if front_begin and not front_end:
            if '---' in line:
                front_end = True 
                continue 
            file_header.append( line )

        if front_end:
            md_content.append( line )

    return COMMON.OK, file_dir, file_name, file_ext, file_header, md_content

def parse_md_header(aHeader):
    retVal = {}

    for line in aHeader:
        key, val = line.split(':')
        retVal[key.strip()] = val.lstrip().rstrip()
            
    return json.dumps(retVal, indent = 4)
 
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

def h_ts_full():
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

def list_to_s( aList, aDelim='' ):
    
    retVal = ''
    for k in aList:
        retVal += k + aDelim

    return retVal

def ipToINT(aIP):
    return -1 # int(netaddr.IPAddress(aIP))

def get_client_ip(request):
    
    try:
        
        ip = None 

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')

        return str( ip )

    except:
        return 'NA'

def is_pro(aUser):
    if aUser:
        return aUser.profile.pro

    return False  

def make_pro(aEmail): 
    try:
        u = Profile.objects.filter(email=aEmail).first()
        u.pro = True
        u.save()
    except:
        pass

def delete_pro(aEmail): 
    try:
        u = Profile.objects.filter(email=aEmail).first()
        u.pro = False
        u.save()
    except:
        pass

def h_label(aLabel):
    try:
        row = Props.objects.filter(data=aLabel).first()
        return row.value if row else aLabel             
    except:
        return aLabel
