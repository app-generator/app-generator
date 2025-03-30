:og:description: Dynamic DataTables - Manage information with ease via pagination, search, and filters without coding
:og:image: https://github.com/user-attachments/assets/6c241f56-3e99-4b6d-a1fe-05fb595c1c99
:og:image:alt: Open-Source pattern that allows to manage the information secure via server-side tables

Dynamic DataTables
==================

.. title:: Dynamic DataTables - Manage information with ease via pagination, search, and filters without coding 
.. meta::
    :description: Open-Source pattern that allows to manage the information secure via server-side tables 
    :keywords: dynamic tables, datatables, dynamic services, dynamic table tool, dynamic programming

This page explains Dynamic DataTables, a programming pattern that allows to manage large amount of data without coding. 
This tool can be used for any model defined in the project for adding, delete, update, search and filter the information via a paginated table view. 

- `Django Datta Able </product/datta-able/django/>`__ - Django Starter that includes `Dynamic DataTables Sample <https://django-datta.onrender.com/dynamic-dt/product/>`__  
- `Django Rocket HTMX </product/rocket-htmx/django/>`__ - Django & HTMX sample of `Dynamic DataTables Sample <https://rocket-django-htmx.onrender.com/>`__  
- `Flask Able Django </product/datta-able/flask/>`__ - Free **Flask Starter**  that incorporates the `Dynamic DataTables Sample <https://flask-datta-demo.onrender.com/dynamic-dt>`__

.. include::  /_templates/components/signin-invite.rst


Features
--------

- `Minimal Configuration` (single line in config for each model)
- `Handles any model` defined across the project
- Search, Pagination 
- Server-Side processing 
- Export (CSV)

.. figure:: https://github.com/user-attachments/assets/6c241f56-3e99-4b6d-a1fe-05fb595c1c99
   :alt: Dynamic DataTables - Manage information with ease via pagination, search, and filters without coding

How to use it
-------------

Download a starter that supports the Dynamic Tables concept: 

- `Django Datta Able </product/datta-able/django/>`__   
- `Django Rocket HTMX </product/rocket-htmx/django/>`__ 
- `Flask Able Django </product/datta-able/flask/>`__ 

.. code-block:: shell
    
    $ unzip django-datta-able.zip
    $ cd django-datta-able

This documentation is provided for the **Django Datta Able** starter.  


Update Configuration
--------------------

The dynamic data table module works with any model defined in the project.

.. code-block:: python 
    :caption: config/settings.py

    DYNAMIC_DATATB = {
        # SLUG -> Import_PATH 
        'product'  : "apps.pages.models.Product",
    }

The above code enables the dynamic module for the **Product** model, defined in **apps.pages.models.py**.

In order to execute successfully this set up, make sure the model exists and the database is migrated. 


Access Dynamic Tables Page 
--------------------------

All models handled by the dynamic module are listed in the `/dynamic-dt/` page. The dynamic view uses a dynamic URL, as specified in the configuration:

- https://django-datta.onrender.com/dynamic-dt/product/

.. figure:: https://github.com/user-attachments/assets/6c241f56-3e99-4b6d-a1fe-05fb595c1c99
   :alt: Dynamic DataTables - Manage information with ease via pagination, search, and filters without coding

.. include::  /_templates/components/footer-links.rst
