:og:description: Django Star Admin - Open-source Starter styled with Star Admin design
:og:image: https://user-images.githubusercontent.com/51070104/168732392-51748c85-f2c2-45ad-978c-2b64e52292e2.png
:og:image:alt: Django Star Admin - Open-source Starter styled with Star Admin design

`Star Admin </product/star-admin/django/>`__
============================================

.. title:: Django Star Admin - Open-source Starter styled with Star Admin design     
.. meta::
    :description: Open-source Django Template styled with Star Admin design  
    :keywords: django, django template, django starter, star-admin, star-admin django 

**Django Star Admin** is an open-source starter built on top of the Star Admin Design, a popular admin dashboard template.

- 👉 `Django Star Admin </product/star-admin/django/>`__ - Product Page (contains download link)
- 👉 `Django Star Admin <https://django-star-admin.appseed-srv1.com>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
------------

- Simple, Easy-to-Extend codebase
- `Star Admin </docs/templates/bootstrap/staradmin.html>`__ Full Integration 
- Bootstrap Styling 
- Session-based Authentication
- DB Persistence: SQLite (default), can be used with MySql, PgSql
- Docker 
- CI/CD integration for Render 

.. image:: https://user-images.githubusercontent.com/51070104/168732392-51748c85-f2c2-45ad-978c-2b64e52292e2.png
   :alt: Django Star Admin - Open-source Starter styled with Star Admin design 


.. include::  /_templates/components/django-prerequisites.rst

Download Source Code 
--------------------

The product can be downloaded from the `official product page </product/star-admin/django/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/django-star-admin.git
    cd django-star-admin

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

.. image:: https://user-images.githubusercontent.com/51070104/168732392-51748c85-f2c2-45ad-978c-2b64e52292e2.png
   :alt: Homepage Django Star Admin - open-source starter built on top of Star Admin Design 

.. include::  /_templates/components/django-create-users.rst

.. include::  /_templates/components/generator-django.rst
        
.. include::  /_templates/components/footer-links.rst
