:og:description: Django Berry PRO - Premium Starter built on top of Berry 
:og:image: https://user-images.githubusercontent.com/51070104/215728155-9b9cfe26-96e8-49c3-8a08-131d96f4f2eb.png
:og:image:alt: Django Berry PRO - Premium Starter built on top of Berry 

`Berry PRO </product/berry-dashboard-pro/django/>`__
=====================================================

.. title:: Django Berry PRO - Premium Starter built on top of Berry     
.. meta::
    :description: Premium Django Template styled with Berry design  
    :keywords: django, django pro template, django pro starter, Berry pro, Berry django 

Premium Django and Bootstrap 5 Starter enhanced with OAuth, API, Charts, DataTables, Extended User Profiles, Media Files Manager, and Docker support. 
The product is built on top of Berry Dashboard, a premium design from CodedThemes.

- 👉 `Django Berry PRO </product/berry-dashboard-pro/django/>`__ - Product Page (contains download link)
- 👉 `Django Berry PRO <https://django-berry-pro.onrender.com/dashboard/>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst

Features
------------

* **Simple, Easy-to-Extend** Codebase
* **Berry PRO** Design - Bootstrap 5 Design 
* **Extended User Profile**
* `API <https://django-berry-pro.onrender.com/api/sales/>`__ via DRF 
* `Charts <https://django-berry-pro.onrender.com/charts/>`__ via ApexJS 
* `DataTables <https://django-berry-pro.onrender.com/tables/>`__: Server-side Pagination, Search, Filters, Export
* **File Manager**
* **Celery** (async tasks)
* **Docker**
* **Deployment-Ready** for Render 

.. image:: https://user-images.githubusercontent.com/51070104/215728155-9b9cfe26-96e8-49c3-8a08-131d96f4f2eb.png
   :alt: Django Berry PRO - Premium Starter built on top of Berry PRO Design


.. include::  /_templates/components/django-prerequisites.rst


Download Source Code 
--------------------

Access the `product page </product/berry-dashboard-pro/django/#pricing>`__ and complete the purchase. 
Unpack the ZIP archive and folow these steps:

.. code-block:: shell

    unzip django-berry-pro.zip
    cd django-berry-pro
    
Once the source code is unzipped, the next step is to start it and use provided features.     


.. include::  /_templates/components/start-in-docker.rst


Codebase  
--------

The project is coded using a simple and intuitive structure presented below:

.. code-block:: bash
    :caption: Project Files

    < PROJECT ROOT >
        |
        |-- core/              # Implements app configuration
        |    |-- settings.py   # Defines Global Settings
        |    |-- wsgi.py       # Start the app in production
        |    |-- urls.py       # Define URLs served by all apps/nodes
        |
        |-- home/              # Serves all pages from the UI Kit  
        |
        |-- apps/
        |    |
        |    |-- common/       # Assets used by all APPS (models, helpers)
        |    |-- users/        # Handles Auth Flow
        |    |-- api/          # DRF API
        |    |-- charts/       # Charts APP
        |    |-- tables/       # DataTables APP
        |    |-- tasks/        # Celery App
        |
        |-- templates/         # Pages & Templates   
        |-- assets/            # Static Assets [ JS, CSS, images ]   
        |
        |-- requirements.txt   # Development modules - SQLite storage
        |
        |-- .env               # Environment
        |-- env.sample         # Environment Sample
        |
        |-- manage.py          # Django Manager File


.. include::  /_templates/components/django-manual-build.rst

.. image:: https://user-images.githubusercontent.com/51070104/215728155-9b9cfe26-96e8-49c3-8a08-131d96f4f2eb.png
   :alt: Homepage Django Berry PRO - open-source starter built on top of Berry PRO 


.. include::  /_templates/components/django-create-users.rst

    
Contents
--------

.. toctree::
   :maxdepth: 1
   
   deployment
