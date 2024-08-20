`Django Datta Able PRO </product/datta-able-pro/django/>`__
===========================================================

.. title:: Django Datta Able PRO - Premium Django SaaS Template 
.. meta::
    :description: Premium Django Template crafted on top of Datta Able, PRO Version
    :keywords: django, datta pro, datta able pro, premium starter, saas starter, django template, datta able, bootstrap 4, django template

**Open-Source Django Template** built with a minimum set of features on top of **Datta Able**, a modern dashboard design from CodedThemes. 
This template can be used to start a new project quickly by adding new features on top of the existing ones or simply for learning purposes.

- 👉 `Datta Able Django PRO </product/datta-able-pro/django/>`__ - `Product page` 
- 👉 `Datta Able Django PRO <https://django-datta-pro.onrender.com/>`__ - `LIVE demo` 

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

- `Product Page </product/datta-able-pro/django/>`__ - requires `authentication </users/signin/>`__

Once the download is complete, the project can be opened in VsCode. 

.. code-block:: bash

    $ unzip django-datta-able-pro.zip
    $ cd django-datta-able-pro       

Start in Docker 
---------------

Te fastest way to see the product running in the browser is to start Django Datta Able in Docker: 

.. code-block:: bash  

    docker-compose up --build 

If Docker is properly installed in the system, you can visit the browser at **http://localhost:5085**. Datta Able should be up and running. 

Manual Build   
------------

This section presents all steps to start Django Datta Able manually. 

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
- **Home**: the application that integrates the Datta Able Design 
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

   extend-add-page
