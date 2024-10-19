Getting Started
===============

MySQL is an open-source relational database management system (RDBMS) that uses Structured Query Language (SQL) for managing and manipulating data. 
It's widely used for web applications, data warehousing, and embedded applications due to its reliability, performance, and ease of use.

.. include::  /_templates/components/banner-top.rst
    
**Key Features** of MySQL include:

- ACID compliance (Atomicity, Consistency, Isolation, Durability)
- Transactional and non-transactional storage engines
- Replication support
- Partitioning
- Stored procedures and triggers
- Views and cursors
- Information schema
- Query caching

To interact with MySQL via terminal, you'll use the MySQL Command-Line Client. Here are the steps to create a database, user, and set privileges:

- Accessing MySQL. Enter the root password when prompted.

.. code-block:: bash  

    mysql -u root -p

- Creating a database

.. code-block:: sql 

    CREATE DATABASE mydatabase;

- Creating a user

.. code-block:: sql 

    CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';

- Granting privileges. This grants all privileges on **mydatabase** to **newuser**.

.. code-block:: sql 

    GRANT ALL PRIVILEGES ON mydatabase.* TO 'newuser'@'localhost';

- Applying changes

.. code-block:: sql 

    FLUSH PRIVILEGES;

- Verifying user privileges

.. code-block:: sql 

    SHOW GRANTS FOR 'newuser'@'localhost';

For more granular control, you can specify individual privileges:

.. code-block:: sql 

    GRANT SELECT, INSERT, UPDATE, DELETE ON mydatabase.* TO 'newuser'@'localhost';

- Revoke privileges:

.. code-block:: sql 

    REVOKE ALL PRIVILEGES ON mydatabase.* FROM 'newuser'@'localhost';

As you progress, explore advanced topics such as replication, partitioning, and stored procedures to leverage MySQL's full capabilities in your applications.

.. include::  /_templates/components/footer-links.rst
