Customization
=============

.. title:: Django Pixel PRO - How to Customize it     
.. meta::
    :description: Learn how to cusomize Pixel PRO, a premium Django starter   
    :keywords: customize django, customize pixel pro, customize django pixel  

This page explains how to customize `Django Pixel PRO <./index.html>`__, a premium Django starter built on top of Pixel Bootstrap 5 Design. 


.. image:: https://user-images.githubusercontent.com/51070104/168760719-f0e45406-2b2a-43e0-badf-fa953edb62b8.png
   :alt: Django Pixel PRO - Premium Starter built on top of Pixel


Use MySql
---------

By default, the starter used SQLite for DB persistence, but this can be easily changed by following these steps: 

- **Step #1**: Make sure **MySql Server** is up & running  

.. code-block:: bash  

    service mysqld status # For Linux Systems 

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

    DB_ENGINE=pqsql
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

If the above steps are executed without errors, the MySql database should contain the project tables.

Use PostgreSQL 
--------------

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

- **Step #4** - Install the PostgreSQL Python Driver 

.. code-block:: bash 

    pip install psycopg2

- **Step #5** - Migrate the DataBase 

.. code-block:: bash 

    python manage.py makemigrations     # Migrate DataBase (generate tables) 
    python manage.py migrate            # Apply Changes on Database 

If the above steps are executed without errors, the MySql database should contain the tables 


UI Changes 
----------

The UI is provided by `django-theme-pixel-pro` private library that shipps all the assets, components and pages used by the Dajngo Pixel PRO starter.  

Django supports to overwrite all assets (css, images, pages) installed by the UI library in the virtual environment ans use a local version that can be fully customized. 

@TODO
