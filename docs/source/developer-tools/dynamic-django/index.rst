`Dynamic Django <https://dynamic-django.onrender.com/>`__
==================================================================

.. title:: Dynamic Django - Dynamic Charts, APIs, DataTables and CLI Tools    
.. meta::
    :description: Dynamic Programming concepts applied in Python/Django
    :keywords: django, dynamic programming, dynamic charts, dynamic dataTables, dynamic api

**Dynamic Django** aims to simplify the data processing and consolidation via generated APIs, DataTables, Charts and CLI tools. 

- 👉 `Dynamic Django <https://dynamic-django.onrender.com/>`__ - **LIVE Demo**
- 👉 `Buy Product <https://appseed.gumroad.com/l/devtool-dynamic-django>`__ - **$499** Lifetime Access, Unlimited projects 

.. include::  /_templates/components/signin-invite.rst

Key features
------------
* **Powerful CLI**: A feature-rich commands able to manage the GIT interface, manipulate the configuration, update existing model and execute migration 
* **Dynamic DataTables**: using a single line of configuration, the data saved in any table is automatically managed   
* **Dynamic Charts**: extract relevant charts without coding all major type are supported  
* **Dynamic API**: any model can become a secure API Endpoint using DRF 

.. image:: https://github.com/user-attachments/assets/2f9f6cef-23cb-4328-b12f-dcc448feaa96
   :alt: Dynamic Django - Dynamic Programming concepts applied in Python/Django: APIs, DataTables, Charts 


Download Sources
-----------------

To get the product navigate to the `payment page <https://appseed.gumroad.com/l/devtool-dynamic-django>`__ and complete the purchase. 
Unpack the ZIP archive and folow these steps:

.. code-block:: shell

   unzip dynamic-django.zip
   cd dynamic-django 

Once the source code is unzipped, the next step is to start it and use provided features. 

.. code-block:: bash
    :caption: Project Files

    < Dynamic Django > 
       |
       |-- core/                            
       |    |-- settings.py         # Project Configuration  
       |    |-- urls.py             # Project Routing
       |
       |-- cli/                     # CLI helpers   
       |-- django_dyn_api/          # Dynamic API module            
       |-- django_dyn_charts/       # Dynamic Charts
       |-- django_dyn_dt/           # Dynamic DataTable 
       |
       |-- requirements.txt         # Project Dependencies
       |
       |-- build.sh                 # Render Builder Script
       |-- render.yaml              # Render Deeployer  
       |
       |-- .env                     # ENV Configuration (default values)
       |-- manage.py                # Start the app - Django default start script


Building the project
--------------------

It's best to use a Python virtual environment for installing the project dependencies. You can use the following
code to create the virtual environment

.. code-block:: bash

    virtualenv env

To activate the environment execute `.\env\Scripts\activate.bat` for Windows or `source env/bin/activate` on Linux-basedoperating systems. 

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

You can run Rocket Django locally or deploy it on Render. If you want to run
the server locally, you'll need to run the following command:

.. code-block:: bash

    python manage.py createsuperuser
    python manage.py runserver

That's it! Open `localhost` on your browswer and you can interact with the
application. If you want to run the application in a Docker container, we've got you covered. Run the following commands:

.. _localhost: http://127.0.0.1:8000/

.. image:: https://github.com/user-attachments/assets/57732fc4-5f16-4c93-885e-2890410df94a
   :alt: Homepage Dynamic Django - a tool that provides dynamic services for Django 

Contents
--------

.. toctree::
   :maxdepth: 1

   configuration
   api
   datatables
   charts 
   cli 
   deployment
