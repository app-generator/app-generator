Dynamic API
===========

This page explains how the **Dynamic API** feature of **Dynamic Django** can be used to expose API endpoints for any model without coding 

.. include::  /_templates/components/signin-invite.rst

Configuration 
-------------

The `django_dyn_api`, the application that handles the feature, is registered in the `INSTALLED_APPS` section. 
`djangorestframework` package being a core dependency, is also registered: 

.. code-block:: python

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

    # Syntax: URI -> Import_PATH
    DYNAMIC_API = {
        "product": "home.models.Product",
        "sales": "home.models.Sales",
    }    


******************************
Resources
******************************

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
