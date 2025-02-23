:og:description: Integrate DaisyUI with Django using Vite - The integration steps and Coding Sample

Integrate DaisyUI
=================

.. title:: Integrate DaisyUI with Django using Vite - The integration steps and Coding Sample   
.. meta::
    :description: Complete integration guide on DaisyUI, Django, and Vite - Free sample included
    :keywords: daisyui, tailwind, daisyui and django, integrate django with daisyui, grafana and django, daisyui integration, vite

Integrate `DaisyUI <../daisyui/index.html>`__ with `Django <./index.html>`__ using `Vite <../vite/index.html>`__ as builder tool - All integration steps and Coding Sample.

for newcomers, `DaisyUI <../daisyui/index.html>`__ is a lightweight, pure CSS component library for Tailwind that provides semantic class names for common UI components. 
It's focused on simplicity and customization through class-based approaches with zero JavaScript dependencies.

    👉 `DaisyUI and Django <https://github.com/app-generator/docs-django-daisy-ui>`__ - Integration Sample

Initial Django Setup
--------------------

First, let's create a new Django project and set up the virtual environment:

.. code-block:: bash

    # Create and activate virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    # Install Django
    pip install django

    # Create a new Django project
    django-admin startproject myproject
    cd myproject

    # Create a main app
    python manage.py startapp main

    # Run initial migrations
    python manage.py migrate    

Configure Django Settings
-------------------------

Add your new app to **settings.py**:

.. code-block:: python 

    # myproject/settings.py

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'main',  # Add your new app
    ]

    # Configure static files
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]    

Set up Tailwind CSS and DaisyUI
-------------------------------

.. code-block:: bash

    # Initialize npm
    npm init -y

    # Install required dependencies
    npm install -D tailwindcss postcss autoprefixer daisyui @tailwindcss/typography    

Configure Tailwind with DaisyUI 
-------------------------------

Create the Tailwind configuration file

.. code-block:: bash

    npx tailwindcss init

Update the configuration

.. code-block:: javascript

    // tailwind.config.js

    module.exports = {
        content: [
            './main/templates/**/*.html',
            './templates/**/*.html',
            './static/**/*.js',
        ],
        theme: {
            extend: {},
        },
        plugins: [
            require('daisyui'),
            require('@tailwindcss/typography'),
        ],
        daisyui: {
            themes: ["light", "dark", "cupcake"], // Add your preferred themes
        }
    }

Create CSS Structure
--------------------

Create your main CSS file:

.. code-block:: bash

    mkdir static/css
    touch static/css/main.css

Add the Tailwind directives to **main.css**: 

.. code-block:: css  

    /* static/css/main.css */

    @tailwind base;
    @tailwind components;
    @tailwind utilities;


Set Up Build Process
--------------------

Add build scripts to **package.json**:

.. code-block:: json

    {
        "scripts": {
            "build": "tailwindcss -i ./static/css/main.css -o ./static/css/output.css --watch"
        }
    }     

Create Base Template
--------------------

Create a base template that includes DaisyUI

.. code-block:: html 

    <!-- templates/base.html -->    
    <!DOCTYPE html>
    <html lang="en" data-theme="light">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{% block title %}Django DaisyUI{% endblock %}</title>
        {% load static %}
        <link href="{% static 'css/output.css' %}" rel="stylesheet">
    </head>
    <body>
        <div class="min-h-screen bg-base-100">
            <!-- Navbar -->
            <div class="navbar bg-base-200">
                <div class="flex-1">
                    <a class="btn btn-ghost normal-case text-xl">My Project</a>
                </div>
                <div class="flex-none">
                    <ul class="menu menu-horizontal px-1">
                        <li><a href="{% url 'home' %}">Home</a></li>
                        <li><a href="{% url 'about' %}">About</a></li>
                    </ul>
                </div>
            </div>

            <!-- Content -->
            <div class="container mx-auto px-4 py-8">
                {% block content %}
                {% endblock %}
            </div>
        </div>
    </body>
    </html>    

Create URL Patterns
-------------------

Set up your URLs:

.. code-block:: python 

    # myproject/urls.py

    from django.urls import path
    from main import views

    urlpatterns = [
        path('', views.home, name='home'),
        path('about/', views.about, name='about'),
    ]    

Create Views
------------

Add views in your main app:

.. code-block:: python 

    # main/views.py

    from django.shortcuts import render

    def home(request):
        return render(request, 'main/home.html')

    def about(request):
        return render(request, 'main/about.html')

Running the Project
-------------------

Start the Tailwind build process:

.. code-block:: bash 

    npm run build

In a separate terminal, run the Django development server:

.. code-block:: bash 

    python manage.py runserver

At this point, the Django starter runs integrated with DaisyUI and we can update the project with more features and UI components. 

.. include::  /_templates/components/footer-links.rst
