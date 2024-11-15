AdminLTE 
========

.. title:: Django Theme AdminLTE - Standalone library for Ui and ADMIN Section     
.. meta::
    :description: Django Theme (UI and Admin Section) styled with AdminLTE   
    :keywords: django, django theme, django ui library, adminlte, adminlte django, adminlte design  

**Django Theme AdminLTE** is a standalone library for UI and Django ADMIN Section 

- 👉 `Django AdminLTE <https://github.com/app-generator/django-adminlte>`__ - Product that uses the library 
- 👉 `Django AdminLTE <https://pypi.org/project/django-admin-adminlte/>`__ - PyPi Page  

.. include::  /_templates/components/signin-invite.rst

Features 
--------

- Design: `AdminLTE </docs/templates/bootstrap/adminlte.html>`__ Bootstrap
- **Sections Covered**: 
    - `Admin Section`, reserved for `superusers`
    - `All pages` managed by `Django.contrib.AUTH`
    - `Registration` page
    - `Misc pages`: colors, icons, typography, blank-page 

.. image:: https://github.com/app-generator/django-adminlte/assets/51070104/8f0c396d-2f33-46b9-9689-2982c987399d
   :alt: Django AdminLTE - Open-source Starter styled with AdminLTE design 
   
Why **Django AdminLTE** 
***********************

- Modern Bootstrap Design
- Responsive Interface
- Minimal Template overriding
- Easy integration


Installation 
------------

.. code-block:: bash

    pip install django-admin-adminlte
    // OR 
    pip install git+https://github.com/app-generator/django-admin-adminlte.git

Add **admin_adminlte** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file (note it should be before django.contrib.admin):

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        ...
        'admin_adminlte.apps.AdminAdminlteConfig',
        'django.contrib.admin',
        ...
    ]

Add LOGIN_REDIRECT_URL and EMAIL_BACKEND of your Django project settings.py file:

.. code-block:: python
    :caption: core/settings.py  

    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Add **admin_adminlte** routing in your Django Project **urls.py** file

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_adminlte.urls')),
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://github.com/app-generator/django-adminlte/assets/51070104/8f0c396d-2f33-46b9-9689-2982c987399d
   :alt: Django AdminLTE - Open-source Starter styled with AdminLTE design 

.. include::  /_templates/components/footer-links.rst

