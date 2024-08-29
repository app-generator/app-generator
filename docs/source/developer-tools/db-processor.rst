DB Processor
=============

This page explains @ToDo

.. include::  /_templates/components/signin-invite.rst

@ToDo

Quick Start 
------------

.. code-block:: bash

    python.exe manage.py shell
    # Here we are inside the SHELL
    >>> from apps.helpers.db_processor import *
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

@Todo 

******************************
Resources
******************************

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
