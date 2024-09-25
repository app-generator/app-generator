DB Processor
=============

This page explains @ToDo

.. include::  /_templates/components/signin-invite.rst

@ToDo

Quick Start 
------------

SQLITE Connection and data dump

.. code-block:: bash

    python.exe manage.py shell
    # Here we are inside the SHELL
    >>> from helpers.db_processor import *
    >>> db_sqlite = DbWrapper()
    >>> db_sqlite.driver = COMMON.DB_SQLITE 
    >>> db_sqlite.db_name = 'media/tool_inspect/api-django.sqlite3' 
    >>> db_sqlite.connect()
    >>> db_sqlite.load_models()
    >>> db_sqlite.dump_tables()    
    >>> db_sqlite.dump_tables_data() 
    # OUTPUT
    tmp/05_27_58_SQLITE.sql 
    tmp/05_28_04_SQLITE_api_user_user.sql
    tmp/05_28_04_SQLITE_auth_permission.sql

MySql Dump 

.. code-block:: bash

    >>> from helpers.db_processor import *
    >>> db_conn = DbWrapper()
    >>> db_conn.driver = COMMON.DB_MYSQL
    >>> db_conn.db_name = 'DB_NAME_HERE'
    >>> db_conn.db_user = 'DB_USER_HERE' 
    >>> db_conn.db_pass = 'DB_PASS_HERE' 
    >>> #db_conn.db_port = 3306 
    >>> #db_conn.db_host = 'localhost' 
    >>> db_conn.connect()            
    True # All good when TRUE
    >>> db_conn.dump_models() 
    >>> db_conn.dump_tables() 
    >>> db_conn.dump_tables_data() 

******************************
Resources
******************************

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
