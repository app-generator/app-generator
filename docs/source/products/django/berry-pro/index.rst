:og:description: Django Berry PRO - Premium Starter built on top of Berry 
:og:image: https://user-images.githubusercontent.com/51070104/215728155-9b9cfe26-96e8-49c3-8a08-131d96f4f2eb.png
:og:image:alt: Django Berry PRO - Premium Starter built on top of Berry 

Django Berry PRO
================

.. title:: Django Berry PRO - Premium Starter built on top of Berry     
.. meta::
    :description: Premium Django Template styled with Berry design  
    :keywords: django, django pro template, django pro starter, Berry pro, Berry django 

**Django Berry** is an open-source starter built on top of the Berry Design

- 👉 `Django Berry PRO <https://django-berry-pro.onrender.com/>`__ - LIVE Demo
- 👉 `Django Berry PRO <https://appseed.gumroad.com/l/django-berry-pro>`__ - Purchase Link (Secured by GUMROAD) 

.. include::  /_templates/components/signin-invite.rst

Features
------------

* **Simple, Easy-to-Extend** Codebase
* **Berry PRO** Design - Bootstrap 5 Design 
* **Extended User Profile**
* **API** via DRF 
* **Charts** via ApexJS 
* **DataTables**
* **File Manager**
* **Celery** (async tasks)
* **Deployment-Ready** for Render 

.. image:: https://user-images.githubusercontent.com/51070104/215728155-9b9cfe26-96e8-49c3-8a08-131d96f4f2eb.png
   :alt: Django Berry PRO - Premium Starter built on top of Berry PRO Design


Download Sources
-----------------

To get the product navigate to the `payment page <https://appseed.gumroad.com/l/django-adminlte>`__ and complete the purchase. 
Unpack the ZIP archive and folow these steps:

.. code-block:: shell

    unzip django-berry-pro.zip
    cd django-berry-pro

Once the source code is unzipped, the next step is to start it and use provided features. 

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


Building the project
--------------------

It's best to use a Python virtual environment for installing the project dependencies. You can use the following
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

You can run Rocket Django locally or deploy it on Render. If you want to run the server locally, you'll need to run the following command:

.. code-block:: bash

    python manage.py createsuperuser
    python manage.py runserver

Open `localhost` on your browser and you can interact with the application. 

.. _localhost: http://127.0.0.1:8000/

.. image:: https://user-images.githubusercontent.com/51070104/215728155-9b9cfe26-96e8-49c3-8a08-131d96f4f2eb.png
   :alt: Homepage Django Berry PRO - open-source starter built on top of Berry PRO 

Contents
--------

.. toctree::
   :maxdepth: 1
   
   deployment
