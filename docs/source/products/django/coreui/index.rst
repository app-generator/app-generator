:og:description: Django CoreUI - Open-source Starter styled with CoreUI design
:og:image: https://user-images.githubusercontent.com/51070104/171336361-b125ca1d-8936-4f4a-b662-9e45ee25f404.png
:og:image:alt: Django CoreUI - Open-source Starter styled with CoreUI design

`CoreUI </product/coreui/django/>`__
=====================================

.. title:: Django CoreUI - Open-source Starter styled with CoreUI design     
.. meta::
    :description: Open-source Django Template styled with CoreUI design  
    :keywords: django, django template, django starter, coreui, coreui django 

**Django CoreUI** is an open-source starter built on top of the CoreUI Design, a popular admin dashboard template.

- 👉 `Django Volt Dashboard </product/coreui/django/>`__ - Product Page (contains download link)
- 👉 `Django Volt Dashboard <https://django-coreui.onrender.com/>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
------------

- Simple, Easy-to-Extend codebase
- `CoreUI </docs/templates/bootstrap/coreui.html>`__ Full Integration 
- Bootstrap 4 Styling 
- Session-based Authentication
- DB Persistence: SQLite
- Docker 
- CI/CD integration for Render 

.. image:: https://user-images.githubusercontent.com/51070104/171336361-b125ca1d-8936-4f4a-b662-9e45ee25f404.png
   :alt: Django CoreUI - Open-source Starter styled with CoreUI design 


.. include::  /_templates/components/django-prerequisites.rst

Download Source Code 
--------------------

The product can be downloaded from the `official product page </product/coreui/django/>`__ or directly from GitHub (public repository)

.. code-block:: shell

    git clone https://github.com/app-generator/django-coreui.git
    cd django-coreui

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

.. image:: https://user-images.githubusercontent.com/51070104/171336361-b125ca1d-8936-4f4a-b662-9e45ee25f404.png
   :alt: Homepage Django CoreUI - open-source starter built on top of CoreUI Design 

.. include::  /_templates/components/django-create-users.rst
    
.. include::  /_templates/components/footer-links.rst
