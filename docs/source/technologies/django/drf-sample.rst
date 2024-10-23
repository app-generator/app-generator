DRF Sample
==========

This page explains the fastest way to expose a secure API on top of a Django model.
Securing a `Django </docs/technologies/django.html>`_ API using the Django REST Framework is a straightforward process. 

The DRF ecosystem provides many ways to secure your API using basic authentication or tokens. 
Here, we will show you how to easily secure an API for a model created in Django using `Djoser <https://djoser.readthedocs.io/en/latest/>`_.

.. include::  /_templates/components/banner-top.rst


Project Setup
-------------

To follow this article, create a small project and install the necessary dependencies.

.. code-block:: bash

    mkdir django-api
    cd django-api
    python3 -m venv venv
    source venv/bin/activate

Then install Django, Django REST Framework, Djoser, and JWT-related libraries.

.. code-block:: bash

    pip install django djangorestframework djoser djangorestframework-simplejwt
    django-admin startproject SecureProject .

Once installed, add the necessary apps to your Django project`s ``INSTALLED_APPS``:

.. code-block:: python

    # SecureProject/settings.py

    INSTALLED_APPS = [
        ...
        'rest_framework',
        'djoser',
        'rest_framework_simplejwt.token_blacklist',
    ]

Once it`s done, configure DRF to use JWT for authentication by including the ``DEFAULT_AUTHENTICATION_CLASSES`` in the ``REST_FRAMEWORK`` variable in ``settings.py``.

.. code-block:: python

    # SecureProject/settings.py

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
    }

In addition, configure SimpleJWT with the following settings to handle JWT tokens:

.. code-block:: python

    # SecureProject/settings.py

    from datetime import timedelta
    ...
    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
        'ROTATE_REFRESH_TOKENS': True,
        'BLACKLIST_AFTER_ROTATION': True,
        'AUTH_HEADER_TYPES': ('Bearer',),
    }

In the configuration above:

* The access token ``ACCESS_TOKEN_LIFETIME`` expires after 15 minutes, and the refresh token ``REFRESH_TOKEN_LIFETIME`` lasts for 1 day.
* Refresh token rotation ``ROTATE_REFRESH_TOKENS`` is enabled, meaning a new refresh token is issued each time the access token is refreshed, and the old one is blacklisted (``BLACKLIST_AFTER_ROTATION``) to prevent reuse.
* Tokens are sent in the Authorization header ``AUTH_HEADER_TYPES`` using the ``Bearer`` scheme.

Now, let`s write the Djoser URLs.

.. code-block:: python

    # SecureProject/urls.py

    from django.urls import path, include

    urlpatterns = [
        path('auth/', include('djoser.urls')),
        path('auth/', include('djoser.urls.jwt')),
    ]

The code above will automatically expose authentication endpoints such as:

* ``/auth/jwt/create/`` – for obtaining a JWT token
* ``/auth/jwt/refresh/`` – for refreshing the JWT token
* ``/auth/jwt/verify/`` – to verify the validity of the token

The project is set, and we can now move to adding the Transaction models and securing it.

Adding the Transaction Application
-----------------------------------

Next, we will quickly write code for the transaction endpoints we will expose. Let`s start by creating a Django application.

.. code-block:: bash

    python manage.py startapp transactions

We can now write the model.

Creating the Transaction Model
------------------------------

Next, let`s define a simple transaction model, which will be secured using JWT authentication.

.. code-block:: python

    # transactions/models.py

    from django.db import models
    from django.contrib.auth.models import User

    class Transaction(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        amount = models.DecimalField(max_digits=10, decimal_places=2)
        description = models.TextField()
        timestamp = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"Transaction by {self.user.username} - {self.amount}"

Register the app in the ``INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'transactions',
    ]

Finally, run migrations to create the transaction table:

.. code-block:: bash

    python manage.py makemigrations
    python manage.py migrate

We can now add the transactions API endpoint.

Creating the Transaction API Endpoint
-------------------------------------

Now, let`s create a DRF viewset to expose the transaction model securely. First, create a serializer for the Transaction model.

