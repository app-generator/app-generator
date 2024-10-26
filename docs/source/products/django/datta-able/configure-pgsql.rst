Configure `PostgreSQL </docs/technologies/postgresql.html>`__  
==============================================================

This page explains how to change the persistence for Django Datta Able from SQLite (the default) to `PostgreSQL </docs/technologies/postgresql.html>`__. 

Prerequisites
-------------

In order to switch to PostgreSQL, a server needs to be installed and running. The 2nd step is to create a database, a user and a strong password for that DB account.

All these informations are going to be used in the `.env` file. 

Manual Set up
-------------

- **Step #1**: Make sure **PostgreSQL Server** is up & running  

.. code-block:: bash  

    pg_isready -h hostname -p port

- **Step #2**: Create the database, and DB user 

Using the terminal or a visual tool like **phpmyadmin** or `DBeaver <https://dbeaver.io/>`__ create the following:

.. code-block:: text  

    - a new database 
    - a new user 
    - a strong password 
    - give full privileges for the DB user over the new database 

- **Step #3**: Update the `.env` file located in the root of Django Datta Source code as suggested below 

.. code-block:: text 

    # True for development, False for production
    DEBUG=True

    SECRET_KEY=<STRONG_KEY_HERE>

    DB_ENGINE=mysql
    DB_HOST=localhost
    DB_NAME=YOUR_DB_HERE
    DB_USERNAME=YOUR_DB_USER_HERE
    DB_PASS=YOUR_DB_PASS_HERE
    DB_PORT=3306    

In case the service runs on another port and not on 3306 (default one), don't forget to adjust. 

- **Step #4** - Install the MySql Python Driver 

.. code-block:: bash 

    pip install mysqlclient


- **Step #5** - Migrate the DataBase 

.. code-block:: bash 

    python manage.py makemigrations     # Migrate DataBase (generate tables) 
    python manage.py migrate            # Apply Changes on Database 

If the above steps are executed without errors, the MySql database should contain the tables 

- **Step #6** - Start the project using MySql 

.. code-block:: bash 

    python manage.py runserver

At this point, the app runs at **http://127.0.0.1:8000/** using MySql as DB Server 

.. include::  /_templates/components/footer-links.rst
