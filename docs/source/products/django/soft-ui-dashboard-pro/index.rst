:og:description: Django Soft Dashboard PRO - Premium Starter built on top of Soft UI Design
:og:image: https://github.com/user-attachments/assets/828b0f83-1a37-4390-8685-411b4f408cdb
:og:image:alt: Premium Django starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with Soft UI Dashboard Design.

`Soft Dashboard PRO </product/soft-ui-dashboard-pro/django/>`__ 
===============================================================

.. title:: Django Material Dashboard PRO - Premium Starter built on top of Material Dashboard     
.. meta::
    :description: Premium Django starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with Soft UI Design.
    :keywords: django, django pro template, django pro starter, material-dashboard pro, material-dashboard django 

Premium Django starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with `Soft Dashboard PRO </product/soft-ui-dashboard/>` from `Creative-Tim </agency/creative-tim/>`__ using Bootstrap 5 Framework.
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. 

- 👉 `Django Soft Dashboard PRO </product/soft-ui-dashboard-pro/django/>`__ - Product Page (contains download link)
- 👉 `Django Soft Dashboard PRO <https://django-soft-dash-pro.onrender.com>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
--------

- **Simple, Easy-to-Extend** Codebase
- `Soft Dashboard PRO </product/soft-ui-dashboard/>`__ Design Integration 
- **OAuth** - Github
- **Extended User Profile**
- **API** via DRF 
- **Charts** via ApexJS 
- **DataTables**
- **Celery** (async tasks)
- **Deployment-Ready** for Render 

.. image:: https://github.com/user-attachments/assets/828b0f83-1a37-4390-8685-411b4f408cdb
   :alt: Premium Django starter built on top of Bootstrap 5 and Soft Dashboard PRO, a pixel-perfect design from Creative-Tim.


.. include::  /_templates/components/django-prerequisites.rst


Download Source Code 
--------------------

Access the `product page </product/soft-ui-dashboard-pro/django/#pricing>`__ and complete the purchase. 
Unpack the ZIP archive and folow these steps:

.. code-block:: shell

    unzip django-soft-ui-dashboard-pro.zip
    cd django-soft-ui-dashboard-pro

Once the source code is unzipped, the next step is to start it and use provided features.     


.. include::  /_templates/components/start-in-docker.rst


Codebase  
--------

The project is coded using a simple and intuitive structure presented below:

.. code-block:: bash
    :caption: Project Files

    < Project ROOT > 
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

.. image:: https://github.com/user-attachments/assets/828b0f83-1a37-4390-8685-411b4f408cdb
   :alt: Premium Django starter built on top of Bootstrap 5 and Soft Dashboard PRO, a pixel-perfect design from Creative-Tim. 

.. include::  /_templates/components/django-create-users.rst
    
.. include::  /_templates/components/footer-links.rst
