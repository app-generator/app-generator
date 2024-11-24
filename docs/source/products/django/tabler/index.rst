:og:description: Django Tabler - Open-source Starter styled with Tabler design
:og:image: https://app-generator.dev/static/product/tabler/django/top.png
:og:image:alt: Django Tabler - Open-source Starter styled with Tabler design

`Tabler </product/tabler/django/>`__
=====================================

.. title:: Django Tabler - Open-source Starter styled with Tabler design     
.. meta::
    :description: Open-source Django Template styled with Tabler design  
    :keywords: django, django template, django starter, tabler, tabler django 

**Django Tabler** is an open-source starter built on top of the Tabler Design, a popular admin dashboard template.

- 👉 `Django Volt Dashboard </product/tabler/django/>`__ - Product Page (contains download link)
- 👉 `Django Volt Dashboard <https://django-tabler.onrender.com/>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
------------

- Simple, Easy-to-Extend codebase
- `Tabler </docs/templates/bootstrap/tabler.html>`__ Full Integration 
- Bootstrap 4 Styling 
- Session-based Authentication
- DB Persistence: SQLite
- Docker 
- CI/CD integration for Render 

.. image:: https://github.com/user-attachments/assets/f1fa943d-7e6c-4346-9734-281a8cd2e093
   :alt: Django Tabler - Open-source Starter styled with Tabler design 


Download Source Code 
--------------------

The product can be downloaded from the `official product page </product/tabler/django/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/django-tabler.git
    cd django-tabler

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
        |         |-- pages                   
        |     
        |-- requirements.txt                  # Project Dependencies
        |
        |-- env.sample                        # ENV Configuration (default values)
        |-- manage.py                         # Start the app - Django default start script


.. include::  /_templates/components/django-manual-build.rst

.. image:: https://github.com/user-attachments/assets/826e18b5-998d-41ec-b57b-35654c210a9b
   :alt: Homepage Django Tabler - open-source starter built on top of Tabler Design 

.. include::  /_templates/components/django-create-users.rst

    
Contents
--------

.. toctree::
   :maxdepth: 1

   customize-ui
   deployment
