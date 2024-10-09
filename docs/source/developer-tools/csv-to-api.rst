CSV to API
==========

.. title:: CSV to API - Using Dynamic Django Tool      
.. meta::
    :description: Convert any CSV File into a Secure API using Dynamic Django Tool  
    :keywords: cvs processor, csv to api, csv to secure api, csv to DRF, csv to Django API, dynamic api, dynamic services, dynamic django, dynamic programming, dynamic patterns

This page explains how to convert a **CSV File** into a Secured API using `Dynamic Django </docs/developer-tools/dynamic-django/index.html>`__ tool. 

.. include::  /_templates/components/signin-invite.rst

.. include::  /_templates/components/install-dynamic-django.rst

Convert CVS to Model 
--------------------

Once the tool is properly installed, we need to use the "csv-to-model" custom command to process the CSV file. Here are the steps for **Titanic.csv** file, shipped with the tool. 

.. code-block:: bash
    :caption: Convert the CSV to a DB Table 

    python manage.py csv-to-model -i                  # STEP #1: Print the help  
    python manage.py csv-to-model -f Titanic.csv -c   # STEP #2: Check CSV file integrity (-c argument)
    python manage.py csv-to-model -f Titanic.csv      # STEP #3: Generate the model in home/models.py   
    python manage.py makemigrations                   # Generate Migration SQL in home/migrations
    python manage.py migrate                          # Apply Changes in DataBase 
    python manage.py csv-to-model -f Titanic.csv -l   # (Optional) Load data in Database (-l argument)
    
At this point, we have the CSV file translated into a DataBase model and the information loaded (if the last step was executed)

To activate a secure API Enpoint for the new model, we need to edit the project configuration as suggested below. 

.. code-block:: python
    :caption: Edit Configuration: Activate Dynamic API for the generated model 

    # Syntax: URI -> Import_PATH
    DYNAMIC_API = {
        "product": "home.models.Product",
        "sales": "home.models.Sales",
        "titanic": "home.models.Titanic",  # <-- NEW 
    }         

- **The new endpoint** is now listed in the **Dynamic API** and ready to be used: **http://localhost:8000/dynamic-dt/titanic/** 

.. image:: https://github.com/user-attachments/assets/a4d4c311-10cb-4682-a9bd-7fa61be3febe
   :alt: CSV File coverted to a Secured API managed by Django and DRF (Django REST Framework) 

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
