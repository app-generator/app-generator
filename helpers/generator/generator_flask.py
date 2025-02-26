# -*- encoding: utf-8 -*-
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
from .parser_deps    import *


# template loader
def load_tmpl( aDir, aTemplate ):

    TMPL_MODEL = os.path.join( aDir, aTemplate )
    
    model_c = file_read( TMPL_MODEL )

    return model_c

# template loader
def flask_load_model_tmpl():

    return load_tmpl( DIR_TMPL_FLASK, 'model.tmpl' )

# template loader
def flask_process_model_tmpl( aContent, aMap ):

    for k in aMap:
        aContent = aContent.replace(k , aMap[k])

    print( aContent )
    return aContent

def flask_process_model_fields( aModelTemplate, aModelFields, MARKER ):

    print( 'flask_process_model_fields() - Begin' )

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

def flask_save_models(SRC_DIR, aContent):

    print( 'flask_save_models() - Begin' )

    # Use project prefix 
    FILE_FL_MODELS = os.path.join( SRC_DIR, FILE_FL_MODELS_s )

    MARKER   = '__MODELS__'

    retcode, content = cfg_load( FILE_FL_MODELS )

    if COMMON.OK != retcode:
        print( ' > ERR, cfg_load( FILE_FL_MODELS ) failed' )
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

    return cfg_save( FILE_FL_MODELS, file_c )

def flask_models_gen(SRC_DIR, aDict):

    print( 'flask_models_gen() - Begin' )

    retCode, data = parse_models( aDict )
    
    if COMMON.OK != retCode:
        print( ' > ERR, parse_models( ) failed' )
        return retCode

    model_tmpl = flask_load_model_tmpl()
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
        model_source = flask_process_model_tmpl(model_tmpl, model_input)

        # Process the fields for each model
        # model_fields = COMMON.TAB + '#SOME Fields'
        model_fields = ''

        for f_name in data[ model_name ]:
            
            f_type = data[ model_name ][ f_name ]

            if COMMON.TYPE_STRING == f_type:

                model_fields += COMMON.TAB + f_name.lower() + ' = db.Column(db.String(255),  nullable=True)' + '\n'

            elif COMMON.TYPE_TEXT == f_type:

                model_fields += COMMON.TAB + f_name.lower() + ' = db.Column(db.Text, nullable=True)' + '\n'

            elif COMMON.TYPE_INT == f_type:

                model_fields += COMMON.TAB + f_name.lower() + ' = db.Column(db.Integer, nullable=True)' + '\n'  

            elif COMMON.TYPE_INTEGER == f_type:

                model_fields += COMMON.TAB + f_name.lower() + ' = db.Column(db.Integer, nullable=True)' + '\n'  

            elif COMMON.TYPE_NUMBER == f_type:

                model_fields += COMMON.TAB + f_name.lower() + ' = db.Column(db.Integer, nullable=True)' + '\n'  

            elif COMMON.TYPE_FLOAT == f_type:

                model_fields += COMMON.TAB + f_name.lower() + ' = db.Column(db.Float, nullable=True)' + '\n'  

            elif COMMON.TYPE_BOOL == f_type:

                model_fields += COMMON.TAB + f_name.lower() + ' = db.Column(db.Boolean, nullable=True)' + '\n'  

            elif COMMON.TYPE_DATE == f_type:

                model_fields += COMMON.TAB + f_name.lower() + ' = db.Column(db.DateTime, default=db.func.current_timestamp())' + '\n'  

            elif COMMON.TYPE_DATE_TIME == f_type:

                model_fields += COMMON.TAB + f_name.lower() + ' = db.Column(db.DateTime, default=db.func.current_timestamp())' + '\n'  

            #elif COMMON.TYPE_TIME == f_type:
            #
            #    model_fields += COMMON.TAB + f_name.lower() + ' = models.DateField(default=timezone.now)' + '\n'  
            #
            # FK processing
            #elif type(f_type) is dict:
            #
            #    model_fields += COMMON.TAB + f_name.lower() + ' = models.ForeignKey(' + f_type['related_model'] + ', on_delete=models.CASCADE)' + '\n'  

            else:    
                # unsupported
                print( ' > WARN: unsupported [' + f"{f_name} -> {f_type}" +'] (ignored)' )
        
        # Process Fields 
        model_source = flask_process_model_fields( model_source, model_fields, model_marker )
        
        models_content += model_source
        models_content += '\n\n'

    return flask_save_models(SRC_DIR, models_content )        

