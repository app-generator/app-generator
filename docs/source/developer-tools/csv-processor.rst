CSV Processor
=============

This page explains how to **Load and Process CSV files** that asa saved in the local fielsystem or remote. 
For newcomers, CSV (Comma-Separated Values) is a simple, text-based file format used for storing tabular data. Each line in a CSV file represents a row of data, with individual values separated by commas. 

.. include::  /_templates/components/signin-invite.rst

CSV files are widely used for data exchange between different software applications due to their simplicity and compatibility.

Regarding our processor, here is the list with all supported operations: 

- load local and remte files 
- print values 
- print column types
- print the mapping types to a Django Model 


Quick Start 
------------

The parser can be used using the CLI and the files shipped in the `media` directory. 

.. code-block:: bash

    $ python manage.py tool_inspect_source -f media/tool_inspect/csv_inspect.json

The tools performs the following tasks: 

- validate the input 
- locate the CSV file (exit with error if not found)
- loads the information and detects the column types 
- detects the Django column type 
- print the first 10 rows 

The same can be applied for local and remote files. For instance, we can analyze the notorious Titanic.cvs by running this one-liner: 

.. code-block:: bash

    $ python manage.py tool_inspect_source -f media/tool_inspect/csv_inspect_distant.json

    # Output
    > Processing .\media\tool_inspect\csv_inspect_distant.json
        |-- file: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
        |-- type: csv


    Field        CSV Type    Django Types
    -----------  ----------  ------------------------------------------
    PassengerId  int64       models.IntegerField(blank=True, null=True)
    Survived     int64       models.IntegerField(blank=True, null=True)
    Pclass       int64       models.IntegerField(blank=True, null=True)
    Name         object      models.TextField(blank=True, null=True)
    Sex          object      models.TextField(blank=True, null=True)
    Age          float64     models.FloatField(blank=True, null=True)
    SibSp        int64       models.IntegerField(blank=True, null=True)
    Parch        int64       models.IntegerField(blank=True, null=True)
    Ticket       object      models.TextField(blank=True, null=True)
    Fare         float64     models.FloatField(blank=True, null=True)
    Cabin        object      models.TextField(blank=True, null=True)
    Embarked     object      models.TextField(blank=True, null=True)


    [1] - PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
    [2] - 1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
    [3] - 2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C
    [4] - 3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925,,S
    [5] - 4,1,1,"Futrelle, Mrs. Jacques Heath (Lily May Peel)",female,35,1,0,113803,53.1,C123,S
    [6] - 5,0,3,"Allen, Mr. William Henry",male,35,0,0,373450,8.05,,S
    [7] - 6,0,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,Q
    [8] - 7,0,1,"McCarthy, Mr. Timothy J",male,54,0,0,17463,51.8625,E46,S
    [9] - 8,0,3,"Palsson, Master. Gosta Leonard",male,2,3,1,349909,21.075,,S
    [10] - 9,1,3,"Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)",female,27,0,2,347742,11.1333,,S
    ... (truncated output)

`Source Code <https://github.com/app-generator/app-generator/blob/main/cli/management/commands/tool_csv_processor.py>`__
-------------------------------------------------------------------------------------------------------------------------

The source for the above can be found on GitHub `here <https://github.com/app-generator/app-generator/blob/main/cli/management/commands/tool_csv_processor.py>`__. 
The relevant parts of this simple CSV Processor are: 

**Loads the information** and prior checks the source if is local or remote

.. code-block:: python 

    print( '> Processing ' + ARG_JSON )
    print( '    |-- file: ' + JSON_DATA['source'] )
    print( '    |-- type: ' + JSON_DATA['type'  ] )
    print( '\n')

    tmp_file_path = None 

    if 'http' in JSON_DATA['source']:
        url = JSON_DATA['source']
        r = requests.get(url)
        tmp_file = h_random_ascii( 8 ) + '.csv'
        tmp_file_path = os.path.join( DIR_TMP, tmp_file )
        if not file_write(tmp_file_path, r.text ):
            return
        JSON_DATA['source'] = tmp_file_path
    else:    
        if not file_exists( JSON_DATA['source'] ):
            print( ' > Err loading SOURCE: ' + JSON_DATA['source'] )            
            return

    csv_types = parse_csv( JSON_DATA['source'] )

**Analyze the headers** and maps the detected types to Django Types. For the tabular view, `Tabulate Library` is used:

.. code-block:: python 

    csv_types = parse_csv( JSON_DATA['source'] )
    
    #pprint.pp ( csv_types )
    
    table_headers = ['Field', 'CSV Type', 'Django Types']
    table_rows    = []
    
    for t in csv_types:
        t_type        = csv_types[t]['type']
        t_type_django = django_fields[ t_type ]
        table_rows.append( [t, t_type, t_type_django] )

    print(tabulate(table_rows, table_headers))

The last step is to **Print the CSV data**:

.. code-block:: python 

    csv_data = load_csv_data( JSON_DATA['source'] )
    
    idx = 0
    for l in csv_data:
        idx += 1
        print( '['+str(idx)+'] - ' + str(l) )  

        # Truncate output ..
        if idx == 10:
            print( ' ... (truncated output) ' ) 
            break 

******************************
Resources
******************************

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
