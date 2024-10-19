CSV to DataTable 
================

.. title:: CSV to DataTable - Using Dynamic Django Tool      
.. meta::
    :description: Convert any CSV File into a powerfull Server-Side DataTable using Dynamic Django Tool  
    :keywords: cvs processor, csv to datatable, csv to server-side datatable, csv to Django App, dynamic datatable, dynamic services, dynamic django, dynamic programming, dynamic patterns

This page explains how to convert a **CSV File** into a powerfull Server-Side DataTable using `Dynamic Django </docs/developer-tools/dynamic-django/index.html>`__ tool. 

.. include::  /_templates/components/banner-top.rst

.. include::  /_templates/components/install-dynamic-django.rst

Convert CVS to DataTable 
------------------------

Once the tool is properly installed, we need to use the **csv-to-model** custom command to process the CSV file. Here are the steps for **Titanic.csv** file, shipped with the tool. 

.. code-block:: bash
    :caption: Convert the CSV to a DB Table 

    python manage.py csv-to-model -i                # STEP #1: Print the help  
    python manage.py csv-to-model -f Titanic.csv    # STEP #2: Generate the Model    
    python manage.py makemigrations                 # STEP #3: Generate Migration SQL 
    python manage.py migrate                        # STEP #4: Apply Changes in DataBase 
    python manage.py csv-to-model -f Titanic.csv -l # STEP #5: Load Data into DataBase  
    
At this point, we have the CSV file translated into a DataBase model and the information loaded

Explanation of the steps 
************************

- **STEP #1**: Print the tool help information using **-i** argument 
- **STEP #2**: Translate the CSV file to a Django Model. The generated Python code is saved in `home/models.py` file
- **STEP #3**: Execute **makemigrations** command that generates the SQL code for DB migration  
- **STEP #4**: Apply the Database migration 
- **STEP #5**: Loads the content of the CSV file into the generated model 

Configuration Update 
********************

To activate the Dynamic DataTable for the new model, we need to edit the project configuration as suggested below. 

.. code-block:: python
    :caption: Edit Configuration: Activate Dynamic API for the generated model 

    # Syntax: URI -> Import_PATH
    DYNAMIC_DATATB = {
        "product": "home.models.Product",
        "sales": "home.models.Sales",
        "titanic": "home.models.Titanic",  # <-- NEW 
    }         

**The new endpoint** is now listed in the **Dynamic DataTable** index page and ready to be used: **http://localhost:8000/api/titanic/** 

.. image:: https://github.com/user-attachments/assets/dec5fbd4-ba19-45bd-93ee-fba708632e65
   :alt: CSV File converted to a powerful server-side DataTable enhanced with search, filters, export.

Video Resources 
---------------

This video material explains how to process CSV files and convert them into secure APIs and server-side data tables using **Dynamic Django** tool.

..  youtube:: cXiUsyi_GJs
    :width: 100%

.. include::  /_templates/components/footer-links.rst
