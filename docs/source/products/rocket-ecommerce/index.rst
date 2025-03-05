`Rocket eCommerce </product/rocket-ecommerce/django/>`__
=========================================================

.. title:: Rocket eCommerce - Premium eCommerce Starter crafted on top of Tailwind/Flowbite and Django.   
.. meta::
    :description: eCommerce Starter powered by Django, Tailwind - Stripe Integration, a Discounts page, Analytics, and Premium Support. 
    :keywords: django, ecommerce, stripe integration, django and stripe

Premium eCommerce Starter crafted on top of Tailwind/Flowbite and Django. The product comes with Stripe Integration, a Discounts page, Analytics, and Premium Support.

- 👉 `Rocket eCommerce <https://rocket-ecommerce.onrender.com/>`__ - LIVE Demo
- 👉 `Rocket eCommerce </product/rocket-ecommerce/django/>`__ - Product page

.. include::  /_templates/components/banner-top.rst

Features
------------

- Stripe Integration
- Checkout, Discounts Page
- Tags, Categories
- Analytics
- Generated Sitemap
- FIGMA project

.. image:: https://github.com/user-attachments/assets/3d3e4abc-3a4e-4ef2-8934-d55bc25942db
   :alt: Rocket eCommerce - Premium eCommerce Starter crafted on top of Tailwind/Flowbite and Django

Download Sources
-----------------

To get the product navigate to the `payment page </product/rocket-ecommerce/django/#pricing>`__ and complete the purchase. 
Unpack the ZIP archive and folow these steps:

.. code-block:: shell
    :caption: Unzip Rocket eCommerce

    unzip rocket-ecommerce.zip
    cd rocket-ecommerce

Once the source code is unzipped, the next step is to start it and use provided features. 

.. code-block:: bash
    :caption: Project Files

    < Rocket eCommerce > 
       |
       |-- core/                            
       |    |-- settings.py         # Project Configuration  
       |    |-- urls.py             # Project Routing
       |
       |-- apps                     # project applications
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

To activate the environment execute `.\env\Scripts\activate.bat` for Windows or `source env/bin/activate` on Linux-based operating systems. 

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

You can run Dynamic Django locally or deploy it on Render. If you want to run the server locally, you'll need to run the following command:

.. code-block:: bash

    python manage.py createsuperuser
    python manage.py runserver

Access the project in your preferred browser and access the dynamic features.
