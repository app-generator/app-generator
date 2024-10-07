CSV Processor
=============

.. title:: CSV Loader and Processor -  Dynamic Django Starter      
.. meta::
    :description: Parse CSV files, generate Django Models and load information via Dynamic Django  
    :keywords: csv to code, csv to database, csv loader, csv to Django model, dynamic django, dynamic programming, dynamic patterns

This page explains how to use the **CSV Loader and Processor** feature of `Dynamic Django Tool <./index.html>`__ that allows to convert CSV files to Django Models and (optional) loads the information.

.. include::  /_templates/components/signin-invite.rst

Tool Syntax 
-----------

The CSV Processor can be invoked in the console using **csv-to-model** command. Here are the inputs expected by the tool:

- **-i**: Prints the help 
- **-f**: The CSV file to process that needs to be saved in the MEDIA directory
- **-c**: Check the file for integrity
- **-l**: Loads the data in the database 
- **-d**: Truncate table before the load 
- **-t**: Limit the load to N lines 
- **-m**: configure the conversion of the fields  

.. code-block:: bash
    :caption: Help Output 

    python manage.py csv-to-model -i

    > HELP: CLI for CSV to Model translation (plus load)
        -i (or --info)       : Print this help, and exit
        -f                   : Input CSV File (input or remote)
        -c (or --check)      : Check Input (CSV) files for integrity (fix if neccessary)
        -s (or --simulation) : Simulates the CVS to Model translation (nothing is write on the disk)
        -l (or --load)       : Load CSV data into associated models
        -t                   : Nbr of lines to load (default=99k)
        -d (or --del)        : Wipe, delete models data
        -m <MAPPER.json>     : Specify a new Mapper file to be used    

Generate a Model  
----------------

The CVS file used to generate the corespondent model needs to be saved in the MEDIA directory. 
For tests, the starter comes with two CSV files that we can use to load data into the database: 

- media/Refunds.csv 
- media/Titanic.csv 

For this demonstration, we will use the Titanic.csv. Of course, we can check the file and also simulate the CSV to model translation. 

.. code-block:: bash
    :caption: Check and Simulate the Conversion 

    python manage.py csv-to-model -f Titanic.csv -c 

    Generate Models FROM multiple CVSs
    > Using Mapper [mapper.json], version v1
    > CVS: Titanic.csv
    > Check INPUT
    > PROCESSING: media/Titanic.csv    

    python manage.py csv-to-model -f Titanic.csv -s

    Generate Models FROM multiple CVSs
    > Using Mapper [mapper.json], version v1
    > CVS: Titanic.csv
    > SIMULATION mode
    > TABLE: Titanic -> ISOLATED
        -> PassengerId models.IntegerField(blank=True, null=True) (detected)
        -> Survived models.IntegerField(blank=True, null=True) (detected)
        -> Pclass models.IntegerField(blank=True, null=True) (detected)
        -> Name models.TextField(blank=True, null=True) (detected)
        -> Sex models.TextField(blank=True, null=True) (detected)
        -> Age models.FloatField(blank=True, null=True) (detected)
        -> SibSp models.IntegerField(blank=True, null=True) (detected)
        -> Parch models.IntegerField(blank=True, null=True) (detected)
        -> Ticket models.TextField(blank=True, null=True) (detected)
        -> Fare models.FloatField(blank=True, null=True) (detected)
        -> Cabin models.TextField(blank=True, null=True) (detected)
        -> Embarked models.TextField(blank=True, null=True) (detected)    

If the output looks good, we can proceed with the CSV-to-Model conversion 

.. code-block:: bash
    :caption: Check and Simulate the Conversion 

    python manage.py csv-to-model -f Titanic.csv

    Generate Models FROM multiple CVSs
    > Using Mapper [mapper.json], version v1
    > CVS: Titanic.csv
    > PROCESSING Titanic.csv
    > Model: Titanic from Titanic.csv
    *** GENERATE Model
    > GENERATE [Titanic]
    -> Field [PassengerId], type = models.IntegerField(blank=True, null=True)
    -> Field [Survived], type = models.IntegerField(blank=True, null=True)
    -> Field [Pclass], type = models.IntegerField(blank=True, null=True)
    -> Field [Name], type = models.TextField(blank=True, null=True)
    -> Field [Sex], type = models.TextField(blank=True, null=True)
    -> Field [Age], type = models.FloatField(blank=True, null=True)
    -> Field [SibSp], type = models.IntegerField(blank=True, null=True)
    -> Field [Parch], type = models.IntegerField(blank=True, null=True)
    -> Field [Ticket], type = models.TextField(blank=True, null=True)
    -> Field [Fare], type = models.FloatField(blank=True, null=True)
    -> Field [Cabin], type = models.TextField(blank=True, null=True)
    -> Field [Embarked], type = models.TextField(blank=True, null=True)

    class Titanic(models.Model):
            id = models.AutoField(primary_key=True)
            PassengerId = models.IntegerField(blank=True, null=True)
            Survived = models.IntegerField(blank=True, null=True)
            Pclass = models.IntegerField(blank=True, null=True)
            Name = models.TextField(blank=True, null=True)
            Sex = models.TextField(blank=True, null=True)
            Age = models.FloatField(blank=True, null=True)
            SibSp = models.IntegerField(blank=True, null=True)
            Parch = models.IntegerField(blank=True, null=True)
            Ticket = models.TextField(blank=True, null=True)
            Fare = models.FloatField(blank=True, null=True)
            Cabin = models.TextField(blank=True, null=True)
            Embarked = models.TextField(blank=True, null=True)

    -> File saved OK

