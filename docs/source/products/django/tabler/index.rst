:og:description: Django Tabler - Open-source Starter styled with Tabler design
:og:image: https://app-generator.dev/static/product/tabler/django/top.png
:og:image:alt: Django Tabler - Open-source Starter styled with Tabler design

`Django Tabler </product/tabler/django/>`__
============================================

.. title:: Django Tabler - Open-source Starter styled with Tabler design     
.. meta::
    :description: Open-source Django Template styled with Tabler design  
    :keywords: django, django template, django starter, tabler, tabler django 

**Django Tabler** is an open-source starter built on top of the Tabler Design, a popular admin dashboard template.

- 👉 `Django Tabler <https://django-tabler.onrender.com/>`__ - LIVE Demo
- 👉 `Django Tabler <https://github.com/app-generator/django-tabler>`__ - Source Code

.. include::  /_templates/components/signin-invite.rst


Features
------------
* **Simple, Easy-to-Extend** codebase
* **AdminLTE** Design 
* **Docker** Support
* **Deployment-Ready** for Render 

.. image:: https://github.com/user-attachments/assets/f1fa943d-7e6c-4346-9734-281a8cd2e093
   :alt: Django Tabler - Open-source Starter styled with Tabler design 


Download Sources
-----------------

The product can be downloaded directly from GitHub (public `repository <https://github.com/app-generator/django-tabler>`__)

.. code-block:: shell

    git clone https://github.com/app-generator/django-tabler.git
    cd django-tabler

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
        |         |-- pages                   
        |     
        |-- requirements.txt                  # Project Dependencies
        |
        |-- env.sample                        # ENV Configuration (default values)
        |-- manage.py                         # Start the app - Django default start script


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

.. image:: https://github.com/user-attachments/assets/826e18b5-998d-41ec-b57b-35654c210a9b
   :alt: Homepage Django Tabler - open-source starter built on top of Tabler Design 

Contents
--------

.. toctree::
   :maxdepth: 1

   customize-ui
   deployment
