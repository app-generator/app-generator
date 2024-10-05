Dynamic API
===========

This page explains how the **Dynamic API** feature of **Dynamic Django** can be used to expose API endpoints for any model without coding 

.. include::  /_templates/components/signin-invite.rst

Configuration 
-------------

The `django_dyn_api`, the application that handles the feature, is registered in the `INSTALLED_APPS` section. 
`djangorestframework` package being a core dependency, is also registered: 

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        ...
        "django_dyn_api",
        ...
        "rest_framework",
        "rest_framework.authtoken",
        ...
    ]

The DRF Library has a distinct section that configure the authentication layer: 

.. code-block:: python
    :caption: core/settings.py  

    REST_FRAMEWORK = {
        "DEFAULT_AUTHENTICATION_CLASSES": [
            "rest_framework.authentication.SessionAuthentication",
            "rest_framework.authentication.TokenAuthentication",
        ],
    }

**Dynamic API** section (fully covered in the configuration page) provides a simple way to specify the models that are automatically managed. 

The section is a dictionary where the key is the segment of the endpoint and the value the import path of the model. Here are the DEMOs for the default models: 

- `Sales Dynamic API Endpoint <https://dynamic-django.onrender.com/api/sales/>`__: Demo Link 
- `Product Dynamic API Endpoint <https://dynamic-django.onrender.com/api/product/>`__: Demo Link 

.. code-block:: python
    :caption: core/settings.py  

    # Syntax: URI -> Import_PATH
    DYNAMIC_API = {
        "product": "home.models.Product",
        "sales": "home.models.Sales",
    }    


Add a new Model  
---------------

Besides the default API endpoints, the Dynamic API feature can be extended to any new model. 
Here are the steps to enable a new endpoint 

- **Define a new model** `Homework` in the `home` aplication

.. code-block:: python
    :caption: home/models.py  

    class Homework(models.Model):
        id = models.AutoField(primary_key=True)
        title = models.CharField(max_length=100)
        content = models.TextField(blank=True, null=True, default='')

- **Migrate the database** 

.. code-block:: bash

    python manage.py makemigrations
    python manage.py migrate    

- **Update the configuration**: `DYNAMIC_API` section 

.. code-block:: python
    :caption: core/settings.py  

    # Syntax: URI -> Import_PATH
    DYNAMIC_API = {
        "product": "home.models.Product",
        "sales": "home.models.Sales",
        "homework": "home.models.Homework",  # <-- NEW 
    }

- The new endpoint is now listed in the **Dynamic API** and ready to be used. 

.. image:: https://github.com/user-attachments/assets/08855141-059a-491b-aac5-ca5769730ed3
   :alt: Dynamic API - New endpoint registered 

.. image:: https://github.com/user-attachments/assets/5ee3d58c-fe06-488c-a95a-37c3dcc88537
   :alt: Dynamic API - New endpoint DRF view  
   
Resources
---------

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
