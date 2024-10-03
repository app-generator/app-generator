import os, importlib, time, datetime
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from django.db.models import ForeignKey, Q
import pandas as pd

from helpers import *

INPUT_DIR     = os.path.join('media')
OUTPUT_FILE   = os.path.join('apps' , 'common', 'models.py')
MODELS_IMPORT = 'apps.common.models'

# Helper 
def normalize_file_name( aName ):

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

# Helper 
def normalize_column(aName, Mapper):

    aName_ = aName

    # Remove Forbiden
    forbiddenChars = ['\'', '"', '`', '\\', '“', '”']
    for c in forbiddenChars:
        aName = aName.replace(c, '')

    # Remove multi-space
    aName  = aName.replace('    ', ' ')
    aName  = aName.replace('   ', ' ')
    aName  = aName.replace('  ', ' ')
    aName  = aName.replace('-', ' ')

    if 'normalize_col_name' not in Mapper:
        #print( '    - normalization1 ['+aName_+'] -> ['+aName+']')
        return aName

    for key in Mapper['normalize_col_name']:
        val = Mapper['normalize_col_name'][key]
        aName = aName.replace(key, val)

    #print( '    - normalization2 ['+aName_+'] -> ['+aName+']')
    return aName

# Helper 
def column_has_transformer(aModel, aColumn, aMapper):

    key = aModel + '_' + aColumn
    if key in aMapper['col_transformers']:
        return aMapper['col_transformers'][key]

    # Defult case (no transformers)
    return False

# Helper 
def column_real_name(aModel, aColumn, aMapper):

    key = aModel + '_' + aColumn
    if key in aMapper["col_name"]:
        return aMapper["col_name"][key]

    return aColumn   

# Helper 
def column_transformer(aRule, aCurrentValue):

    transformer = aRule.split('_')[0]
    key         = aRule.split('_')[1]

    if 'int' == transformer:
        return int(key)

    if 'append' == transformer:
        return aCurrentValue + key

    if 'timestamp' == transformer:
        aCurrentValue = time.mktime(datetime.strptime( aCurrentValue, key ).timetuple())
        return int( aCurrentValue )

    # No transformer
    return aCurrentValue

# Helper 
def model_real_name( CVS_FILE, Mapper):

    ModelCsv = CVS_FILE

    if file_exists(CVS_FILE):
        head, tail = os.path.split( CVS_FILE )
        ModelCsv = tail

    model_name = normalize_file_name( ModelCsv )
    if 'models_name' in Mapper:
        if ModelCsv in Mapper['models_name']:
            model_name = Mapper['models_name'][ModelCsv]
    return model_name

# Helper
def model_dependencies( ModelName, Mapper):
    if ModelName in Mapper['linked_models']:
        return Mapper['linked_models'][ModelName].split(',')
    return None  

# Helper 
def model_is_isolated(ModelName, Mapper):
    if model_dependencies(ModelName, Mapper):
        return False
    return True

# Helper
def model_field_relation(ModelName, FieldName, Mapper):    
    key = ModelName + '_' +FieldName
    if 'linked_fields' in Mapper:
        if key in Mapper['linked_fields']:
            return Mapper['linked_fields'][key]
    return None  

# Helper
def model_field_is_referenced(ModelName, FieldName, Mapper):    
    data = ModelName + '_' +FieldName
    if 'linked_fields' in Mapper:
        for key in Mapper['linked_fields']:
            if data == Mapper['linked_fields'][key]:
                return key
    return None 

# Helper
def is_model_fk(ModelName, FieldName, Mapper):
    """Returns None if not foreignkey, otherswise the relevant model"""
    field_object, model, direct, m2m = ModelName._meta.get_field(FieldName)
    if not m2m and direct and isinstance(field_object, ForeignKey):
        return field_object.rel.to
    return None

def has_forbiddedn_chars(aInput, ForbiddednChars=None ):
    
    if not ForbiddednChars:
        ForbiddednChars = [',"', '",']

    for s in ForbiddednChars:
        if s in aInput:
            return True 

    return False                

