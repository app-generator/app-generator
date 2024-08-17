Getting Started
=====================

`Django <https://www.djangoproject.com/>`__ is an opinionated framework that provides a complete set of tools for web development, from URL routing to form handling and user authentication. 
It promotes best practices in web development through its structure and conventions, encouraging developers to write maintainable and scalable code. 
**Django**'s middleware system allows for global processing of requests and responses, enabling the implementation of complex features like session handling and caching with minimal effort.

.. include::  /_templates/components/signin-invite.rst
    
Here are the basic **steps to code a simple Django project**:

**Installation**

.. code-block:: bash

    pip install django

**Create a project**

.. code-block:: bash

    django-admin startproject myproject
    cd myproject

**Create an app**

.. code-block:: bash

    python manage.py startapp myapp

**Configure settings**: Edit `myproject/settings.py`

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'myapp',
    ]

**Define a model**

.. code-block:: python

    from django.db import models

    class Item(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()

        def __str__(self):
            return self.name

**Create and apply migrations**            

.. code-block:: bash

    python manage.py makemigrations
    python manage.py migrate

**Create a view**    

.. code-block:: python

    from django.shortcuts import render
    from .models import Item

    def item_list(request):
        items = Item.objects.all()
        return render(request, 'myapp/item_list.html', {'items': items})
        
**Create a template**

.. code-block:: html

    <h1>Items</h1>
        <ul>
        {% for item in items %}
            <li>{{ item.name }} - {{ item.description }}</li>
        {% endfor %}
    </ul>

**Configure URL patterns**

.. code-block:: python

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('myapp.urls')),
    ]

**Create** `myapp/urls.py`

.. code-block:: python

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.item_list, name='item_list'),
    ]

**Run the development server**

.. code-block:: bash

    python manage.py runserver

**Create a superuser**

.. code-block:: bash

    python manage.py createsuperuser

**Register models** in the admin: Edit `myapp/admin.py`

.. code-block:: python

    from django.contrib import admin
    from .models import Item

    admin.site.register(Item)

**Forms** Create `myapp/forms.py`

.. code-block:: python

    from django import forms
    from .models import Item

    class ItemForm(forms.ModelForm):
        class Meta:
            model = Item
            fields = ['name', 'description']

**Create, update, delete** views: Add to `myapp/views.py`

.. code-block:: python

    from django.shortcuts import render, redirect, get_object_or_404
    from .forms import ItemForm
    from .models import Item

    def item_create(request):
        if request.method == 'POST':
            form = ItemForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('item_list')
        else:
            form = ItemForm()
        return render(request, 'myapp/item_form.html', {'form': form})

    def item_update(request, pk):
        item = get_object_or_404(Item, pk=pk)
        if request.method == 'POST':
            form = ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('item_list')
        else:
            form = ItemForm(instance=item)
        return render(request, 'myapp/item_form.html', {'form': form})

    def item_delete(request, pk):
        item = get_object_or_404(Item, pk=pk)
        if request.method == 'POST':
            item.delete()
            return redirect('item_list')
        return render(request, 'myapp/item_confirm_delete.html', {'item': item})

**Add URL patterns for CRUD operations** Update `myapp/urls.py`

.. code-block:: python

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.item_list, name='item_list'),
        path('create/', views.item_create, name='item_create'),
        path('update/<int:pk>/', views.item_update, name='item_update'),
        path('delete/<int:pk>/', views.item_delete, name='item_delete'),
    ]

**Static files**: Configure `STATIC_URL` in `settings.py`

.. code-block:: python

    STATIC_URL = '/static/'

Use static files in templates:

.. code-block:: html

    {% load static %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">

**User authentication**: Add to `myapp/views.py`

.. code-block:: python

    from django.contrib.auth.decorators import login_required

    @login_required
    def protected_view(request):
        return render(request, 'myapp/protected.html')

**Testing**: Create tests in `myapp/tests.py`

.. code-block:: python

    from django.test import TestCase
    from .models import Item

    class ItemModelTest(TestCase):
        def test_string_representation(self):
            item = Item(name="Test Item")
            self.assertEqual(str(item), item.name)

**Run tests**

.. code-block:: bash

    python manage.py test

**Database configuration**: For PostgreSQL, install psycopg2 and update `DATABASES` in `settings.py`

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

**Deployment preparation**: Update `settings.py` for production:    

.. code-block:: python

    DEBUG = False
    ALLOWED_HOSTS = ['your-domain.com']

This guide covers the fundamental aspects of Django. 
As you progress, explore more advanced topics like class-based views, Django REST framework for API development, and integrating with front-end frameworks.

******************************
Resources
******************************

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
