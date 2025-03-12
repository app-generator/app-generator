:og:description: Getting Started with HTMX - Learn how to use HTMX in real-life projects | App-Generator.dev

Getting Started
================

.. title:: Getting Started with HTMX - Learn how to use HTMX in real-life projects | App-Generator.dev
.. meta::
    :description: Unified index for HTMX resources: tutorials, starters, best practices and dev tips

HTMX is a modern JavaScript library that allows you to access AJAX, CSS transitions, WebSockets, and Server-Sent Events directly in HTML, without writing JavaScript. 
When paired with Django, it creates a powerful combination that simplifies building dynamic web applications.

.. include::  /_templates/components/banner-top.rst

Set Up Your Development Environment
-----------------------------------

First, let's create a basic development environment:

.. code-block:: bash

  # Create a virtual environment
  python -m venv venv

  # Activate the virtual environment
  # For Windows:
  venv\Scripts\activate
  # For macOS/Linux:
  source venv/bin/activate

  # Install Django
  pip install django

  # Create a new Django project
  django-admin startproject htmx_demo

  # Navigate to your project
  cd htmx_demo

  # Create an app
  python manage.py startapp demo


2. Configure Your Django Project
--------------------------------

Add your app to the project settings:

.. code-block:: python

  # htmx_demo/settings.py
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'demo',  # Add your app here
  ]


3. Create a Basic Model
-----------------------

.. code-block:: python

  # demo/models.py
  from django.db import models

  class Task(models.Model):
      title = models.CharField(max_length=100)
      completed = models.BooleanField(default=False)
      created_at = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
          return self.title


Run migrations:

.. code-block:: bash

  python manage.py makemigrations
  python manage.py migrate


4. Set Up Templates
-------------------

Create a base template:

.. code-block:: bash

  mkdir -p demo/templates/demo

.. code-block:: html

  <!-- demo/templates/demo/base.html -->
  <!DOCTYPE html>
  <html>
  <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Django + HTMX Demo</title>
      
      <!-- Include HTMX -->
      <script src="https://unpkg.com/htmx.org@1.9.10"></script>
      
      <style>
          body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
          .task { padding: 10px; margin: 5px 0; border: 1px solid #ddd; border-radius: 4px; }
          .completed { text-decoration: line-through; background-color: #f8f8f8; }
          button { cursor: pointer; }
      </style>
  </head>
  <body>
      <h1>Django + HTMX Task Manager</h1>
      
      {% block content %}{% endblock %}
  </body>
  </html>


5. Create Views and Templates for Tasks
---------------------------------------

Create a view for the task list:

.. code-block:: python

  # demo/views.py
  from django.shortcuts import render
  from django.http import HttpResponse
  from .models import Task

  def task_list(request):
      tasks = Task.objects.all().order_by('-created_at')
      return render(request, 'demo/task_list.html', {'tasks': tasks})

  def add_task(request):
      title = request.POST.get('title')
      task = Task.objects.create(title=title)
      return render(request, 'demo/partials/task.html', {'task': task})

  def toggle_task(request, pk):
      task = Task.objects.get(pk=pk)
      task.completed = not task.completed
      task.save()
      return render(request, 'demo/partials/task.html', {'task': task})

  def delete_task(request, pk):
      Task.objects.get(pk=pk).delete()
      return HttpResponse("")


Create templates for the task list:

.. code-block:: html

  <!-- demo/templates/demo/task_list.html -->
  {% extends "demo/base.html" %}

  {% block content %}
      <!-- Add Task Form -->
      <form hx-post="{% url 'add_task' %}" hx-target="#task-list" hx-swap="afterbegin">
          {% csrf_token %}
          <input type="text" name="title" placeholder="Add a new task..." required>
          <button type="submit">Add</button>
      </form>

      <!-- Task List -->
      <div id="task-list">
          {% for task in tasks %}
              {% include "demo/partials/task.html" %}
          {% endfor %}
      </div>
  {% endblock %}


Create a partial template for individual tasks:

.. code-block:: html

  <!-- demo/templates/demo/partials/task.html -->
  <div class="task {% if task.completed %}completed{% endif %}" id="task-{{ task.id }}">
      <input type="checkbox" 
            {% if task.completed %}checked{% endif %} 
            hx-post="{% url 'toggle_task' task.id %}" 
            hx-target="#task-{{ task.id }}" 
            hx-swap="outerHTML">
      {{ task.title }}
      <button hx-delete="{% url 'delete_task' task.id %}" 
              hx-target="#task-{{ task.id }}" 
              hx-swap="outerHTML">Delete</button>
  </div>


6. Set Up URLs
--------------

.. code-block:: python

  # demo/urls.py
  from django.urls import path
  from . import views

  urlpatterns = [
      path('', views.task_list, name='task_list'),
      path('add/', views.add_task, name='add_task'),
      path('toggle/<int:pk>/', views.toggle_task, name='toggle_task'),
      path('delete/<int:pk>/', views.delete_task, name='delete_task'),
  ]


.. code-block:: python

  # htmx_demo/urls.py
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('demo.urls')),
  ]

7. Run Your Project
-------------------

.. code-block:: bash 

  python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to see your app in action!

Understanding What's Happening
------------------------------

1. **HTMX Attributes**:
   - `hx-post`: Makes a POST request to the specified URL
   - `hx-get`: Makes a GET request to the specified URL
   - `hx-delete`: Makes a DELETE request to the specified URL
   - `hx-target`: Specifies where to insert the response HTML
   - `hx-swap`: Defines how the response should be inserted (e.g., `innerHTML`, `outerHTML`, `afterbegin`)
   - `hx-trigger`: Defines when the request should be triggered (default is based on the element's natural event)

2. **HTMX Flow**:
   - User interacts with an element with HTMX attributes
   - HTMX sends an AJAX request to the server
   - Server returns HTML fragment
   - HTMX inserts the HTML fragment into the target element

For developers familiar with Django's templating system, HTMX feels like a natural extension that brings modern interactivity without the overhead of a complex JavaScript ecosystem.

`Rocket HTMX </product/rocket-htmx/django/>`__ 
-----------------------------------------------

**Django Rocket HTMX** is an open-source starter built with basic modules, authentication, data tables, charts, API and `HTMX </docs/technologies/htmx/index.html>`__ support.
The product UI is styled with **Flowbite**, an open source collection of UI components built with the utility classes from Tailwind CSS. 

- 👉 `Django Rocket HTMX </product/rocket-htmx/django/>`__ - Product Page (contains download link)
- 👉 `Django Rocket HTMX <https://rocket-django-htmx.onrender.com/>`__ - LIVE Demo

Features
********

- Simple, Easy-to-Extend codebase
- Styling: Flowbite/Tailwind
- Extended User Model
- ApexJS Charts
- DataTables via `HTMX </docs/technologies/htmx/index.html>`__
- API
- DB Persistence: SQLite (default), can be used with MySql, PgSql
- Docker 
- CI/CD integration for Render 

.. image:: https://github.com/user-attachments/assets/d7527d5e-046c-4679-8f72-525290a5edd5
   :alt: Django Rocket HTMX - Open-source Starter powered by HTMX and Tailwind 

.. include::  /_templates/components/footer-links.rst