# Helper 
def cvs_process_header( aLine ):
    
    INNER_sep = '_'
    
    danger = has_forbiddedn_chars( aLine ) 

    fields = aLine.split(',')

    # The happy case 
    if not danger:
        return fields

    count = aLine.count('"')
    if (count % 2) != 0:
        #print( ' >>>  cvs_process_header() -> EXIT 1' )
        return None         
    
    # search for "" sequences and extract
    aLine_p = ''
    index = 0
    for tk in aLine.split('"'):
        
        index += 1

        if ( index % 2 ) == 0:
            #print( ' TK [' + tk + ']')
            aLine_p += tk.replace(',', INNER_sep)
        else:
            aLine_p += tk 

    return aLine_p.split(',')

# Helper 
def cvs_process_line( aLine, aExpectedTokens=None ):
    
    INNER_sep = '__X__'
    
    danger = has_forbiddedn_chars( aLine ) 

    fields = aLine.split(',')

    if not aExpectedTokens:
        aExpectedTokens = len(fields)

    # The happy case 
    if aExpectedTokens == len( fields ) and not danger:
        return fields

    count = aLine.count('"')
    if (count % 2) != 0:
        print( ' >>>  cvs_process_line() -> EXIT 1' )
        return None         
    
    # search for "" sequences and extract
    aLine_p = ''
    index = 0
    for tk in aLine.split('"'):
        
        index += 1

        if ( index % 2 ) == 0:
            #print( ' TK [' + tk + ']')
            aLine_p += tk.replace(',', INNER_sep)
        else:
            aLine_p += tk 

    fields = aLine_p.split(',')

    fields_p = []
    for f in fields:
        fields_p.append( f.replace(INNER_sep, ',') )
    
    return fields_p

def cvs_check( aCsvFile, aApplyCorrection=True ):
    
    status    = False 
    corrected = False 

    CVS_DATA  = csv_load( aCsvFile )

    #if not CVS_FILE_c:
    if not CVS_DATA:    
        print(f" > ERR loading INPUT file: " + aCsvFile)
        return False, False

    # Check Header
    CVS_HEADER = CVS_DATA[0]
    if has_forbiddedn_chars( CVS_HEADER ):

        CVS_HEADER_fields = cvs_process_header( CVS_HEADER )

        if not CVS_HEADER_fields:
            print(f' > ERROR parsing header ['+str(len( CVS_HEADER ))    +']: ' + CVS_HEADER )
            return False, False

        CVS_HEADER_raw    = ','.join( CVS_HEADER_fields )

        if aApplyCorrection:

            CVS_DATA[0] = CVS_HEADER_raw
            csv_save(aCsvFile, CVS_DATA)

        return True, True

    return True, False

def csv_load(aFilePath):

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

def csv_save(aFilePath, aCSVData):

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

# Helper
def generate_model(ModelName, ModelData, Mapper): 

    print( ' > GENERATE [' + ModelName + '] ')

    model_code = f"class {ModelName}(models.Model):\n\tID = models.AutoField(primary_key=True)\n"

    # Processing HERE 
    codes = ""
    for attribute_name in ModelData:

        if attribute_name.lower() == 'id':
            continue

        attribute = ModelData[attribute_name]

        attribute_type = attribute # attribute['type']

        print( '  -> Field [' + attribute_name + '], type = ' + attribute_type )

        # hack
        field_name_key = ModelName + '_' + attribute_name  # Used for mapper
        
        if field_name_key in Mapper['col_name']:
            attribute_name = Mapper['col_name'][field_name_key]
            print( '     (i) NAME mapped to [' + attribute_name + '] ')

        if field_name_key in Mapper['col_type']:
            attribute_type = Mapper['col_type'][field_name_key]        
            print( '     (i) TYPE mapped to [' + attribute_type + '] ')
        # hack ends        
        
        codes = codes + f"\t{attribute_name} = "

        relation = model_field_relation(ModelName, attribute_name, Mapper)
        if relation:

            relation_model = relation.split('_')[0]
            relation_field = relation.split('_')[1]
            print( '      > RELATION detected for [' + attribute_name + '], (FK) -> ' + relation_model + '.' + relation_field)
            codes += "models.ForeignKey({0}, to_field='{1}', on_delete=models.CASCADE)".format(relation_model, relation_field) 
            codes += '\n'

        elif model_field_is_referenced(ModelName, attribute_name, Mapper):   

            print( '      > REFERENCE detected for [' + attribute_name + '] (needs UNIQUES) ')
            f_type = django_fields['object_unique'] + '\n'
            codes += f_type

        elif attribute_type in django_fields:

            f_type = django_fields[attribute_type] + '\n'
            codes += f_type

        else:
            codes += attribute_type + '\n'

    model_code += codes
    return model_code

