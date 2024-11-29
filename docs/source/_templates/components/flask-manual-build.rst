Manual Build   
------------

It's best to use a Python Virtual Environment for installing the project dependencies. You can use the following
code to create the virtual environment

.. code-block:: bash

    virtualenv env

To activate the environment execute **env\\Scripts\\activate.bat** for Windows or **source env/bin/activate** on Linux-based operating systems. 

Having the `VENV` active, we can proceed and install the project dependencies:

.. code-block:: bash

    pip install -r requirements.txt


Environment   
-----------

The starter loads the environment variables from `.env` file. Here are the critical ones: 

- **DEBUG**: set by default to False (development mode)
- **SECRET_KEY**: a random value used by Django to secure sensitive information like passwords and cookie information 
- **Database** Credentials: `DB_ENGINE`, `DB_USERNAME`, `DB_PASS`, `DB_HOST`, `DB_PORT`, `DB_NAME`
    - if detected, the database is switched automatically from the default SQLite to the specified DBMS  


Setting up the Database
-----------------------

**By default**, the application **uses SQLite** for persistence. In order to use `MySql` / `PostgreSQL`, you'll need to install the Python driver(s):

.. code-block:: bash

    pip install mysqlclient # for MySql
    # OR 
    pip install psycopg2    # for PostgreSQL

To connect the application with the database, you'll need to fill in the credentials int the `.env` file and run the migrations.

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

Set up the environment

.. code-block:: bash

    export FLASK_APP=run.py

Use the following commands to set up the database:

.. code-block:: bash

    # Init migration folder
    flask db init # to be executed only once         

    flask db migrate # Generate migration SQL
    flask db upgrade # Apply changes

Running the project
-------------------

The following command starts the project using Flask development server:

.. code-block:: bash  

    flask run              # Starts on default PORT 5000
    flask run --port 8999  # Starts on PORT 8999 (custom port)

By default Flask starts on port **5000** but this can be easily changed by adding the PORT number as argument. 
At this point, the app runs at **http://127.0.0.1:5000/**
