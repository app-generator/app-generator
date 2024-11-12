:og:description: Database Migrations in Flask - A tutorial for beginners

Database Migrations
===================

.. title:: Database Migrations in Flask - A tutorial for beginners
.. meta::
    :description: A complete tutorial on Flask Migrations with focus on Flask-Migrate and SQLAlchemy 

This page is a guide that uses **Flask-Migrate** and **SQLAlchemy** for handling database migrations in a `Flask <./index.html>`__ application. 
It covers the configuration of different DBMS (SQLite, MySQL, PostgreSQL) and provides a complete setup for Flask-Migrate.

In order to link the theory with practice, here is an open-source sample that incorporates the source code and configuration mentioned in this page. 

- `Flask-Migrate & SQLAlchemy Sample <https://github.com/app-generator/docs-flask-db-migrations>`__ - GitHub Repository

.. include::  /_templates/components/banner-top.rst

Table of Contents
-----------------

1. `Introduction`
2. `Setup for Different DBMS`
   - `SQLite`
   - `MySQL`
   - `PostgreSQL`
3. `Flask Migrate Full Kickoff`
4. `Common Flask-Migrate Commands`
5. `Conclusion`

Introduction
------------

**Flask-Migrate** is an extension that handles database migrations for Flask applications using **Alembic**. 
It works alongside **SQLAlchemy**, which is an ORM (Object Relational Mapper) that maps Python objects to database tables.

Using Flask-Migrate, you can easily handle version control for your database schema, allowing for smooth database changes and rollbacks over time.

Setup for Different DBMS
------------------------

Flask-Migrate supports different database management systems. Below are the steps to configure SQLite, MySQL, and PostgreSQL.

SQLite
******

SQLite is a lightweight, file-based database suitable for small projects or testing.

1. **Install dependencies**:

   .. code-block:: bash

      pip install Flask-SQLAlchemy Flask-Migrate

2. **Update `config.py`**:

   .. code-block::

      # config.py
      class Config:
          SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  # SQLite URI
          SQLALCHEMY_TRACK_MODIFICATIONS = False

3. **Initialize Flask-Migrate** in `app.py`:

   .. code-block::

      from flask import Flask
      from flask_sqlalchemy import SQLAlchemy
      from flask_migrate import Migrate

      app = Flask(__name__)
      app.config.from_object('config.Config')

      db = SQLAlchemy(app)
      migrate = Migrate(app, db)


MySQL
*****

1. **Install the MySQL client**:

   .. code-block:: bash

      pip install mysqlclient

2. **Update `config.py`**:

   .. code-block::

      # config.py
      class Config:
          SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/db_name'  # MySQL URI
          SQLALCHEMY_TRACK_MODIFICATIONS = False

3. **Ensure MySQL is running** and the database exists:

   .. code-block:: bash

      mysql -u username -p
      CREATE DATABASE db_name;


PostgreSQL
**********

1. **Install the PostgreSQL client**:

   .. code-block:: bash

      pip install psycopg2

2. **Update `config.py`**:

   .. code-block::

      # config.py
      class Config:
          SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/db_name'  # PostgreSQL URI
          SQLALCHEMY_TRACK_MODIFICATIONS = False

3. **Ensure PostgreSQL is running** and create the database:

   .. code-block:: bash

      psql -U username
      CREATE DATABASE db_name;

Flask Migrate KickOff
---------------------

To set up **Flask-Migrate** and apply migrations to your database, follow these steps:

1. **Clone the Git repository**:

   .. code-block:: bash

      git clone https://github.com/app-generator/docs-flask-db-migrations
      cd docs-flask-db-migrations

2. **Create and activate a virtual environment**:

   .. code-block:: bash

      python3 -m venv venv
      source venv/bin/activate  # On Windows, use venv\Scripts\activate

3. **Install required packages**:

   .. code-block:: bash

      pip install -r requirements.txt

4. **Configure your database** in `config.py` (choose SQLite, MySQL, or PostgreSQL).

5. **Initialize Flask-Migrate**:

   .. code-block:: bash

      flask db init

6. **Create your models** in `models.py`:

   .. code-block::

      from app import db

      class User(db.Model):
          id = db.Column(db.Integer, primary_key=True)
          username = db.Column(db.String(150), unique=True, nullable=False)
          email = db.Column(db.String(150), unique=True, nullable=False)

7. **Create the initial migration**:

   .. code-block:: bash

      flask db migrate -m "Initial migration"

8. **Apply the migration**:

   .. code-block:: bash

      flask db upgrade

9. **Run the application**:

   .. code-block:: bash

      flask run

   Your Flask app will be running at `http://127.0.0.1:5000`.

Common Flask-Migrate Commands
-----------------------------

- **`flask db init`**: Initializes the migration directory (`migrations/`).
- **`flask db migrate -m "message"`**: Generates a new migration script.
- **`flask db upgrade`**: Applies the migration to the database.
- **`flask db downgrade`**: Rolls back the last migration.
- **`flask db history`**: Shows the migration history.
- **`flask db stamp head`**: Marks the current database as being at the latest migration.

Conclusion
----------

In this guide, we’ve covered how to set up **Flask-Migrate** with **SQLAlchemy** for managing database migrations in Flask applications.
We’ve also shown how to configure different databases (SQLite, MySQL, PostgreSQL) and run the Flask application with migrations.

By using Flask-Migrate, you can handle database schema changes in a more structured and controlled way. 
This approach simplifies managing database evolution over time, especially as your project grows.

Feel free to explore the code in the repository and follow the steps to integrate Flask-Migrate into your own Flask applications.

.. include::  /_templates/components/footer-links.rst