.. code-block:: python

    # transactions/serializers.py

    from rest_framework import serializers
    from .models import Transaction

    class TransactionSerializer(serializers.ModelSerializer):
        class Meta:
            model = Transaction
            fields = ['id', 'user', 'amount', 'description', 'timestamp']

Then, create a viewset to handle the transactions, ensuring it`s protected with JWT authentication.

.. code-block:: python

    # transactions/views.py

    from rest_framework import viewsets
    from rest_framework.permissions import IsAuthenticated
    from .models import Transaction
    from .serializers import TransactionSerializer

    class TransactionViewSet(viewsets.ModelViewSet):
        queryset = Transaction.objects.all()
        serializer_class = TransactionSerializer
        permission_classes = [IsAuthenticated]

        def get_queryset(self):
            # Return only the transactions for the authenticated user
            return Transaction.objects.filter(user=self.request.user)

The code above defines a ``TransactionViewSet`` that provides CRUD operations for the Transaction model, restricted to authenticated users. 
The ``get_queryset`` method ensures that only transactions belonging to the authenticated user are returned, enforcing user-level data filtering.

Now, register the transaction view in your Django project`s URLs.

.. code-block:: python

    # transactions/urls.py

    from rest_framework.routers import DefaultRouter
    from .views import TransactionViewSet

    router = DefaultRouter()
    router.register(r'transactions', TransactionViewSet, basename='transaction')

    urlpatterns = router.urls

Include these URLs in the main ``urls.py`` file of the project:

.. code-block:: python

    # secure_api/urls.py

    from django.urls import path, include

    urlpatterns = [
        path('auth/', include('djoser.urls')),
        path('auth/', include('djoser.urls.jwt')),
        path('api/', include('transactions.urls')),
    ]

Once it`s done, ensure that the project is running by typing this command.

.. code-block:: bash

    python manage runserver

The API will be running at http://localhost:8000.

Adding Pagination
-----------------

@TODO 

Adding Search
-------------

@TODO 

Document the API
----------------

@TODO 

Testing the API
---------------

You can now test the secured API using tools like **curl** or **Postman**. First, register a user via the Djoser registration endpoint, then log in to get a JWT token. 
Use the token to authenticate requests to the ``/transactions/`` endpoint to list, create, or manage transaction records.

Example JWT Authentication Flow:

1. **Register a user**:

.. code-block:: bash

    curl -X POST http://localhost:8000/auth/users/ \
    -H "Content-Type: application/json" \
    -d '{"username": "user", "password": "password123"}'

2. **Obtain a JWT Token**:

.. code-block:: bash

    curl -X POST http://localhost:8000/auth/jwt/create/ \
    -H "Content-Type: application/json" \
    -d '{"username": "user", "password": "password123"}'

The response will include the ``access`` and ``refresh`` tokens. Use the ``access`` token in the Authorization header for the next requests.

3. **Use the JWT Token to access the transactions endpoint**:

.. code-block:: bash

    curl -X GET http://localhost:8000/transactions/ \
    -H "Authorization: Bearer <your-token-here>"

Using Postman
-------------

You can also test this flow in Postman by creating POST requests to the registration and login endpoints, 
and then including the JWT token in the ``Authorization`` header as a ``Bearer`` token to access the transactions endpoint.

Conclusion
----------

Using **Djoser** with **JWT** makes securing a Django REST API easy. With Djoser's built-in views and JWT token handling, you can implement secure authentication for your APIs quickly. 
This example demonstrates securing a transactions endpoint, but Djoser can extend to more complex authentication needs effortlessly.

You can read more about Djoser on their official `documentation <https://djoser.readthedocs.io/en/latest/>`_.


.. include::  /_templates/components/footer-links.rst
