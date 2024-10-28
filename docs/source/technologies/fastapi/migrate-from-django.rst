Migrate Django API
==================

This tutorial will use a project-driven approach to migrate a simple API from Django to FastAPI. We’ll take a Django-based API and incrementally transition it to FastAPI, covering the application structure, endpoints, and a seamless data migration process using SQLAlchemy. This guide is intended for developers who want to convert their API infrastructure while maintaining database consistency.

.. include::  /_templates/components/banner-top.rst

Project Setup and Initial Structure in Django
---------------------------------------------

Start by creating a Django project for a basic API that handles users and tasks. This application will include endpoints to create, retrieve, update, and delete records.

Step 1: Setting Up the Django Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create a new Django project and app:

   .. code-block:: bash

       django-admin startproject project_migration
       cd project_migration
       python manage.py startapp tasks

   Here, ``django-admin`` initiates a new project named ``project_migration``, and ``startapp`` creates a ``tasks`` app within the project to handle user and task APIs.

2. In ``settings.py``, configure the database and add the ``tasks`` app to ``INSTALLED_APPS``.

3. Define a simple data model in ``tasks/models.py`` for Users and Tasks:

   .. code-block:: python

       from django.db import models

       class User(models.Model):
           username = models.CharField(max_length=100, unique=True)
           email = models.EmailField(unique=True)

       class Task(models.Model):
           user = models.ForeignKey(User, on_delete=models.CASCADE)
           title = models.CharField(max_length=200)
           description = models.TextField(blank=True)
           is_completed = models.BooleanField(default=False)

   This code defines a ``User`` model with a unique username and email, and a ``Task`` model linked to a ``User``, allowing each user to have multiple tasks. The ``Task`` model includes fields for task details and completion status.

4. Create and apply migrations:

   .. code-block:: bash

       python manage.py makemigrations
       python manage.py migrate

   ``makemigrations`` generates migration files for model changes, and ``migrate`` applies them to the database, creating tables for the ``User`` and ``Task`` models.

5. Implement basic views and URL routes in ``tasks/views.py`` and ``tasks/urls.py``:

   .. code-block:: python

       from django.shortcuts import get_object_or_404
       from .models import User, Task
       from django.http import JsonResponse
       from django.views.decorators.csrf import csrf_exempt
       import json

       @csrf_exempt
       def create_user(request):
           if request.method == 'POST':
               data = json.loads(request.body)
               user = User.objects.create(username=data['username'], email=data['email'])
               return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email})

       @csrf_exempt
       def list_tasks(request, user_id):
           tasks = Task.objects.filter(user_id=user_id)
           return JsonResponse([{'id': task.id, 'title': task.title, 'is_completed': task.is_completed} for task in tasks], safe=False)

   The ``create_user`` view handles POST requests to add a new user, and ``list_tasks`` fetches tasks related to a specified ``user_id``. Each function returns a JSON response, making the endpoints accessible for external requests.

6. Configure the main URL routes in ``project_migration/urls.py``:

   .. code-block:: python

       from django.urls import path, include

       urlpatterns = [
           path('api/', include('tasks.urls')),
       ]

   Here, the main URL configuration includes routes from the ``tasks`` app under the ``/api/`` endpoint, centralizing the project’s API structure.

At this point, we have a functioning API in Django. Now, let’s begin the migration process by setting up FastAPI.


Step 2: Setting Up the FastAPI Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new directory structure for FastAPI:

.. code-block:: bash

    mkdir fastapi_migration
    cd fastapi_migration

Install FastAPI and an ASGI server, such as ``uvicorn``, for local testing:

.. code-block:: bash

    pip install fastapi uvicorn sqlalchemy pydantic

This sets up the ``fastapi_migration`` folder for our new project, installing FastAPI, ``uvicorn`` for running the app, and ``sqlalchemy`` and ``pydantic`` for data modeling and validation.


Step 3: Setting Up SQLAlchemy Models in FastAPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define SQLAlchemy models similar to Django’s ORM models.

