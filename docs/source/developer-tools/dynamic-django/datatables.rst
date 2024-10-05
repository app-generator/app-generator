Dynamic DataTables 
==================

This page explains how the **Dynamic DataTables** feature of **Dynamic Django** can be used to manage any DB table using a powerful paginated view  

.. include::  /_templates/components/signin-invite.rst

Configuration 
-------------

The `django_dyn_dt`, the application that handles the feature, is registered in the `INSTALLED_APPS` section. 

.. code-block:: python
    :caption: core/settings.py  

    INSTALLED_APPS = [
        ...
        "django_dyn_api",
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

**Dynamic API** section (also covered in the configuration page) provides a simple way to specify the models that are automatically managed. 

The section is a dictionary where the key is the segment of the endpoint and the value the import path of the model. Here are the DEMOs for the default models: 

- `Sales Dynamic Tables View <https://dynamic-django.onrender.com/dynamic-dt/sales/>`__: Demo Link 
- `Product Dynamic Tables View <https://dynamic-django.onrender.com/dynamic-dt/product/>`__: Demo Link 

.. code-block:: python
    :caption: core/settings.py  

    # Syntax: URI -> Import_PATH
    DYNAMIC_DATATB = {
        "product": "home.models.Product",
        "sales": "home.models.Sales",
    }    


Add a new Model  
---------------

Besides the default tables view (Sales and Product models), the Dynamic DataTable feature can be extended to any new model. 
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
    DYNAMIC_DATATB = {
        "product": "home.models.Product",
        "sales": "home.models.Sales",
        "homework": "home.models.Homework",  # <-- NEW 
    }

- **The new view** is now listed in the **Dynamic DataTable** page and ready to be used. 

.. image:: https://github.com/user-attachments/assets/4e2f2739-c34a-4714-865b-33f7da48950d
   :alt: Dynamic DataTable - New view (model) registered 

- **The new DataTable** for the newly created model 

.. image:: https://github.com/user-attachments/assets/a4d4c311-10cb-4682-a9bd-7fa61be3febe
   :alt: Dynamic DataTable - New view for the Homework Model   
   
Resources
---------

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
