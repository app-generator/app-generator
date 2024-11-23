:og:description: Django AdminLTE - Open-source Starter styled with AdminLTE design
:og:image: https://app-generator.dev/static/product/adminlte/django/top.png
:og:image:alt: Django AdminLTE - Open-source Starter styled with AdminLTE design

`AdminLTE </product/adminlte/django/>`__ 
=========================================

.. title:: Django AdminLTE - Open-source Starter styled with AdminLTE design     
.. meta::
    :description: Open-source Django Template styled with AdminLTE design  
    :keywords: django, django template, django starter, adminlte, adminlte django 

**Django AdminLTE** is an open-source starter built with basic modules, authentication and Docker support on top of the AdminLTE Design.

- 👉 `Django AdminLTE </product/adminlte/django/>`__ - Product Page (contains download link)
- 👉 `Django AdminLTE <https://adminlte-django.appseed-srv1.com/>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
--------

- Simple, Easy-to-Extend codebase
- `AdminLTE </docs/templates/bootstrap/adminlte.html>`__ Full Integration 
- Bootstrap 4 Styling 
- Session-based Authentication
- DB Persistence: SQLite
- Docker 
- CI/CD integration for Render 

.. image:: https://github.com/app-generator/django-adminlte/assets/51070104/8f0c396d-2f33-46b9-9689-2982c987399d
   :alt: Django AdminLTE - Open-source Starter styled with AdminLTE design 


`Download Django AdminLTE </product/adminlte/django/>`__
--------------------------------------------------------

The product can be downloaded from the `official product page </product/adminlte/django/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/django-adminlte.git
    cd django-adminlte

Once the source code is available in the local filesystem, the next step is to start it and use provided features. 

.. code-block:: bash
    :caption: Project Files

    < Project ROOT > 
        |
        |
        |-- core/                            
        |    |-- settings.py                  # Project Configuration  
        |    |-- urls.py                      # Project Routing
        |
        |-- home/
        |    |-- views.py                     # APP Views 
        |    |-- urls.py                      # APP Routing
        |    |-- models.py                    # APP Models 
        |    |-- tests.py                     # Tests  
        |    |-- templates/                   # Theme Customisation 
        |         |-- includes                # 
        |              |-- custom-footer.py   # Custom Footer      
        |     
        |-- requirements.txt                  # Project Dependencies
        |
        |-- env.sample                        # ENV Configuration (default values)
        |-- manage.py                         # Start the app - Django default start script


Building the project
--------------------

It's best to use a Python Virtual Environment for installing the project dependencies. You can use the following
code to create the virtual environment

.. code-block:: bash

    virtualenv env

To activate the environment execute **env\Scripts\activate.bat** for Windows or **source env/bin/activate** on Linux-based operating systems. 

Having the `VENV` active, we can proceed and install the project dependencies:

.. code-block:: bash

    pip install -r requirements.txt

Core Dependencies
-----------------

The starter requires the following in order to be succesfully started: 

- Python 3.10 (or above)
- (Optional) Git command line - used by the versioning system 
- (Optional) MySql or PostgreSQL DB Servers 
  - if the default SQLite is not enough
- A modern code editor like VsCode or Sublime 

The python version can be easily check in the terminal by typing: 

.. code-block:: bash

    python --version
    Python 3.12.0

Environment Settings  
--------------------

The starter loads the environment variables from `.env` file. Here are the critical ones: 

- **DEBUG**: set by default to False (development mode)
- **SECRET_KEY**: a random value used by Django to secure sensitive information like passwords and cookie information 
- **Database** Credentials: `DB_ENGINE`, `DB_USERNAME`, `DB_PASS`, `DB_HOST`, `DB_PORT`, `DB_NAME`
    - if detected, the database is switched automatically from the default SQLite to the specified DBMS  

Setting up the Database
-----------------------

**By default**, the application **uses SQLite** for persistence. In order to use `MySql`/`PostgreSQL`, you'll need to install the Python driver(s):

.. code-block:: bash

    pip install mysqlclient # for MySql
    # OR 
    pip install psycopg2    # for PostgreSQL

To connect the application with your mySQL database, you'll need to fill in the credentials
int the `.env` file and run the migrations.

.. code-block:: text
    :caption: .env

    DB_ENGINE=mysql
    # OR 
    DB_ENGINE=postgresql

    # DB credentials below
    DB_HOST=localhost
    DB_NAME=<DB_NAME_HERE>
    DB_USERNAME=<DB_USER_HERE>
    DB_PASS=<DB_PASS_HERE>
    DB_PORT=3306

Use the following commands to seed your data:

.. code-block:: bash

    python manage.py makemigrations
    python manage.py migrate

Running the project
-------------------

You can run **Django AdminLTE** locally or deploy it on `Render`. If you want to run the server locally, you'll need to run the following command:

.. code-block:: bash

    python manage.py createsuperuser
    python manage.py runserver

Open `localhost` on your browser and you can interact with the application. 

.. _localhost: http://127.0.0.1:8000/

.. image:: https://github.com/user-attachments/assets/4d5f6b17-3b80-469b-ade7-2b8e318f829d
   :alt: Homepage Django AdminLTE - open-source starter built on top of AdminLTE 

Contents
--------

.. toctree::
   :maxdepth: 1

   source-code 
   deployment
