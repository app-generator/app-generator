Configuration
=============

.. title:: Configuration -  Dynamic Django Starter      
.. meta::
    :description: The configuratio layer of Dynamic Django, a powerful tool to manipulate data  
    :keywords: dynamic services configuration, dynamic django configuration, dynamic programming configuration, dynamic patterns configuration

This page explains the core settings of `Dynamic Django Tool <./index.html>`__, a starter that allows to build services with a minimum coding effort. 

.. include::  /_templates/components/signin-invite.rst

Django Specific 
---------------

* **SECRET_KEY**: used to encrypt the sensitive data like browser cookies
* **DEBUG**: True (development) or False (production)
* **ROOT_URLCONF**: main routing file
* **DATABASES**: by default, the SQLite storage is used: `db.sqlite3` (root of the project) 

Project Specific 
----------------

* **UI_TEMPLATES**: local template directory
* **DB Credentials**: optional. If detected, the database switch from the default SQLite to the speficied DBMS.

Dynamic Services 
----------------

Dynamic services, the core of this project, empowers the developer to expose services like API endpoints, datatables and charts with zero coding effort and a minimal configuration.  

Dynamic API 
***********

The dynamic API module allows to expose secure API enpoints mapped to any model without coding. 
The syntax uses a dictionary structure where the key is segment added to the `api` URL and the value is the import path of the Model. 

For instance, the default models shipped with the product defines two `API Endpoints <https://dynamic-django.onrender.com/api/>`__ for Sales and Product models: 

- `Product API <https://dynamic-django.onrender.com/api/product/>`__: Live DEMO 
- `Sales API <https://dynamic-django.onrender.com/api/sales/>`__: Live DEMO

.. code-block:: python
    :caption: core/settings.py
    
    # Syntax: URI -> Import_PATH
    DYNAMIC_API = {
        "product": "home.models.Product",
        "sales": "home.models.Sales",
    }

Dynamic DataTables 
******************

This module allows to handle the database information using a powerfull dataTable view with server-side pagination, search, data filters and export function. 

Using the same configuration pattern as for Dynamic API, any model/table defined in the application can be fully managed by a **Powerful DataTable** view enhanced with:

- CRUD - for authenticated users  
- Server side pagination
- Search 
- Filters 
- CSV export   

To visualize the UI and the options, feel free to access 
the DEMOs for `Sales <https://dynamic-django.onrender.com/dynamic-dt/sales/>`__ and `Product <https://dynamic-django.onrender.com/dynamic-dt/product/>`__ models.  

.. code-block:: python
    :caption: core/settings.py

    # Syntax: URI -> Import_PATH
    DYNAMIC_DATATB = {
        "product": "home.models.Product",
        "sales": "home.models.Sales",
    }   

Dynamic Charts  
**************

In order to have the full control over the data, the **Dynamic Charts** feature is a must. 
The configuration that enables the visual reports on any table is the one listed below.

All registered models can be showcased using different chart types: **Line**, **Bar**, **Radar**, **Donut** .. etc. 
The starter also allows to embed the charts is external systems. Here are some demos: 

- `DONUT Chart <https://dynamic-django.onrender.com/dynamic-charts/sales/?chart_id=8>`__: DEMO Link
- `POLAR Chart <https://dynamic-django.onrender.com/dynamic-charts/sales/?chart_id=10>`__: DEMO Link  
- Embeddable `Pie Chart <https://dynamic-django.onrender.com/dynamic-charts/embed/2/>`__ link (for integration in external systems)

The new charts can be easily added using the creation form where authenticated users defines the correlation between the columns.

.. code-block:: python
    :caption: core/settings.py

    # Syntax: URI -> Import_PATH
    DYNAMIC_CHARTS = {
        "product": "home.models.Product",
        "sales": "home.models.Sales",
    } 

Resources
---------

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
