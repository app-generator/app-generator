:og:description: Django Argon Dashboard - Open-Source Django Template 
:og:image: https://user-images.githubusercontent.com/51070104/215804889-94eba681-8262-41a3-8e57-7d5b12dcc209.png
:og:image:alt: Django Argon Dashboard - Open-Source Django Template 

`Argon Dashboard </product/argon-dashboard/django/>`__
=======================================================

.. title:: Django Argon Dashboard - Open-Source Django Template 
.. meta::
    :description: Open-Source Django Template crafted on top of Argon Dashboard Design
    :keywords: argon dashboard, django argon template, django argon starter, argon ui design, argon ui dashboard, bootstrap argon design

Free starter built on top of Bootstrap and Django with database, authentication, and Docker support. The Argon Dashboard design is crafted by Creative-Tim using Bootstrap 5 Framework.

- 👉 `Django Argon Dashboard </product/argon-dashboard/django/>`__ - Product Page (contains download link)
- 👉 `Django Argon Dashboard <https://django-argon-dash2.onrender.com/`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
--------

- Simple, Easy-to-Extend codebase
- `Argon Dashboard </docs/templates/bootstrap/argon-dashboard.html>`__ Full Integration 
- Bootstrap 5 Styling 
- Session-based Authentication
- DB Persistence: SQLite/MySql/PostgreSQL
- Docker 
- CI/CD integration for Render 

.. image:: https://user-images.githubusercontent.com/51070104/215804889-94eba681-8262-41a3-8e57-7d5b12dcc209.png
   :alt: Django Argon Dashboard - Open-source Starter styled with Argon Dashboard design 


.. include::  /_templates/components/django-prerequisites.rst


Download Source Code 
--------------------

The product can be downloaded from the `official product page </product/argon-dashboard/django/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/django-argon-dashboard.git
    cd django-argon-dashboard

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

.. image:: https://user-images.githubusercontent.com/51070104/215804889-94eba681-8262-41a3-8e57-7d5b12dcc209.png
   :alt: Django Argon Dashboard - Open-source Starter styled with Argon Dashboard design 

.. include::  /_templates/components/django-create-users.rst
    
.. include::  /_templates/components/footer-links.rst
