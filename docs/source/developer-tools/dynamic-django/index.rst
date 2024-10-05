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

Building the project
--------------------

It's best to use a Python virtual environment for installing the project dependencies. You can use the following
code to create the virtual environment

.. code-block:: bash

    virtualenv env

To activate the environment execute `.\env\Scripts\activate.bat` for Windows or `source env/bin/activate` on Linux-basedoperating systems. 

Having the `VENV` active, we can proceed and install the project dependencies:

.. code-block::

    pip install -r requirements.txt


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

    python manage.py runserver

That's it! Open `localhost` on your browswer and you can interact with the
application. If you want to run the application in a Docker container, we've got you covered. Run the following commands:

.. _localhost: http://127.0.0.1:8000/

Moreover, if you want to deploy the application on Render, you'll have to
modify the ``render.yaml`` file.

.. code-block:: yaml
    :caption: render.yaml

    services:
    - type: web
        name: appseed-v2
        plan: starter
        env: python
        region: frankfurt  # region should be same as your database region.
        buildCommand: "./build.sh"
        startCommand: "gunicorn core.wsgi:application"
        envVars:
        - key: DEBUG
            value: True
        - key: SECRET_KEY
            generateValue: true
        - key: WEB_CONCURRENCY
            value: 4

* You'll need to create a Blueprint instance on Render by going to this `link`_.
* Connect the repository that you want to deploy.
* Fill in the Service Group Name and click on the Update Existing Resources button.
* Click on Environment and add key called ``PYTHON_VERSION`` and set it equal to ``3.12.0``.
* After you make this change, the deployment will start automatically.

.. _link: https://dashboard.render.com/blueprints

In the end you should have a LIVE deployment identical to the official `Dynamic Django DEMO <https://dynamic-django.onrender.com/dynamic-dt/sales/>`__. 

.. image:: https://github.com/user-attachments/assets/7abec2c4-220f-4ac5-9de6-e96f8fc17c3e
   :alt: Dynamic Django - Dynamic DataTables view: minimal configuration, fully-fleged server-side paginated view 

Contents
--------

.. toctree::
   :maxdepth: 1

   configuration
   charts 
   datatables
   api
   cli 
   deployment
