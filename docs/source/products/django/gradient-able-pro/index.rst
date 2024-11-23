:og:description: Django Gradient Able PRO - Premium Django SaaS Template
:og:image: https://app-generator.dev/static/product/gradient-able-pro/django/top.png
:og:image:alt: Django Gradient Able PRO - Premium Django SaaS Template

`Gradient Able PRO </product/gradient-able-pro/django/>`__
=================================================================

.. title:: Django Gradient Able PRO - Premium Django SaaS Template 
.. meta::
    :description: Premium Django Template crafted on top of Gradient Able, PRO Version
    :keywords: django, gradient pro, gradient able pro, premium starter, saas starter, django template, gradient able, bootstrap 4, django template

Premium Django and Bootstrap 5 Starter enhanced with OAuth, API, Charts, DataTables, Extended User Profiles, Media Files Manager, and Docker support. 
**Gradient Able** design is a premium dashboard UI provided by CodeThemes.

- 👉 `Gradient Able Django PRO </product/gradient-able-pro/django/>`__ - `Product page` 
- 👉 `Gradient Able Django PRO <https://django-gradient-pro.onrender.com/>`__ - `LIVE demo` 

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
- `DataTables <https://django-gradient-pro.onrender.com/tables/>`__
- `Charts <https://django-gradient-pro.onrender.com/charts/>`__
- Celery (Async Tasks)
- File Manager
- `Docker`
- `Automated e2e Tests <#tests>`__ - reports generated in `HTML and Video` format 

.. figure:: https://user-images.githubusercontent.com/51070104/216759901-7b3a6c50-b224-4ae2-922c-3cb4648a5802.png
   :alt: Gradient Able PRO - Premium Django Starter and SaaS Template

Prerequisites
-------------

A few tools need to be installed in the system to use the starter efficiently:

- `Python <https://www.python.org/>`__ 
- A modern code editor like `VsCode <https://code.visualstudio.com/>`__, or `Sublime <https://www.sublimetext.com/>`__
- (optional) `GIT <https://git-scm.com/>`__ - for pulling the source code and work under a version control system 
- (optional) `Docker <https://www.docker.com/>`__ for isolated execution 
- (optional) DB Servers: 
  - `MySql <https://www.mysql.com/>`__ 
  - `PostgreSQL <https://www.postgresql.org/>`__ 


Download Sources 
----------------

The **product can be downloaded** from the official page - requires a `purchase <https://gumroad.com/l/LqPVM/>`__

- `Product Page </product/gradient-able-pro/django/>`__ - requires `authentication </users/signin/>`__

Once the download is complete, the project can be opened in VsCode. 

.. code-block:: bash

    $ unzip django-gradient-able-pro.zip
    $ cd django-gradient-able-pro       

Start in Docker 
---------------

Te fastest way to see the product running in the browser is to start Django Gradient Able in Docker: 

.. code-block:: bash  

    docker-compose up --build 

If Docker is properly installed in the system, you can visit the browser at **http://localhost:5085**. Gradient Able should be up and running. 

Manual Build   
------------

This section presents all steps to start Django Gradient Able manually. 

.. code-block:: bash  

    virtualenv env                      # Create a Virtual Environment 
    source env/bin/activate             # Activate the environment 
    pip install -r requirements.txt     # Install modules 
    python manage.py makemigrations     # Migrate DataBase (generate tables) 
    python manage.py migrate            # Apply Changes on Database 

The project environment and database are ready to be used. The last thing is to start the application: 


.. code-block:: bash  

    python manage.py runserver          # Starts on default PORT 8000
    python manage.py runserver 8999     # Starts on PORT 8999 (custom port)

By default Django starts on port **8000** but this can be easily changed by adding the PORT number as argument. 
At this point, the app runs at **http://127.0.0.1:8000/**


Codebase  
--------

The project is coded using a simple and intuitive structure presented below:

- **Core**: holds the project settings 
- **Home**: the application that integrates the Gradient Able Design 
- **Api**: the generated API 

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


Create Users
------------

By default, the app redirects guest users to authenticate. In order to access the private pages, follow this set up: 

- Start the app
- Access the `registration` page and create a new user:
  - `http://127.0.0.1:8000/register/`
- Access the `sign in` page and authenticate
  - `http://127.0.0.1:8000/login/`


Start Celery (async tasks)
--------------------------

- Make sure you have a Redis Server running: `redis://localhost:6379`
  - `$ redis-cli` and type `ping` 
- In the base directory inside `tasks_scripts` folder you need to write your scripts file.
- Run the celery command from the CLI.

.. code-block:: bash  

    export DJANGO_SETTINGS_MODULE="core.settings"  
    celery -A apps.tasks worker -l info -B

- You will see a new route `Apps -> Tasks` in the sidebar.
- You can start and cancel any task from the UI.


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

.. include::  /_templates/components/footer-links.rst
