CSV to DB Table
===============

.. title:: CSV to DataBase Table - Using Dynamic Django Tool      
.. meta::
    :description: Convert any CSV File into a DataBase Table using Dynamic Django Tool  
    :keywords: keywords: cvs processor, csv to database, csv to database table, csv converter, csv to Django Model, dynamic services, dynamic django, dynamic programming, dynamic patterns

This page explains how to translate a **CSV File into a DataBase Table** using `Dynamic Django </docs/developer-tools/dynamic-django/index.html>`__ tool. 

.. include::  /_templates/components/signin-invite.rst

.. include::  /_templates/components/install-dynamic-django.rst

Convert CVS into a Table 
------------------------

Once the tool is properly installed, the next step is to execute **csv-to-model** custom command to process the CSV file. Here are the steps for **Titanic.csv** file, shipped with the tool. 

.. code-block:: bash
    :caption: Convert the CSV to a DB Table 

    python manage.py csv-to-model -i                # STEP #1: Print the help  
    python manage.py csv-to-model -f Titanic.csv -c # STEP #2: Check File integrity 
    python manage.py csv-to-model -f Titanic.csv    # STEP #3: Generate the model definition   
    python manage.py makemigrations                 # STEP #4: Generate Migration SQL 
    python manage.py migrate                        # STEP #5: Apply Changes in DataBase 
    
At this point, we have the CSV file translated into a DataBase Model/Table ready to be used.

Explanation of the steps 
************************

- **STEP #1**: Print the tool help using **-i** argument 
- **STEP #2**: Check the integrity of the CSV file using **-c** argument
- **STEP #3**: Translate the CSV file to a Django model. The definition is also printed in the terminal
- **STEP #4**: Execute **makemigrations** command that generates the SQL code for DB migration  
- **STEP #5**: Apply the Database migration 

Invoke the Model (Django Shell) 
*******************************

The model can be used and provisioned with information using **python manage.py csv-to-model -f Titanic.csv -l** command. 
Please note the **-l** argument that enables the data load.  

.. code-block:: python
    :caption: Access the new Model 

    python manage.py shell 

    >>> from home.models import *
    >>> Titanic.objects.all()
    <QuerySet []>


Video Resources 
---------------

This video material explains how to process CSV files and convert them into secure APIs and server-side data tables using **Dynamic Django** tool.

..  youtube:: cXiUsyi_GJs
    :width: 100%

******************************
Resources
******************************

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
