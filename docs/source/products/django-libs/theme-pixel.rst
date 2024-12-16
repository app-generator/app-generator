Pixel UI
========

.. title:: Django Pixel UI - UI Library for Django with Pixel Design (free version)      
.. meta::
    :description: Django Ui Theme built on top of Pixel Design 
    :keywords: pixel ui desgin, pixel design, django pixel design, django pixel ui theme, django pixel library, bootstrap pixel design  
 
Modern UI Library for **Django**, Auth Pages (registration included) crafted on top of **Pixel UI Design**, an open-source `Bootstrap` design.

- 👉 `Django Pixel UI </product/pixel-bootstrap/django/>`__ - Product that uses the library 
- 👉 `Django Pixel UI <pixel-https://django-pixel-lite.appseed-srv1.com>`__ - LIVE Demo

.. include::  /_templates/components/signin-invite.rst

Features 
--------

- Design: `Pixel UI </docs/templates/bootstrap/pixel-bootstrap.html>`__ Bootstrap
- **Sections Covered**: 
    - `All pages` managed by `Django.contrib.AUTH`
    - `Registration` page
    - `Misc pages`: colors, icons, typography, blank-page 

.. image:: https://user-images.githubusercontent.com/51070104/168753915-d61b2f97-57b2-4d14-a774-d217d120ff62.png
   :alt: Pixel UI Kit - Open-source UI Kit from Themesberg 

Why **Django Pixel UI Kit** 
*****************************

- Modern Bootstrap 5 Design
- Responsive Interface
- Minimal Template overriding
- Easy integration


Installation 
------------

.. code-block:: bash

    $ pip install django-django-theme-pixel
    // OR
    $ pip install git+https://github.com/app-generator/django-theme-pixel.git

Add **theme_pixel** application to the **INSTALLED_APPS Section** of your Django project **settings.py** file:

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",

        'theme_pixel',          # <-- NEW 
    ]

Add LOGIN_REDIRECT_URL and EMAIL_BACKEND of your Django project settings.py file:

.. code-block:: python
    :caption: core/settings.py  

    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Add **theme_pixel** routing in your Django Project **urls.py** file

.. code-block:: python

    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('theme_pixel.urls')),  #  <-- NEW
    ]

Start the project now styled with the AdminLTE Design 

.. code-block:: bash
    :caption: Steps to start the project 

    python manage.py collectstatic
    python manage.py runserver # default port 8000    

Access the project in your preferred browser and the UI should be styled with the new design.

.. image:: https://user-images.githubusercontent.com/51070104/168753915-d61b2f97-57b2-4d14-a774-d217d120ff62.png
   :alt: Pixel UI Kit - Open-source UI Kit from Themesberg 

.. include::  /_templates/components/generator-django.rst
        
.. include::  /_templates/components/footer-links.rst
