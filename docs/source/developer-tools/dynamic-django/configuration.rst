Configuration
=============

This page explains the core settings of **Dynamic Django**, a starter that allows to build services with a minimum coding effort. 

.. include::  /_templates/components/signin-invite.rst

Django Specific 
---------------

* **SECRET_KEY**: used to encrypt the sensitive data like browser cookies
* **DEBUG**: True (development) or False (production)
* **ROOT_URLCONF**: main routing file

Project Specific 
----------------

* **UI_TEMPLATES**: local template directory
* **DB Credentials**: optional. If detected, the database switch from the default SQLite to the speficied DBMS.

Dynamic Services 
----------------

Dynamic API 
***********

The dynamic API module allows to expose secure API enpoints mapped to any model without coding 

.. code-block:: python

    # Syntax: URI -> Import_PATH
    DYNAMIC_API = {
        "product": "home.models.Product",
        "sales": "home.models.Sales",
    }

Dynamic DataTables 
******************

This module allows to handle the database information using a powerfull dataTable view with server-side pagination, search, data filters and export function. 

.. code-block:: python

    # Syntax: URI -> Import_PATH
    DYNAMIC_DATATB = {
        "product": "home.models.Product",
        "sales": "home.models.Sales",
    }   

Dynamic Charts  
**************

In order to have the full control over the data, the Dynamic Charts feature is a must. The configuration that enables the visual reports on any table is the one listed below: 

.. code-block:: python

    # Syntax: URI -> Import_PATH
    DYNAMIC_CHARTS = {
        "product": "home.models.Product",
        "sales": "home.models.Sales",
    } 

Resources
*********

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
