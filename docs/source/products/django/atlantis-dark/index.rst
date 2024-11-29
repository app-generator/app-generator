:og:description: Django Atlantis Dark - Open-Source Django Template 
:og:image: https://user-images.githubusercontent.com/51070104/172799909-4cbc8eed-fdde-4408-ab61-123f235212d0.png
:og:image:alt: Django Atlantis Dark - Open-Source Django Template 

`Atlantis Dark </product/atlantis-dark/django/>`__
=======================================================

.. title:: Django Atlantis Dark - Open-Source Django Template 
.. meta::
    :description: Open-Source Django Template crafted on top of Atlantis Dark Design
    :keywords: atlantis dashboard, django atlantis template, django atlantis starter, atlantis ui design, atlantis ui dashboard, bootstrap atlantis design

Free starter built on top of Bootstrap and Django with database, authentication, and Docker support. The Atlantis design is built on top of Bootstrap 4 Framework.

- 👉 `Django Atlantis Dark </product/atlantis-dark/django/>`__ - Product Page (contains download link)
- 👉 `Django Atlantis Dark <https://django-atlantis-dark.appseed-srv1.com/>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
--------

- Simple, Easy-to-Extend codebase
- Atlantis Design - Full Integration 
- Bootstrap 4 Styling 
- Session-based Authentication
- DB Persistence: SQLite (default), can be used with MySql, PgSql
- Docker 
- CI/CD integration for Render 

.. image:: https://user-images.githubusercontent.com/51070104/172799909-4cbc8eed-fdde-4408-ab61-123f235212d0.png
   :alt: Django Atlantis Dark - Open-source Starter styled with Atlantis Dark design 


.. include::  /_templates/components/django-prerequisites.rst


Download Source Code 
--------------------

The product can be downloaded from the `official product page </product/atlantis-dark/django/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/django-atlantis-dark.git
    cd django-atlantis-dark

Once the source code is unzipped, the next step is to start it and use provided features.     


.. include::  /_templates/components/start-in-docker.rst


Codebase  
--------

The project is coded using a simple and intuitive structure presented below:

.. code-block:: bash
    :caption: Project Files

    < Project ROOT > 
        |
        |
        |-- core/                            
        |    |-- settings.py                  # Project Configuration  
        |    |-- urls.py                      # Project Routing
        |
        |-- home/
        |    |-- views.py                     # APP Views 
        |    |-- urls.py                      # APP Routing
        |    |-- models.py                    # APP Models 
        |    |-- tests.py                     # Tests  
        |    |-- templates/                   # Theme Customisation 
        |         |-- includes                # UI Components  
        |     
        |-- requirements.txt                  # Project Dependencies
        |
        |-- env.sample                        # ENV Configuration (default values)
        |-- manage.py                         # Start the app - Django default start script


.. include::  /_templates/components/django-manual-build.rst

.. image:: https://user-images.githubusercontent.com/51070104/172799909-4cbc8eed-fdde-4408-ab61-123f235212d0.png
   :alt: Django Atlantis Dark - Open-source Starter styled with Atlantis Dark design 

.. include::  /_templates/components/django-create-users.rst
    
.. include::  /_templates/components/footer-links.rst
