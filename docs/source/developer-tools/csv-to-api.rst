CSV to API
==========

.. title:: CSV to API - Using Dynamic Django Tool      
.. meta::
    :description: Convert any CSV File into a Secure API using Dynamic Django Tool  
    :keywords: cvs processor, csv to api, csv to secure api, csv to DRF, csv to Django API, dynamic api, dynamic services, dynamic django, dynamic programming, dynamic patterns

This page explains how to convert a **CSV File into a Secure API** using `Dynamic Django </docs/developer-tools/dynamic-django/index.html>`__ tool. 

.. include::  /_templates/components/banner-top.rst

.. include::  /_templates/components/install-dynamic-django.rst

Convert CVS to Model 
--------------------

Once the tool is properly installed, we need to use the **csv-to-model** custom command to process the CSV file. Here are the steps for **Titanic.csv** file, shipped with the tool. 

.. code-block:: bash
    :caption: Convert the CSV to a DB Table 

    python manage.py csv-to-model -i                # STEP #1: Print the help  
    python manage.py csv-to-model -f Titanic.csv -c # STEP #2: Check CSV file integrity 
    python manage.py csv-to-model -f Titanic.csv    # STEP #3: Generate the Model    
    python manage.py makemigrations                 # STEP #4: Generate Migration SQL 
    python manage.py migrate                        # STEP #5: Apply Changes in DataBase 
    python manage.py csv-to-model -f Titanic.csv -l # STEP #6: (Optional) Load Data 
    
At this point, we have the CSV file translated into a DataBase model and the information loaded (if the last step was executed)

Explanation of the steps 
************************

- **STEP #1**: Print the tool help information using **-i** argument 
- **STEP #2**: Check the integrity of the Titanic.csv, saved in the `media` directory located in the root of the project
- **STEP #3**: Translate the CSV file to a Django model. The generated Python code is added to the `home/models.py` file
- **STEP #4**: Execute **makemigrations** command that generates the SQL code for DB migration  
- **STEP #5**: Apply the Database migration 
- **STEP #6**: Loads the content of the CSV file into the generated model 

Configuration Update 
********************

To activate a secure API Enpoint for the new model, we need to edit the project configuration as suggested below. 

.. code-block:: python
    :caption: Edit Configuration: Activate Dynamic API for the generated model 

    # Syntax: URI -> Import_PATH
    DYNAMIC_API = {
        "product": "home.models.Product",
        "sales": "home.models.Sales",
        "titanic": "home.models.Titanic",  # <-- NEW 
    }         

**The new endpoint** is now listed in the **Dynamic API** index page and ready to be used: **http://localhost:8000/api/titanic/** 

.. image:: https://github.com/user-attachments/assets/5e7562b9-0d50-4cdc-87fc-5cbed2628ed1
   :alt: CSV File converted to a Secured API managed by Django and DRF (Django REST Framework) 

Video Resources 
---------------

This video material explains how to process CSV files and convert them into secure APIs and server-side data tables using **Dynamic Django** tool.

..  youtube:: cXiUsyi_GJs
    :width: 100%

.. include::  /_templates/components/footer-links.rst
