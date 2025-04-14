:og:description: Django AdminLTE PRO - Premium Starter built on top of AdminLTE
:og:image: https://github.com/user-attachments/assets/892dd62b-2127-4a8c-ba44-932999fdddbc
:og:image:alt: Premium Django starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with AdminLTE Design.

`AdminLTE PRO </product/adminlte-pro/django/>`__ 
=================================================

.. title:: Django AdminLTE PRO - Premium Starter built on top of AdminLTE     
.. meta::
    :description: Premium Django starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with AdminLTE Design.
    :keywords: django, django pro template, django pro starter, adminlte pro, adminlte django 

Premium Django starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with `AdminLTE </product/adminlte/>`__ Design.
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. 

- 👉 `Django AdminLTE PRO </product/adminlte-pro/django/>`__ - Product Page (contains download link)
- 👉 `Django AdminLTE PRO <https://django-adminlte-pro.onrender.com/>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
---------

- **Simple, Easy-to-Extend** Codebase
- `AdminLTE </product/adminlte/>`__ Design Integration
- **OAuth** - Github
- **Extended User Profile**
- **API** via DRF 
- **Charts** via ApexJS 
- **React Integration** (new) 
- **Dynamic DataTables**
- **CSV to Model** Generator
- **CSV** Loader 
- **Celery** (async tasks)
- **Deployment-Ready** for Render 

.. image:: https://github.com/user-attachments/assets/892dd62b-2127-4a8c-ba44-932999fdddbc
   :alt: Django AdminLTE PRO - Premium Starter built on top of AdminLTE


.. include::  /_templates/components/django-prerequisites.rst


Download Source Code 
--------------------

Access the `product page </product/adminlte-pro/django/#pricing>`__ and complete the purchase. 
Unpack the ZIP archive and folow these steps:

.. code-block:: shell

    unzip django-adminlte-pro.zip
    cd django-adminlte-pro

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

.. image:: https://github.com/user-attachments/assets/892dd62b-2127-4a8c-ba44-932999fdddbc
   :alt: Homepage Django AdminLTE - open-source starter built on top of AdminLTE 


.. include::  /_templates/components/django-create-users.rst


Contents
--------

.. toctree::
   :maxdepth: 1
   
   source-code
   datatables
   deployment