# Helper
def csv_to_model( CVS_FILE, aMapper ):

    fields = []
    types  = [] 
    model  = {}

    # used for fields name mapping 
    model_name = model_real_name( CVS_FILE, aMapper)

    df = pd.read_csv( CVS_FILE )
    for dtype in df.dtypes.items():
        # print( str( dtype[ 0 ] ) + ' - ' + str( dtype[ 1 ] ) )
        
        item_name = str( dtype[ 0 ] )
        item_type = str( dtype[ 1 ] )

        for tk in item_name.split(','):
            fields.append( normalize_column( tk, aMapper ) )     
            types.append ( item_type )

        # fields.append(  normalizeStr( str( dtype[ 0 ] )) )
        # types.append (  str( dtype[ 1 ] ) )
    
    for i in range(len(fields)):
        
        # We can fields mapped to other types
        field_name     = fields[i]
        field_type     = types[i]
        field_name_key = model_name + '_' + field_name  # Used for mapper
        
        if field_name_key in aMapper['col_name']:
            field_name = aMapper['col_name'][field_name_key]

        # Update KEY     
        field_name_key = model_name + '_' + field_name  # Used for mapper

        if field_name_key in aMapper['col_type']:
            field_type = aMapper['col_type'][field_name_key]

        model[ normalize_column(field_name, aMapper) ] = django_fields[ field_type ]

    return model