def flask_custom_user_save( SRC_DIR, aContent ):

    # Use project prefix 
    FILE_FL_USER_MODEL = os.path.join( SRC_DIR, FILE_FL_USER_MODEL_s )

    MARKER   = '__PROFILE_FIELDS__'

    retcode, content = cfg_load( FILE_FL_USER_MODEL )

    if COMMON.OK != retcode:
        print( ' > ERR, cfg_load( FILE_FL_USER_MODEL ) failed' )
        return retcode
    
    file_c = []

    MARKER_BEGIN = '#' + MARKER
    MARKER_END   = '#' + MARKER + 'END'
    processing   = False 

    for line in content:

        if processing:

            if MARKER_END in line:
                processing = False
                file_c.append( COMMON.TAB + MARKER_END )

            continue 

        else:

            if MARKER_BEGIN in line:

                processing = True 

                added_content  = ''
                added_content += COMMON.TAB + MARKER_BEGIN + '\n'
                added_content += aContent           

                file_c.append( added_content )

            else:

                file_c.append( line )                      

    return cfg_save( FILE_FL_USER_MODEL, file_c )

def flask_custom_user_gen( SRC_DIR, aDict ):

    retCode, data = parse_custom_user( aDict )
    
    if COMMON.OK != retCode:
        print( ' > ERR, parse_custom_user() failed' )
        return retCode

    custom_user_c = ''

    for f_name in data:
        
        f_type = data[ f_name ]

        if COMMON.TYPE_STRING == f_type:

            custom_user_c += COMMON.TAB + f_name.lower() + ' = db.Column(db.String(255),  nullable=True)' + '\n'

        elif COMMON.TYPE_TEXT == f_type:

            custom_user_c += COMMON.TAB + f_name.lower() + ' = db.Column(db.Text, nullable=True)' + '\n'
 
        elif COMMON.TYPE_INT == f_type:

            custom_user_c += COMMON.TAB + f_name.lower() + ' = db.Column(db.Integer, nullable=True)' + '\n'  

        elif COMMON.TYPE_INTEGER == f_type:

            custom_user_c += COMMON.TAB + f_name.lower() + ' = db.Column(db.Integer, nullable=True)' + '\n'  

        elif COMMON.TYPE_NUMBER == f_type:

            custom_user_c += COMMON.TAB + f_name.lower() + ' = db.Column(db.Integer, nullable=True)' + '\n'  

        elif COMMON.TYPE_FLOAT == f_type:

            custom_user_c += COMMON.TAB + f_name.lower() + ' = db.Column(db.Float, nullable=True)' + '\n'  

        elif COMMON.TYPE_BOOL == f_type:

            custom_user_c += COMMON.TAB + f_name.lower() + ' = db.Column(db.Boolean, nullable=True)' + '\n'  

        elif COMMON.TYPE_DATE == f_type:

            custom_user_c += COMMON.TAB + f_name.lower() + ' = db.Column(db.DateTime, default=db.func.current_timestamp())' + '\n'  

        elif COMMON.TYPE_TIME == f_type:

            custom_user_c += COMMON.TAB + f_name.lower() + ' = db.Column(db.DateTime, default=db.func.current_timestamp())' + '\n'  

        else:    
            # unsupported
            print( ' > WARN: unsupported ['+f_type+'] (ignored)' )

    return flask_custom_user_save( SRC_DIR, custom_user_c )

