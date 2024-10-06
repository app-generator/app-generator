Django AdminLTE PRO
=========================================================

.. title:: Django AdminLTE PRO - Premium Starter built on top of AdminLTE     
.. meta::
    :description: Premium Django Template styled with AdminLTE design  
    :keywords: django, django pro template, django pro starter, adminlte pro, adminlte django 

**Django AdminLTE** is an open-source starter built on top of the AdminLTE Design

- 👉 `Django AdminLTE PRO <https://django-adminlte-pro.onrender.com/>`__ - LIVE Demo
- 👉 `Django AdminLTE PRO <https://appseed.gumroad.com/l/django-adminlte>`__ - Purchase Link (Secured by GUMROAD) 

.. include::  /_templates/components/signin-invite.rst

Features
------------
* **Simple, Easy-to-Extend** Codebase
* **AdminLTE** Design 
* **OAuth** - Github
* **Extended User Profile**
* **API** via DRF 
* **Charts** via ApexJS 
* **React Integration** (new) 
* **Dynamic DataTables**
* **CSV to Model** Generator
* **CSV** Loader 
* **Celery** (async tasks)
* **Deployment-Ready** for Render 

.. image:: https://github.com/app-generator/django-adminlte/assets/51070104/8f0c396d-2f33-46b9-9689-2982c987399d
   :alt: Django AdminLTE PRO - Premium Starter built on top of AdminLTE


Download Sources
-----------------

To get the product navigate to the `payment page <https://appseed.gumroad.com/l/django-adminlte>`__ and complete the purchase. 
Unpack the ZIP archive and folow these steps:

.. code-block:: shell

    unzip django-adminlte-pro.zip
    cd django-adminlte-pro

Once the source code is unzipped, the next step is to start it and use provided features. 

.. code-block:: bash
    :caption: Project Files

    <  ROOT  >
        |
        |-- core/                 # Project Settings 
        |    |-- settings.py 
        |    |-- wsgi.py     
        |    |-- urls.py     
        |
        |-- home/                 # Presentation app 
        |    |-- views.py         # serve the HOMEpage  
        |    |-- urls.py     
        |    |-- models.py
        |
        |-- apps/                 # Utility Apps 
        |    |-- common/          # defines models & helpers
        |    |    |-- models.py   
        |    |    |-- util.py 
        |    |-- users            # Handles Authentication 
        |    |-- api              # DRF managed API
        |    |-- charts           # Showcase Different Charts
        |    |-- tables           # Implements DataTables
        |    |-- tasks            # Celery, async processing
        |
        |-- templates/            # UI templates 
        |-- static/               # Tailwind/Flowbite 
        |    |-- src/             # 
        |         |-- input.css   # CSS Styling
        |
        |-- Dockerfile            # Docker
        |-- docker-compose.yml    # Docker 
        |
        |-- render.yml            # CI/CD for Render
        |-- build.sh              # CI/CD for Render 
        |
        |-- manage.py             # Django Entry-Point
        |-- requirements.txt      # dependencies
        |-- .env                  # ENV File


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

.. image:: https://github.com/user-attachments/assets/4d5f6b17-3b80-469b-ade7-2b8e318f829d
   :alt: Homepage Django AdminLTE - open-source starter built on top of AdminLTE 

Contents
--------

.. toctree::
   :maxdepth: 1

   datatables
   deployment
