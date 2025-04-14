:og:description: Django Argon Dashboard PRO - Premium Starter built on top of Argon Dashboard
:og:image: https://github.com/user-attachments/assets/e2bca541-ed94-4369-8ab7-361a7f112e69
:og:image:alt: Premium Django starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with Argon Dashboard Design.

`Argon Dashboard PRO </product/argon-dashboard-pro/django/>`__ 
==============================================================

.. title:: Django Argon Dashboard PRO - Premium Starter built on top of Argon Dashboard     
.. meta::
    :description: Premium Django starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with Argon Dashboard Design.
    :keywords: django, django pro template, django pro starter, argon-dashboard pro, argon-dashboard django 

Premium Django starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with `Argon Dashboard </product/argon-dashboard/>`__ Design, 
released and crafted by `Creative-Tim </agency/creative-tim/>`__ using Bootstrap 5 Framework.
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. 

- 👉 `Django Argon Dashboard PRO </product/argon-dashboard-pro/django/>`__ - Product Page (contains download link)
- 👉 `Django Argon Dashboard PRO <https://django-argon-dash2-pro.onrender.com>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
---------

- **Simple, Easy-to-Extend** Codebase
- `Argon Dashboard PRO </product/argon-dashboard/>`__ Design Integration
- **OAuth** - Github
- **Extended User Profile**
- **API** via DRF 
- **Charts** via ApexJS 
- **DataTables**
- **Celery** (async tasks)
- **Deployment-Ready** for Render 

.. image:: https://github.com/user-attachments/assets/e2bca541-ed94-4369-8ab7-361a7f112e69
   :alt: Django Argon Dashboard PRO - Premium Starter built on top of Argon Dashboard


.. include::  /_templates/components/django-prerequisites.rst


Download Source Code 
--------------------

Access the `product page </product/argon-dashboard-pro/django/#pricing>`__ and complete the purchase. 
Unpack the ZIP archive and folow these steps:

.. code-block:: shell

    unzip django-argon-dashboard-pro.zip
    cd django-argon-dashboard-pro

Once the source code is unzipped, the next step is to start it and use provided features.     


.. include::  /_templates/components/start-in-docker.rst


Codebase  
--------

The project is coded using a simple and intuitive structure presented below:

.. code-block:: bash
    :caption: Project Files

    <  ROOT  >
        |
        |-- core/                 # Project Settings 
        |    |-- settings.py 
        |    |-- wsgi.py     
        |    |-- urls.py     
        |
        |-- home/                 # Presentation app 
        |    |-- views.py         # serve the HOMEpage  
        |    |-- urls.py     
        |    |-- models.py
        |
        |-- apps/                 # Utility Apps 
        |    |-- common/          # defines models & helpers
        |    |    |-- models.py   
        |    |    |-- util.py 
        |    |-- users            # Handles Authentication 
        |    |-- api              # DRF managed API
        |    |-- charts           # Showcase Different Charts
        |    |-- tables           # Implements DataTables
        |    |-- tasks            # Celery, async processing
        |
        |-- templates/            # UI templates 
        |-- static/               # Tailwind/Flowbite 
        |    |-- src/             # 
        |         |-- input.css   # CSS Styling
        |
        |-- Dockerfile            # Docker
        |-- docker-compose.yml    # Docker 
        |
        |-- render.yml            # CI/CD for Render
        |-- build.sh              # CI/CD for Render 
        |
        |-- manage.py             # Django Entry-Point
        |-- requirements.txt      # dependencies
        |-- .env                  # ENV File


.. include::  /_templates/components/django-manual-build.rst

.. image:: https://github.com/user-attachments/assets/e2bca541-ed94-4369-8ab7-361a7f112e69
   :alt: Django Argon Dashboard PRO - Premium Starter built on top of Argon Dashboard

.. include::  /_templates/components/django-create-users.rst
    
.. include::  /_templates/components/footer-links.rst
