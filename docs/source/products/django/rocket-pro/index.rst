:og:description: Django Rocket PRO - Premium Starter built on top of Flowbite/Tailwind
:og:image: https://github.com/user-attachments/assets/d60069f3-be43-460f-ba03-0da92276f87c
:og:image:alt: Premium Django starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with Flowbite/Tailwind Design.

`Rocket PRO </product/rocket-pro/django/>`__ 
============================================

.. title:: Django Rocket PRO - Premium Starter built on top of Rocket     
.. meta::
    :description: Premium Django starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with Rocket Design.
    :keywords: django, django pro template, django pro starter, rocket pro, rocket django 

Premium Django starter built with Database, DB Tools, API, OAuth, Celery, and React Integration with Flowbite/Tailwind Design.
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. 

- 👉 `Django Rocket PRO </product/rocket-pro/django/>`__ - Product Page (contains download link)
- 👉 `Django Rocket PRO <https://django-rocket-pro.onrender.com/>`__ - LIVE Demo
- 👉 `Get Support </ticket/create/>`__ via Email and Discord 

.. include::  /_templates/components/signin-invite.rst


Features
---------

- **Simple, Easy-to-Extend** Codebase
- **Rocket** Design
- Tailwind/Flowbite CSS
- **OAuth** - Github
- **Extended User Profile**
- **API** via DRF 
- **Charts** via ApexJS 
- **React Integration** (new) 
- **Celery** (async tasks)
- **Deployment-Ready** for Render 

.. image:: https://github.com/user-attachments/assets/d60069f3-be43-460f-ba03-0da92276f87c
   :alt: Django Rocket PRO - Premium Starter built on top of Flowbite/Tailwind


.. include::  /_templates/components/django-prerequisites.rst

Download Source Code 
--------------------

Access the `product page </product/rocket-pro/django/#pricing>`__ and complete the purchase. 
Unpack the ZIP archive and folow thhe installation steps:

.. code-block:: shell

    unzip django-rocket-pro.zip
    cd django-rocket-pro

Once the source code is unzipped, the next step is to start it and use provided features.     


.. include::  /_templates/components/start-in-docker.rst


Codebase  
--------

The project is coded using a simple and intuitive structure presented below:

.. code-block:: bash
    :caption: Project Files

    < PROJECT ROOT >
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


Install Tailwind/Flowbite
-------------------------

Tested with **Node** `v18.20.0` (use at least this version or above)

.. code-block:: bash

    $ npm install
    $ npm run dev
    $ npx tailwindcss -i ./static/assets/style.css -o ./static/dist/css/output.css --watch # DEVELOPMENT (LIVE reload)
    $ npx tailwindcss -i ./static/assets/style.css -o ./static/dist/css/output.css         # PRODUCTION    

.. include::  /_templates/components/django-manual-build.rst

.. image:: https://github.com/user-attachments/assets/d60069f3-be43-460f-ba03-0da92276f87c
   :alt: Django Rocket PRO - Premium Starter built on top of Flowbite/Tailwind


.. include::  /_templates/components/django-create-users.rst


.. include::  /_templates/components/django-start-celery.rst