The new model is generated in the `HOME` application. The next step is to migrate the Database 

Migrate the Database   
--------------------

The **Titanic** model is now saved in **home/models.py**, and we need to execute the migration steps: 

.. code-block:: bash
    :caption: Migrate Database

    python manage.py makemigrations

    Migrations for 'home':
    home/migrations/0002_titanic.py
        - Create model Titanic    

    python manage.py migrate  

    Running migrations:
        Applying home.0002_titanic... OK    


Test the new Model    
------------------

We can double check the process by importing the model in the Django Shell 

.. code-block:: python
    :caption: Access the new Model 

    python manage.py shell 

    >>> from home.models import *
    >>> Titanic.objects.all()
    <QuerySet []>

Load CSV Data     
-------------

The information can be easily loaded using the options:

- **-l**: Loads the data in the database 
- **-d**: Truncate table before the load 
- **-t**: Limit the load to N lines 

.. code-block:: python
    :caption: Load CSV data into Database (only 10 lines)

    python manage.py csv-to-model -f Titanic.csv -ld -t 10 

    Generate Models FROM multiple CVSs
    > load_limit: 10
    > Using Mapper [mapper.json], version v1
    > CVS: Titanic.csv
    > CVSs: ['Titanic.csv']
    > *** *** ***
    > PROCESSING Titanic.csv
    > Model: Titanic from Titanic.csv
    > Input data into [Titanic] from [Titanic.csv]
    > DELETE data trigered for [home.models.Titanic]
    > ...done
    > [12] CSV Headers: ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
        Line [1][ > 12 fields ['1', '0', '3', 'Braund, Mr. Owen Harris', 'male', '22', '1', '0', 'A/5 21171', '7.25', '', 'S']
        Line [2][ > 12 fields ['2', '1', '1', 'Cumings, Mrs. John Bradley (Florence Briggs Thayer)', 'female', '38', '1', '0', 'PC 17599', '71.2833', 'C85', 'C']
        Line [3][ > 12 fields ['3', '1', '3', 'Heikkinen, Miss. Laina', 'female', '26', '0', '0', 'STON/O2. 3101282', '7.925', '', 'S']
        Line [4][ > 12 fields ['4', '1', '1', 'Futrelle, Mrs. Jacques Heath (Lily May Peel)', 'female', '35', '1', '0', '113803', '53.1', 'C123', 'S']
        Line [5][ > 12 fields ['5', '0', '3', 'Allen, Mr. William Henry', 'male', '35', '0', '0', '373450', '8.05', '', 'S']
        Line [6][ > 12 fields ['6', '0', '3', 'Moran, Mr. James', 'male', '', '0', '0', '330877', '8.4583', '', 'Q']
        Line [7][ > 12 fields ['7', '0', '1', 'McCarthy, Mr. Timothy J', 'male', '54', '0', '0', '17463', '51.8625', 'E46', 'S']
        Line [8][ > 12 fields ['8', '0', '3', 'Palsson, Master. Gosta Leonard', 'male', '2', '3', '1', '349909', '21.075', '', 'S']
        Line [9][ > 12 fields ['9', '1', '3', 'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)', 'female', '27', '0', '2', '347742', '11.1333', '', 'S']
        Line [10][ > 12 fields ['10', '1', '2', 'Nasser, Mrs. Nicholas (Adele Achem)', 'female', '14', '1', '0', '237736', '30.0708', '', 'C']
    > STATS: 
        TOTAL Lines       : 891
        Imported          : 891
        Warnings          : 0
        Errors            : 0
        Unprocessed Lines : []
    > EXIT    

Visualize the CSV Data      
----------------------

We can quickly check out the information usind the Django Shell or enable the **Dynamic DataTable** view for the generated model. 
Let's try both: 

.. code-block:: python
    :caption: Access the new Model 

    python manage.py shell 

    >>> from home.models import *
    >>> Titanic.objects.all()
    <QuerySet [<Titanic: Titanic object (1)>, <Titanic: Titanic object (2)>, <Titanic: Titanic object (3)>, <Titanic: Titanic object (4)>, <Titanic: Titanic object (5)>, <Titanic: Titanic object (6)>, <Titanic: Titanic object (7)>, <Titanic: Titanic object (8)>, <Titanic: Titanic object (9)>, <Titanic: Titanic object (10)>]>
    >>> Titanic.objects.all()[0].Name 
    'Braund, Mr. Owen Harris'

We can see the new information correctly loaded in the database. 

Enable the `Dynamic DT <./datatables.html>`__ View      
--------------------------------------------------

For this, we need to add a single line of code in **settings.DYNAMIC_DATATB** file 

.. code-block:: python
    :caption: core/settings.py

    # Syntax: URI -> Import_PATH
    DYNAMIC_DATATB = {
        "product": "home.models.Product",
        "sales": "home.models.Sales",
        "titanic": "home.models.Titanic", <-- NEW 
    }

The effect is reflected automatically in the ui and we can access the generated Dynamic Table: 

.. image:: https://github.com/user-attachments/assets/fe97ce7c-28ec-4fad-97c7-a80cbb5165db
   :alt: CSV Loader and Processor - Generate Django models from CSV, integrate in Dynamic Datatables  

**On access, we can see the CSV data loaded by the Dynamic DataTable module without any coding**.  

.. image:: https://github.com/user-attachments/assets/dec5fbd4-ba19-45bd-93ee-fba708632e65
   :alt: Dynamic Django - Dynamic Programming concepts applied in Python/Django: APIs, DataTables, Charts 

Resources
---------

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
