:og:description: Django Gradient Able PRO - Premium Django SaaS Template
:og:image: https://app-generator.dev/static/product/gradient-able-pro/django/top.png
:og:image:alt: Django Gradient Able PRO - Premium Django SaaS Template

`Gradient Able PRO </product/gradient-able-pro/django/>`__
==========================================================

.. title:: Django Gradient Able PRO - Premium Django SaaS Template 
.. meta::
    :description: Premium Django Template crafted on top of Gradient Able, PRO Version
    :keywords: django, gradient pro, gradient able pro, premium starter, saas starter, django template, gradient able, bootstrap 4, django template

Premium Django and Bootstrap 5 Starter enhanced with OAuth, API, Charts, DataTables, Extended User Profiles, Media Files Manager, and Docker support. 
`Gradient Able </product/gradient-able/>`__ design is a premium dashboard UI provided by `CodedThemes </agency/codedthemes/>`__.

- 👉 `Gradient Able Django PRO </product/gradient-able-pro/django/>`__ - Product Page (contains download link)
- 👉 `Gradient Able Django PRO <https://django-gradient-pro.onrender.com/>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features 
--------

- `Up-to-date dependencies`
- `Gradient Able </product/gradient-able/>`__ Design Integration
- Database: `SQLite` (default), PgSQL, MySql
- **Authentication**
    - `Session-Based authentication`
    - `Social Login`: **Github**
- **User Extended profile**
- **API** via DRF
- `DataTables <https://django-gradient-pro.onrender.com/tables/>`__
- `Charts <https://django-gradient-pro.onrender.com/charts/>`__
- Celery (Async Tasks)
- File Manager
- `Docker`

.. figure:: https://user-images.githubusercontent.com/51070104/216759901-7b3a6c50-b224-4ae2-922c-3cb4648a5802.png
   :alt: Gradient Able PRO - Premium Django Starter and SaaS Template


.. include::  /_templates/components/django-prerequisites.rst


Download Source Code 
--------------------

Access the `product page </product/gradient-able-pro/django/#pricing>`__ and complete the purchase. 
Unpack the ZIP archive and folow thhe installation steps:

.. code-block:: shell

    unzip django-gradient-able-pro.zip
    cd django-gradient-able-pro

Once the source code is unzipped, the next step is to start it and use provided features.     


.. include::  /_templates/components/start-in-docker.rst


Codebase  
--------

The project is coded using a simple and intuitive structure presented below:

.. code-block:: bash   

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
    |
    |-- ************************************************************************


.. include::  /_templates/components/django-manual-build.rst

.. figure:: https://user-images.githubusercontent.com/51070104/216759901-7b3a6c50-b224-4ae2-922c-3cb4648a5802.png
   :alt: Gradient Able PRO - Premium Django Starter and SaaS Template

.. include::  /_templates/components/django-create-users.rst
    
.. include::  /_templates/components/footer-links.rst
     