API Generator
=============

@TODO

.. include::  /_templates/components/banner-top.rst


1. What the Library is Doing
----------------------------
The **Django API Generator** is a tool designed to automate the creation of RESTful APIs for Django models. It leverages Django Rest Framework (DRF) to provide secure, efficient, and easily accessible endpoints for CRUD (Create, Read, Update, Delete) operations. The generated APIs are secured using JWT authentication for mutating requests (POST, PUT, DELETE).

2. How to Activate the API for a Model
--------------------------------------

Step 1: Install the Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Install the Django API Generator package using pip:

.. code-block:: bash

    pip install django-api-generator

Alternatively, install it directly from the GitHub repository:

.. code-block:: bash

    pip install git+https://github.com/app-generator/django-api-generator.git

Step 2: Add Required Apps to Django Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Add the following to your ``INSTALLED_APPS`` in ``settings.py``:

.. code-block:: python

    INSTALLED_APPS = [
        'django_api_gen',            # Django API Generator
        'rest_framework',            # Django Rest Framework
        'rest_framework.authtoken',  # DRF Auth Token
        # other installed apps...
    ]

Step 3: Define Your Model
~~~~~~~~~~~~~~~~~~~~~~~~~~
Ensure your Django model is defined. For example:

.. code-block:: python

    from django.db import models

    class Book(models.Model):
        title = models.CharField(max_length=255)
        author = models.CharField(max_length=255)
        published_date = models.DateField()

Step 4: Configure API Generator Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Add the following configuration to ``settings.py`` to specify which models should have an API generated:

.. code-block:: python

    API_GENERATOR = {
        # pattern: 
        # API_SLUG -> Import_PATH 
        'books': "app1.models.Book",
    }

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
        ],
    }

Step 5: Generate the API
~~~~~~~~~~~~~~~~~~~~~~~~~
Run the following command to automatically generate the API for your models:

.. code-block:: bash

    python manage.py generate-api

This command creates serializers, views, and URL patterns required for API interaction.

3. How to Access the Information (GET Requests)
------------------------------------------------

Once the API is generated, you can access it through the following endpoints:

- **List all records:**

  .. code-block:: none

      GET /api/books/

  .. image:: https://private-user-images.githubusercontent.com/101915710/408878910-2e09f0d8-718c-49c0-85c5-a739e6315879.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzg1MTE1NTMsIm5iZiI6MTczODUxMTI1MywicGF0aCI6Ii8xMDE5MTU3MTAvNDA4ODc4OTEwLTJlMDlmMGQ4LTcxOGMtNDljMC04NWM1LWE3MzllNjMxNTg3OS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjAyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIwMlQxNTQ3MzNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00NTJlNTg5ZDdmMGE2ZGU3ZmEzOTI4ZTMyYzRjY2RlY2JiMDk3OGFjZmJlZjk5YTY0NzY0MTU4OWNkNDRlZGJjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.FIeIFj3rd_D2AcisEpD_Wo6TAZl78OvRqE4EbW_D-kA
    :alt: List of all books

  Retrieves a list of all ``Book`` entries.

- **Retrieve a specific record:**

  .. code-block:: none

      GET /api/books/{id}/
  
  .. image:: https://private-user-images.githubusercontent.com/101915710/408878919-d87d25b8-7aac-4130-b14a-a08b0a1f02ca.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzg1MTE1NTMsIm5iZiI6MTczODUxMTI1MywicGF0aCI6Ii8xMDE5MTU3MTAvNDA4ODc4OTE5LWQ4N2QyNWI4LTdhYWMtNDEzMC1iMTRhLWEwOGIwYTFmMDJjYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjAyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIwMlQxNTQ3MzNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yNzE4MmY1MTlmYjNkZDNiNjZiYzhkY2UzMzE4YTFlMzlhZTc5M2VhMTk4ZmNkYTQyYTcyNjYzYTA0OGNhMGRmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.cKhBSxGPqwvZ_8Ov9xXUgcMEJGpMmt3AMKuI0D8rbmQ
    :alt: Details of a book

  Replace ``{id}`` with the primary key of the book you want to retrieve.

4. How to Update/Create Records
--------------------------------

Creating a New Record (POST Request)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none

    POST /api/books/

.. image:: https://private-user-images.githubusercontent.com/101915710/408878933-c5e85b22-efdc-4d0c-87a5-98eb09f52973.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzg1MTE1NTMsIm5iZiI6MTczODUxMTI1MywicGF0aCI6Ii8xMDE5MTU3MTAvNDA4ODc4OTMzLWM1ZTg1YjIyLWVmZGMtNGQwYy04N2E1LTk4ZWIwOWY1Mjk3My5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjAyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIwMlQxNTQ3MzNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jNDliZTc4NzY3MGE0NDE4YWU2ODYwNTdkNjVmNmI2NWMwN2FhYTQ0NTJkNTgzMTYwNDViNTA0NTY3NWZmMzY0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.6oJkHnQmUCXDWYA_nbfDzWP0YQzwF7rwvB3uzZok95s
    :alt: Create a book

Request Body:

.. code-block:: json

    {
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "published_date": "1997-06-26"
    }

Headers:

.. code-block:: none

    Authorization: Bearer <your_jwt_token>
    Content-Type: application/json

Updating an Existing Record (PUT Request)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none

    PUT /api/books/{id}/

.. image:: https://private-user-images.githubusercontent.com/101915710/408878939-8adff0c1-1495-4bc6-902b-a547f6f497b3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzg1MTE1NTMsIm5iZiI6MTczODUxMTI1MywicGF0aCI6Ii8xMDE5MTU3MTAvNDA4ODc4OTM5LThhZGZmMGMxLTE0OTUtNGJjNi05MDJiLWE1NDdmNmY0OTdiMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjAyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIwMlQxNTQ3MzNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iZmU0YjMwYTg0MGE4YTUzM2MyY2U4NTMyZDE1ZWIyOTkwYzhjMmI5NDI2OWFlMWJiOWIzMDcxOTQ1NTFkMjBjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.EUszNFks6IfkIctVcIaruRTUfbvPsgSSJKV2oJstUEA
    :alt: Update a book

Request Body:

.. code-block:: json

    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "published_date": "1997-06-26"
    }

Headers:

.. code-block:: none

    Authorization: Token <your_jwt_token>
    Content-Type: application/json

Replace ``{id}`` with the primary key of the record you want to update.


.. include::  /_templates/components/footer-links.rst
