Getting Started
===============

PostgreSQL, often referred to as Postgres, is an advanced, open-source object-relational database management system (ORDBMS) 
that extends the SQL language combined with many features that safely store and scale complex data workloads.

.. include::  /_templates/components/signin-invite.rst
    
**Key Features** of PostgreSQL include:

- ACID compliance
- Multi-Version Concurrency Control (MVCC)
- Robust transactional support
- Extensibility (custom functions, operators, data types)
- Advanced indexing techniques
- Full-text search
- JSON and JSONB support
- Table inheritance and partitioning
- Procedural languages (PL/pgSQL, PL/Python, PL/Perl, etc.)
- Foreign data wrappers

To interact with PostgreSQL via terminal, you'll use the PostgreSQL Command-Line Client. Here are the steps to create a database, user, and set privileges:

- Accessing PostgreSQL. Enter the root password when prompted.

.. code-block:: bash  

    sudo -u postgres psql

- Creating a database

.. code-block:: sql 

    CREATE DATABASE mydb;

- Creating a user

.. code-block:: sql 

    CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';

- Granting privileges. This grants all privileges on **mydb** to **myuser**.

.. code-block:: sql 

    GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

- Connecting to the new database

.. code-block:: sql 

    /c mydb

- Granting schema privileges

.. code-block:: sql 

    GRANT ALL ON SCHEMA public TO myuser;

- Verifying user privileges

.. code-block:: sql 

    /du myuser

For more granular control, you can specify individual privileges:

.. code-block:: sql 

    GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO myuser;

- Revoke privileges:

.. code-block:: sql 

    REVOKE ALL PRIVILEGES ON DATABASE mydb FROM myuser;

As you advance, explore features like custom extensions, foreign data wrappers, and parallel query execution to leverage PostgreSQL's full potential in your applications.


******************************
Resources
******************************

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