1. **database.py**: Set up the connection to the database using SQLAlchemy.

   .. code-block:: python

       from sqlalchemy import create_engine
       from sqlalchemy.ext.declarative import declarative_base
       from sqlalchemy.orm import sessionmaker

       SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

       engine = create_engine(SQLALCHEMY_DATABASE_URL)
       SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
       Base = declarative_base()

   This code establishes a SQLite database connection using SQLAlchemy. ``SessionLocal`` creates sessions for database operations, while ``Base`` serves as a base class for model definitions.

2. **models.py**: Recreate the Django models in SQLAlchemy.

   .. code-block:: python

       from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
       from sqlalchemy.orm import relationship
       from .database import Base

       class User(Base):
           __tablename__ = "users"
           id = Column(Integer, primary_key=True, index=True)
           username = Column(String, unique=True, index=True)
           email = Column(String, unique=True, index=True)

       class Task(Base):
           __tablename__ = "tasks"
           id = Column(Integer, primary_key=True, index=True)
           title = Column(String, index=True)
           description = Column(String)
           is_completed = Column(Boolean, default=False)
           user_id = Column(Integer, ForeignKey("users.id"))

           user = relationship("User")

   The models here mirror the Django structure, with a ``User`` table and a ``Task`` table that includes a foreign key to ``User``, enforcing relational integrity between tasks and users.

3. **schemas.py**: Define Pydantic models to validate input data.

   .. code-block:: python

       from pydantic import BaseModel

       class UserBase(BaseModel):
           username: str
           email: str

       class TaskBase(BaseModel):
           title: str
           description: str
           is_completed: bool

   These Pydantic models handle validation and serialization of user and task data, ensuring correct data structures for input and output across the API.

4. **crud.py**: Implement the CRUD functions using SQLAlchemy’s session.

   .. code-block:: python

       from sqlalchemy.orm import Session
       from . import models, schemas

       def create_user(db: Session, user: schemas.UserBase):
           db_user = models.User(username=user.username, email=user.email)
           db.add(db_user)
           db.commit()
           db.refresh(db_user)
           return db_user

       def get_tasks(db: Session, user_id: int):
           return db.query(models.Task).filter(models.Task.user_id == user_id).all()

   ``create_user`` adds a new user to the database, while ``get_tasks`` retrieves tasks associated with a user ID, utilizing SQLAlchemy’s ORM for data interactions.


Step 4: Exporting Django Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the Django project, use the following script to export data:

.. code-block:: python

    import json
    from tasks.models import User, Task

    data = {
        "users": list(User.objects.values()),
        "tasks": list(Task.objects.values())
    }

    with open('data.json', 'w') as f:
        json.dump(data, f)

This script collects all ``User`` and ``Task`` records into dictionaries and writes them to a JSON file, ``data.json``, which will be imported into the FastAPI project.

Step 5: Importing Data into FastAPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the FastAPI project, create an import script:

.. code-block:: python

    import json
    from sqlalchemy.orm import Session
    from .database import SessionLocal, engine
    from . import models

    models.Base.metadata.create_all(bind=engine)

    def import_data():
        db = SessionLocal()
        with open('data.json') as f:
            data = json.load(f)
            for user_data in data['users']:
                user = models.User(id=user_data['id'], username=user_data['username'], email=user_data['email'])
                db.add(user)
            db.commit()

            for task_data in data['tasks']:
                task = models.Task(id=task_data['id'], title=task_data['title'], is_completed=task_data['is_completed'], user_id=task_data['user_id'])
                db.add(task)
            db.commit()

This function reads ``data.json`` and inserts each record into the FastAPI database. The ``Base.metadata.create_all`` call ensures tables exist before importing data, and each ``add`` operation pushes individual records to the database.

Summary
-------

The migration process shows how to transition from Django to FastAPI with data integrity maintained through SQLAlchemy. The provided code snippets create a functional API in FastAPI, complete with database migrations and CRUD operations, serving as a reusable guide for real-world applications where a shift to FastAPI enhances performance. 

.. include::  /_templates/components/footer-links.rst