class Command(BaseCommand):
    help = 'CVSs To Models'

    def add_arguments(self, parser):
        
        parser.add_argument('-i', '--info'      , action='store_true', help='Prin Help')
        parser.add_argument('-s', '--simulation', action='store_true', help='Simulates the generator')
        parser.add_argument('-l', '--load'      , action='store_true', help='Load Data into DB')
        parser.add_argument('-d', '--del'       , action='store_true', help='Delete Model data before load')
        parser.add_argument('-m',                 type=str,            help='Mapper File')
        parser.add_argument('-c', '--check'     , action='store_true', help='Check Input Files')
        parser.add_argument('-f',                 type=str,            help='Input File')

    def handle(self, *args, **kwargs):
        
        simulation  = kwargs[ 'simulation' ]
        load        = kwargs[ 'load'       ]
        del_data    = kwargs[ 'del'        ]
        mapper_file = kwargs[ 'm'          ]
        check_input = kwargs[ 'check'      ]
        info        = kwargs[ 'info'       ]
        input_file  = kwargs[ 'f'          ]

        if info: 
            print(f"")
            print(f" > HELP: CLI for CSV to Model translation (plus load)")
            print(f"    -i (or --info)       : Print this help, and exit")
            print(f"    -c (or --check)      : Check Input (CSV) files for integrity (fix if neccessary)")
            print(f"    -s (or --simulation) : Simulates the CVS to Model translation (nothing is write on the disk)")
            print(f"    -l (or --load)       : Load CSV data into associated models")
            print(f"    -d (or --del)        : Wipe, delete models data")
            print(f"    -m <MAPPER.json>     : Specify a new Mapper file to be used")
            print(f"")

            return             

        print(f"Generate Models FROM multiple CVSs")

        if not mapper_file:
            mapper_file = 'mapper.json'

        input  = INPUT_DIR # kwargs['input']
        mapper = json_load( os.path.join( INPUT_DIR, mapper_file) )

        if not input:
            print(f" > ERR: Input DIR not provided")
            return  

        if not dir_exists( input ):
            print(f" > ERR: Input is not a DIR")
            return  

        if not mapper:
            print(f" > ERR: Mapper not provided or not found ["+mapper_file+"]")
            return  

        if mapper and 'version' in mapper:
            print( ' > Using Mapper [' + mapper_file + '], version ' + mapper['version'] )

        all_csv_files = list_files( input, 'csv' )
        csv_files = []

        if input_file:
            print( ' > CVS: ' + input_file )
            
            if input_file not in all_csv_files:
                print(f" > ERR: INPUT file not found in MEDIA folder")
                return

            csv_files.append( input_file )

        else:    
            if 'input' in mapper:
                for csv_f in mapper['input']: 
                    csv_files.append( csv_f )
            else: 
                csv_files = all_csv_files

        if not csv_files or ( 0 == len( csv_files ) ):
            print(f" > ERR: No CVSs found in ["+input+"]")
            return  

        print( ' > CVSs: ' + str( csv_files ) )

        ### Load Target File (Models.py) 
        MODEL_FILE_MARK = '### ### Below code is Generated ### ###'
        MODEL_FILE_c    = file_load( OUTPUT_FILE, MODEL_FILE_MARK )

        ## Simulation mode active
        if simulation:

            print( ' > SIMULATION mode')

            # Print Tables & Quality
            for file_name in csv_files:  

                ### Load CSV File 
                CVS_FILE   = os.path.join( INPUT_DIR, file_name)
                CVS_FILE_c = file_load( CVS_FILE ) 

                model_name = model_real_name( file_name, mapper)

                if model_is_isolated(model_name, mapper ):
                    print(f" > TABLE: " + model_name + ' -> ISOLATED ')
                else:
                    print(f" > TABLE: " + model_name + ' -> DEPS: ' + str( model_dependencies(model_name, mapper ) ) )
                
                # Parse CVS and extract fields + Types 
                model_data = csv_to_model( os.path.join( INPUT_DIR, file_name), mapper )
                for model_field in model_data:
                    print('   -> ' + model_field + ' ' + model_data[model_field] + ' (detected)')

                    #print( ' *****************> SCAN relation for [' + model_name + '] -> [' + model_field + ']' )
                    relation = model_field_relation(model_name, model_field, mapper)
                    if relation:
                        print('      |--> (One-to-One) ' + relation.replace('_', '.') )

                    is_referenced = model_field_is_referenced(model_name, model_field, mapper) 
                    if is_referenced:
                        print('      |--> (UNIQUE), referenced by ' + is_referenced.replace('_', '.') )

            # Exit Simulation
            return

        elif check_input:
            
            print( ' > Check INPUT')
            for file_name in csv_files:               

                ### Load CSV File 
                CVS_FILE = os.path.join( INPUT_DIR, file_name)
                
                print( ' > PROCESSING: ' + CVS_FILE )

                status, corrected = cvs_check( CVS_FILE )

                if status:

                    if corrected: 
                        print( ' ----> STATUS OK (corrected)' )
                    else:
                        print( ' ----> STATUS OK' )
                
                else:
                    print( ' ----> STATUS ERR (file cannot be used)' )

        else:

            for file_name in csv_files:

                # Execution mode active
                print(f" > *** *** ***" )
                print(f" > PROCESSING " + file_name )

                ### Load CSV File 
                CVS_FILE   = os.path.join( INPUT_DIR, file_name)
                #CVS_FILE_c = file_load( CVS_FILE ) 
                CVS_DATA   = csv_load( CVS_FILE )

                #if not CVS_FILE_c:
                if not CVS_DATA:    
                    print(f" > ERR loading INPUT file: " + CVS_FILE)
                    return         

                # Data used in both contexts 
                model_data = csv_to_model( CVS_FILE, mapper )

                model_name = model_real_name(CVS_FILE, mapper)

                print( ' > Model: ' + model_name + ' from ' + file_name)

                # Load case
                if load or del_data: 

                    print( ' > Input data into [' + model_name + '] from [' + file_name + ']')        

                    models = importlib.import_module( MODELS_IMPORT )

                    try:
                        model = getattr(models, model_name)
                    except Exception as e:
                        print( ' > Model Exception ' + str(e) )
                        return 

                    print(f" > Model Found: " +model_name+ " ")

                    try:
                        model.objects.last()
                    except OperationalError:
                        print( ' > Model ['+model_name+'] not migrated, ' + str(e) )
                        print( ' > Migrate Model ['+model_name+'] ')
                        call_command('makemigrations', 'portfolio' )
                        call_command('migrate',        'portfolio' )
                        print( '   ...done ')    

                    print(f" > Model IS Migrated: " +model_name)

                    if del_data:
                        print( ' > DELETE data trigered for [' + model_name + ']') 
                        model.objects.all().delete()
                        print( ' > ...done' ) 

                        if not load:
                            continue 
                    
                    CVS_DATA_HEADERS_RAW = cvs_process_line( CVS_DATA.pop(0) )
                    CVS_DATA_HEADERS     = []

                    #for cvs_header_field in CVS_DATA.pop(0).split(','):
                    for cvs_header_field in CVS_DATA_HEADERS_RAW:

                        # Column_real_name
                        CVS_DATA_HEADERS.append( column_real_name(model_name, cvs_header_field, mapper) )

                    print(f" > [" +str( len(CVS_DATA_HEADERS) )+ "] CSV Headers: " + str(CVS_DATA_HEADERS) )

                    count     = 0
                    countWARN = {} # mismatch between Expected and Found token 
                    countERR  = {} # conversion errors 

                    for line in CVS_DATA:

                        count += 1

                        try:

                            #print(f" > LINE = " + str (line) )
                            fields = cvs_process_line( line, len(CVS_DATA_HEADERS) )

                            if not fields:
                                print(f"  ERR Parsing [" + str(count) + "] ["+line+"]" )
                                continue

                            print(f"  Line [" + str(count) + "][ > " +str( len(fields) )+ " fields " + str(fields) )

                            if len( CVS_DATA_HEADERS ) != len( fields ):
                                countWARN[count] = line
                                print(f" > WARN: Line["+str( count )+"]: expected ["+str(len( CVS_DATA_HEADERS))+"] tokens, found ["+str(len( fields ))+"]")
                                continue    

                            db_item    = model()
                            insert_row = True 
                            idx = -1

                            for val in fields:

                                idx += 1

                                # We need here the real column name
                                field_name = normalize_column( CVS_DATA_HEADERS[ idx ], mapper)
                                field_val = cleanValue(val)

                                fk_model =  model_field_relation(model_name, field_name, mapper) 

                                if fk_model:
                                    fk_model_name  = fk_model.split('_')[0]
                                    fk_model_field = fk_model.split('_')[1]

                                    try: 

                                        fk_model = getattr(models, fk_model_name)

                                        field_val = fk_model.objects.filter( Q(**{fk_model_field + '__icontains': field_val} ) ).get()

                                        setattr( db_item, field_name, field_val)

                                    except Exception as e:
                                            insert_row = False
                                            countERR[count] = line
                                            print( '   >>> ERR Set Value for ['+field_name+'] ' + str(e) )

                                elif hasattr(db_item, field_name): 
                                    
                                    transformer = column_has_transformer(model_name, field_name, mapper)

                                    # Use transformed value    
                                    if transformer: 
                                        converted_val = column_transformer(transformer, field_val)    
                                        print( '   ['+str(idx)+']['+field_val+'] -> ' + str(converted_val) + ' (from transformer)')
                                        setattr( db_item, field_name, converted_val)
                                    # Use default    
                                    else:

                                        try:   
                                            setattr( db_item, field_name, field_val) 
                                        except Exception as e:
                                            insert_row = False
                                            countERR[count] = line
                                            print( '    >>> ERR Set Value for ['+field_name+'] ' + str(e) )
                                else:
                                    insert_row = False
                                    print( '   ---> Warn: ['+field_name+']['+str(idx)+']: NOT_IN_MODEL') 

                            if insert_row:
                                db_item.save()
                            else:
                                print( '   ---> ROW not added it ') 

                        except Exception as e:
                            countERR[count] = line
                            print(f" > ERR on line["+str(count)+"]: " + str( e ) )
                            print(f"          line["+str(line)+"]" )

                            continue

                    sz_CVS_DATA  = len( CVS_DATA  )
                    sz_countWARN = len( countWARN )
                    sz_countERR  = len( countERR  )
                    sz_IMPORTED  = sz_CVS_DATA - sz_countWARN - sz_countERR

                    print(f" > STATS: ")
                    print(f"    TOTAL Lines       : " + str( sz_CVS_DATA              ) )
                    print(f"    Imported          : " + str( sz_IMPORTED              ) )    
                    print(f"    Warnings          : " + str( sz_countWARN             ) )    
                    print(f"    Errors            : " + str( sz_countERR              ) )  
                    print(f"    Unprocessed Lines : " + str( list ( countERR.keys() ) ) )

                # Model extraction case     
                else:     

                    model_django = os.linesep + generate_model( model_name, model_data, mapper)

                    if not MODEL_FILE_c:
                        print(f" > ERR loading OUTPUT file: " + OUTPUT_FILE)
                        return     

                    MODEL_FILE_c += str( model_django )
                    
                    if file_save( OUTPUT_FILE, MODEL_FILE_c ):
                        print(f"   -> File saved")
                    else:
                        print(f"   -> ERR saving OUTPUT file: " + OUTPUT_FILE)            

                print(f" > EXIT")
        