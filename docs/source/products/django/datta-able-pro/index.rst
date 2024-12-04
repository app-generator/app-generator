:og:description: Django Datta Able PRO - Premium Django SaaS Template
:og:image: https://app-generator.dev/static/product/datta-able/django/top.png
:og:image:alt: Django Datta Able PRO - Premium Django SaaS Template

`Datta Able PRO </product/datta-able-pro/django/>`__
===========================================================

.. title:: Django Datta Able PRO - Premium Django SaaS Template 
.. meta::
    :description: Premium Django Template crafted on top of Datta Able, PRO Version
    :keywords: django, datta pro, datta able pro, premium starter, saas starter, django template, datta able, bootstrap 4, django template

Premium Django and Bootstrap 5 Starter enhanced with OAuth, API, Charts, DataTables, Extended User Profiles, Media Files Manager and Docker support.
**Datta Able** design is a premium dashboard UI provided by CodeThemes.

- 👉 `Datta Able Django PRO </product/datta-able-pro/django/>`__ - Product Page (contains download link)
- 👉 `Datta Able Django PRO <https://django-datta-pro.onrender.com/>`__ - LIVE Demo 
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features 
--------

- `Up-to-date dependencies`
- Database: `SQLite` (default), PgSQL, MySql
- **Authentication**
  - `Session-Based authentication`
  - `Social Login`: **Github**
- **User Extended profile**
- **API** via DRF
- `DataTables <https://django-datta-pro.onrender.com/tables/>`__
- `Charts <https://django-datta-pro.onrender.com/charts/>`__
- Celery (Async Tasks)
- File Manager
- `Docker`
- `Automated e2e Tests <#tests>`__ - reports generated in `HTML and Video` format 

.. figure:: https://user-images.githubusercontent.com/51070104/170474361-a58da82b-fff9-4a59-81a8-7ab99f478f48.png
   :alt: Datta Able PRO - Premium Django Starter and SaaS Template


.. include::  /_templates/components/django-prerequisites.rst


Download Source Code 
--------------------

Access the `product page </product/datta-able-pro/django/#pricing>`__ and complete the purchase. 
Unpack the ZIP archive and folow thhe installation steps:

.. code-block:: shell

    unzip django-datta-able-pro.zip
    cd django-datta-able-pro

Once the source code is unzipped, the next step is to start it and use provided features.     


.. include::  /_templates/components/start-in-docker.rst


Codebase  
--------

The project is coded using a simple and intuitive structure presented below:

- **Core**: holds the project settings 
- **Home**: the application that integrates the Datta Able Design 
- **Api**: the generated API 

.. code-block:: bash   

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

.. figure:: https://user-images.githubusercontent.com/51070104/170474361-a58da82b-fff9-4a59-81a8-7ab99f478f48.png
   :alt: Datta Able PRO - Premium Django Starter and SaaS Template


.. include::  /_templates/components/django-create-users.rst


.. include::  /_templates/components/django-start-celery.rst


Enable Social Login 
-------------------

  👉 **Github Setup** - `Create an OAuth App <https://docs.github.com/en/developers/apps/building-oauth-apps/creating-an-oauth-app>`__

- SignIN to `Github`
- Access `Settings` -> `Developer Settings` -> `OAuth Apps`
- Edit your OAuth App
  - `App Name`
  - `App Description`
  - (mandatory) `HomePage`: `https://localhost:8000`
  - (mandatory) `Authorization callback URL`: `https://localhost:8000/`
  - Generate a new `secret key`


Tests
-----

**Software Prerequisites**: (Docker & NodeJS)

- Check Docker installation by typing `docker info` on a terminal screen. 
- Install NodeJS `v20.5.0` or above.
  - check the installation via `node --version`

**Running** `tests` on **Linux/macOS**

.. code-block:: bash  
    
    test.sh


**Running** `tests` on **Windows**

.. code-block:: bash  
    
    test.bat

The testing report is saved in the `test_reports` directory in **HTML and Video Format**.

Resources
---------

.. toctree::
   :maxdepth: 1

   extend-adding-page
