# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, sys,wget, zipfile

from .common         import *
from .helpers        import *
from .cli            import *
from .parser_common  import *
from .parser_json    import *

# template loader
def load_model_tmpl():

    TMPL_MODEL = os.path.join( DIR_TMPL, 'model.tmpl')
    
    model_c = file_read( TMPL_MODEL )
    print( model_c )
    return model_c

# template loader
def process_model_tmpl( aContent, aMap):

    for k in aMap:
        aContent = aContent.replace(k , aMap[k])

    print( aContent )
    return aContent

def process_model_fields( aModelTemplate, aModelFields, MARKER ):
    
    aModelTemplate_proc = []

    MARKER_BEGIN = '#' + MARKER
    MARKER_END   = '#' + MARKER + 'END'
    processing   = False 

    print( ' > INPUT')
    print( '    |-- Fields: ' + aModelFields)
    print( '    |-- MARKER: ' + MARKER      )
    
    for line in aModelTemplate.splitlines():

        print( ' > Line: '+line)    
        if processing:

            if MARKER_END in line:
                processing = False
                aModelTemplate_proc.append( COMMON.TAB + MARKER_END )

            continue 

        else:

            if MARKER_BEGIN in line:

                processing = True 

                added_content  = ''
                added_content += COMMON.TAB + MARKER_BEGIN + '\n'
                added_content += aModelFields           

                aModelTemplate_proc.append( added_content )

            else:

                aModelTemplate_proc.append( line )                      

    return list_to_s( aModelTemplate_proc, '\n' )

def save_models(SRC_DIR, aContent):

    # Use project prefix 
    FILE_DJ_MODELS = os.path.join( SRC_DIR, FILE_DJ_MODELS_s )

    MARKER   = '__MODELS__'

    retcode, content = cfg_load( FILE_DJ_MODELS )

    if COMMON.OK != retcode:
        print( ' > ERR, cfg_load( FILE_DJ_MODELS ) failed' )
        return retcode
    
    file_c = []

    MARKER_BEGIN = '#' + MARKER
    MARKER_END   = '#' + MARKER + 'END'
    processing   = False 

    for line in content:

        if processing:

            if MARKER_END in line:
                processing = False
                file_c.append( MARKER_END )

            continue 

        else:

            if MARKER_BEGIN in line:

                processing = True 

                added_content  = ''
                added_content += MARKER_BEGIN + '\n'
                added_content += aContent           

                file_c.append( added_content )

            else:

                file_c.append( line )                      

    return cfg_save( FILE_DJ_MODELS, file_c )

def models_gen(SRC_DIR, aDict):

    retCode, data = parse_models( aDict )
    
    if COMMON.OK != retCode:
        print( ' > ERR, parse_models( ) failed' )
        return retCode

    model_tmpl = load_model_tmpl()
    models_content = ''

    for model_name in data:

        model_input  = {}
        model_source = ''

        # UC First the model name
        model_name_p = model_name.title()
        model_marker = '__{}_FIELDS__'.format(model_name_p)
        model_input['MODEL_NAME']         = model_name_p
        model_input['MODEL_NAME_VERBOSE'] = model_name_p 

        # Process Metadata 
        model_source = process_model_tmpl(model_tmpl, model_input)

        # Process the fields for each model
        # model_fields = COMMON.TAB + '#SOME Fields'
        model_fields = ''

        for f_name in data[ model_name ]:
            
            f_type = data[ model_name ][ f_name ]

            if COMMON.TYPE_STRING == f_type.lower():

                model_fields += COMMON.TAB + f_name.lower() + ' = models.CharField(max_length=255, null=True, blank=True)' + '\n'

            elif COMMON.TYPE_TEXT == f_type.lower():

                model_fields += COMMON.TAB + f_name.lower() + ' = models.TextField(max_length=255, null=True, blank=True)' + '\n'

            elif COMMON.TYPE_INT == f_type:

                model_fields += COMMON.TAB + f_name.lower() + ' = models.IntegerField(null=True, blank=True)' + '\n'  

            elif COMMON.TYPE_INTEGER == f_type:

                model_fields += COMMON.TAB + f_name.lower() + ' = models.IntegerField(null=True, blank=True)' + '\n'  

            elif COMMON.TYPE_NUMBER == f_type:

                model_fields += COMMON.TAB + f_name.lower() + ' = models.IntegerField(null=True, blank=True)' + '\n'  

            elif COMMON.TYPE_FLOAT == f_type:

                model_fields += COMMON.TAB + f_name.lower() + ' = models.FloatField(null=True, blank=True)' + '\n'  

            elif COMMON.TYPE_DATE == f_type:

                model_fields += COMMON.TAB + f_name.lower() + ' = models.DateTimeField(blank=True, null=True, default=timezone.now)' + '\n'  

            elif COMMON.TYPE_TIME == f_type:

                model_fields += COMMON.TAB + f_name.lower() + ' = models.DateTimeField(blank=True, null=True, default=timezone.now)' + '\n'  

            else:    
                # unsupported
                print( ' > WARN: unsupported ['+f_type+'] (ignored)' )
        
        # Process Fields 
        model_source = process_model_fields( model_source, model_fields, model_marker )
        
        models_content += model_source
        models_content += '\n\n'

    return save_models(SRC_DIR, models_content )        
