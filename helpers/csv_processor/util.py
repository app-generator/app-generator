# -*- encoding: utf-8 -*-

import os, json, glob, fnmatch, shutil, re
from datetime import datetime
import pandas as pd
from django.conf import settings

from .common import * 

def get_ts():
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

def dir_create(dir_path):
    try:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
    except Exception as e:
        raise e

def dir_exists ( aPath ):
    return os.path.isdir( aPath )   

def dir_rm ( aPath ):
    if os.path.exists( aPath ):
        shutil.rmtree( aPath )          

def file_exists( aPath ):

    try:

        if open( aPath, 'r'):
            return True

    except:
        return False  

def file_save( aPath, aContent ):

    with open(aPath, 'w') as f:

        if isinstance(aContent, str):
            f.write( aContent )
            return True

        if isinstance(aContent, list): 

            content_str = ''    
            for line in aContent:
                content_str += line + '\n'       

            f.write( content_str )
            return True

        if isinstance(aContent, dict): 

            content_str = ''    
            for key, value in aContent.items():
                content_str += key + '=' + value + '\n'       

            f.write( content_str )
            return True

    return False

def file_append( aPath, aNewContent ):

    with open(aPath, "r") as file:

       content  = file.read()
       content += '\n' + aNewContent

       return file_save( aPath, content )

    return False

def file_load( aFilePath, aMark=None ):

    try:

        f = open( aFilePath, 'r')
        if not f:
            return None

        if aMark:

            content = ''
            for line in f:
                content += line
                if aMark in line:
                    break 

        else:

            content = f.read()    
            
        f.close()
        return content 

    except:

        try: 
            with open(aFilePath, mode='rb') as f: # b is important -> binary
                return f.read()
        except:
            return None

    return None        

def file_rm ( aPath ):
    if file_exists( aPath ):
        os.remove( aPath )

def list_files( aPath, aExt=None ):

    matches = []

    for root, dirnames, filenames in os.walk( aPath ):
        
        if aExt: 

            for filename in fnmatch.filter(filenames, '*.' + aExt ):

                #item = os.path.join(root, filename)

                matches.append( filename)
        else:

            for filename in filenames:

                #item = os.path.join(root, filename)

                matches.append( filename )

    return matches

def find_type(values):
    numbers = "[0-9]"
    alphabets = "[a-zA-Z]"
    not_number_alphabet = "[^a-zA-Z0-9.]"
    types = []
    for value in values:
        has_number   = re.search(numbers, value)
        has_alphabet = re.search(alphabets, value)
        has_extra    = re.search(not_number_alphabet, value)
        if ' ' not in value:
            if has_number and not has_alphabet:
                if has_extra:
                    types.append('string')
                elif '.' in value:
                    types.append('number')
                else:
                    types.append('integer')
            else:
                types.append('string')
        else:
            types.append('string')
    return types

def normalizeStr( aName ):

    if not aName:
        return aName

    forbiddenChars = ['\'', '"', '`', '(', ')','/', '\\', '“', '”', '%']
    for c in forbiddenChars:
        aName = aName.replace(c, '')

    if '.' in aName:
        aName = aName.split('.')[0]

    aName  = aName.replace('   ', ' ')
    aName  = aName.replace('  ', ' ')
    aName  = aName.replace('_', ' ')
    aName  = aName.replace('-', ' ')
    retVal = aName

    if ' ' in aName:

        retVal = ''

        for token in aName.split(' '):
            
            retVal += token.capitalize()

    return retVal

def cleanValue( aVal ):

    # This makes the fiels NULLable
    if not aVal:
        return None
    
    forbiddenChars = ['“', '”']

    for c in forbiddenChars:
        aVal = aVal.replace(c, '')

    # Boolean type Fix
    if 'true' == aVal.lower():
        aVal = aVal.capitalize()

    if 'false' == aVal.lower():
        aVal = aVal.capitalize()

    if '' == aVal:
        aVal = None 

    # print(' cleanValue() returns ' + str(aVal) )

    return aVal 

def parse_csv( CVS_FILE ):

    fields = []
    types  = [] 
    model  = {}

    df = pd.read_csv( CVS_FILE )
    for dtype in df.dtypes.items():
        # print( str( dtype[ 0 ] ) + ' - ' + str( dtype[ 1 ] ) )
        
        item_name = str( dtype[ 0 ] )
        item_type = str( dtype[ 1 ] )

        for tk in item_name.split(','):
            fields.append( normalizeStr( tk ) )     
            types.append ( item_type )

        # fields.append(  normalizeStr( str( dtype[ 0 ] )) )
        # types.append (  str( dtype[ 1 ] ) )
    
    for i in range(len(fields)):
        model[ normalizeStr(fields[i]) ] = {'type': types[i]}

    return model

def load_csv_data(aFilePath):

    try:

        cvs_data = []
        
        f = open( aFilePath, 'r')
        if not f:
            return None

        for line in f:
            cvs_data.append( line.strip() )

        return cvs_data 
        
    except:

        return None 

def save_csv_data(aFilePath, aCSVData):

    try:

        cvs_data = aCSVData
        
        f = open( aFilePath, 'w')
        if not f:
            return None

        for line in aCSVData:
            f.write( line + '\n' )

        f.close()    
        return True
        
    except:

        return False

def get_django_model(model_dict):
    codes = ""
    for attribute_name in model_dict:

        if attribute_name.lower() == 'id':
            continue

        codes = codes + f"\t{attribute_name} = "
        attribute = model_dict[attribute_name]

        attribute_type = attribute['type']

        # print( ' > ATTR ['+attribute_name+'] -> ['+attribute_type+']' )

        if attribute_type == 'OneToOneField':
            codes = codes + f"models.OneToOneField({attribute_type}_ID)\n"
            # print( '   match -> OneToOneField' ) 

        elif attribute_type == 'ManyToManyField':
            codes = codes + f"models.ManyToManyField({attribute_type}_ID)\n"
            # print( '   match -> ManyToManyField' ) 

        elif attribute_type == 'ForeignKey':
            codes = codes + f"models.ForeignKey({attribute_type}_ID)\n"
            # print( '   match -> ForeignKey' ) 

        elif attribute_type in django_fields:

            f_type = django_fields[attribute_type] + '\n'
            codes = codes + f_type
            # print( '   match -> django_field->' + f_type ) 

        else:
            codes = codes + f"models.ForeignKey({attribute_type})\n"
            # print( '   match -> ForeignKey' ) 

    return codes

def convert_csv_to_django_models(ModelName, Fields):

    model_code  = f"class {ModelName}(models.Model):\n\tID = models.AutoField(primary_key=True)\n"

    model_code += get_django_model(Fields)

    return model_code

def media_file_exists( aFile ):
    return file_exists( os.path.join(settings.MEDIA_ROOT, aFile) )

def media_file_rm( aFile ):
    return file_rm( os.path.join(settings.MEDIA_ROOT, aFile) )

def json_load( aPath ):

    if file_exists( aPath ):
        return json.loads( file_load( aPath ) ) 

    return None
 
