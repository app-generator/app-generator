:og:description: Django REST Framework (DRF) Tutorial - Build Secure APIs like a PRO

DRF Tutorial
============

.. title:: Django REST Framework (DRF) Tutorial - Build Secure APIs like a PRO   
.. meta::
    :description: Learn how to write a code secure APIs using Django REST Framework
    :keywords: drf tutorial, Django Rest Framework, drf and django, drf free tutorial 

Django REST Framework (DRF) extends Django's capabilities to easily build RESTful APIs. 
It provides serialization, authentication, viewsets, and many other features that make API development efficient and maintainable.

.. include::  /_templates/components/banner-top.rst

Key Features
------------

- Powerful serialization system
- Class-based views and viewsets
- Authentication and permissions
- Browsable API
- Pagination, filtering, and searching
- Extensive documentation


Installation and Setup
-----------------------

Let's start by installing DRF and setting it up in a Django project:

.. code-block:: python

    # Install Django and Django REST framework
    pip install django
    pip install djangorestframework

    # Create a new Django project
    django-admin startproject myproject
    cd myproject

    # Create an app
    python manage.py startapp api


Update your `settings.py` to include the REST framework:

.. code-block:: python

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'api',
    ]

    # REST Framework settings
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.BasicAuthentication',
        ],
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
    }


Models
------

Let's create a simple model in our app:

.. code-block:: python

    # api/models.py
    from django.db import models

    class Book(models.Model):
        title = models.CharField(max_length=100)
        author = models.CharField(max_length=100)
        isbn = models.CharField(max_length=13, unique=True)
        published_date = models.DateField()
        
        def __str__(self):
            return self.title

After defining your model, run migrations:

.. code-block:: python

    python manage.py makemigrations
    python manage.py migrate


Serializers
-----------

Serializers allow complex data like querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML, or other content types. 
They also provide deserialization, allowing parsed data to be converted back into complex types.

.. code-block:: python

    # api/serializers.py
    from rest_framework import serializers
    from .models import Book

    class BookSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ['id', 'title', 'author', 'isbn', 'published_date']
            
        def validate_isbn(self, value):
            """
            Check that the ISBN is a valid 13-digit number
            """
            if len(value) != 13 or not value.isdigit():
                raise serializers.ValidationError("ISBN must be a 13-digit number")
            return value

Serializer Types
****************

1. **ModelSerializer**: Automatically generates fields based on the model
2. **HyperlinkedModelSerializer**: Uses hyperlinks for relationships
3. **Serializer**: Base class for more custom serialization


Views
-----

DRF provides several types of views for handling API requests.

Function-based views
********************

.. code-block:: python

    # api/views.py
    from rest_framework import status
    from rest_framework.decorators import api_view
    from rest_framework.response import Response
    from .models import Book
    from .serializers import BookSerializer

    @api_view(['GET', 'POST'])
    def book_list(request):
        """
        List all books, or create a new book.
        """
        if request.method == 'GET':
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        
        elif request.method == 'POST':
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    @api_view(['GET', 'PUT', 'DELETE'])
    def book_detail(request, pk):
        """
        Retrieve, update or delete a book instance.
        """
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = BookSerializer(book)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

Class-based views
*****************

.. code-block:: python

    # api/views.py (class-based version)
    from rest_framework import generics
    from .models import Book
    from .serializers import BookSerializer

    class BookList(generics.ListCreateAPIView):
        queryset = Book.objects.all()
        serializer_class = BookSerializer

    class BookDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Book.objects.all()
        serializer_class = BookSerializer

ViewSets
********

ViewSets combine the logic for multiple related views into a single class:

.. code-block:: python

    # api/views.py (viewset version)
    from rest_framework import viewsets
    from .models import Book
    from .serializers import BookSerializer

    class BookViewSet(viewsets.ModelViewSet):
        """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.
        """
        queryset = Book.objects.all()
        serializer_class = BookSerializer

URL Routing
-----------

**For function-based and class-based views**:

.. code-block:: python


    # api/urls.py
    from django.urls import path
    from rest_framework.urlpatterns import format_suffix_patterns
    from api import views

    urlpatterns = [
        path('books/', views.BookList.as_view()),
        path('books/<int:pk>/', views.BookDetail.as_view()),
    ]

    urlpatterns = format_suffix_patterns(urlpatterns)

**For ViewSets**:

.. code-block:: python

    # api/urls.py (for viewsets)
    from django.urls import path, include
    from rest_framework.routers import DefaultRouter
    from api import views

    router = DefaultRouter()
    router.register(r'books', views.BookViewSet)

    urlpatterns = [
        path('', include(router.urls)),
    ]

Don't forget to include your app URLs in the project:

.. code-block:: python

    # myproject/urls.py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include('api.urls')),
        path('api-auth/', include('rest_framework.urls')),
    ]


Authentication and Permissions
------------------------------

DRF provides a powerful system for authentication and permissions:

Authentication
**************

.. code-block:: python

    # settings.py excerpt
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
        ],
    }

For token authentication, add `'rest_framework.authtoken'` to `INSTALLED_APPS` and run migrations.

Permissions
***********

.. code-block:: python

    # api/views.py
    from rest_framework import permissions

    class BookViewSet(viewsets.ModelViewSet):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        
        def get_permissions(self):
            """
            Instantiates and returns the list of permissions that this view requires.
            """
            if self.action == 'list':
                permission_classes = [permissions.IsAuthenticated]
            else:
                permission_classes = [permissions.IsAdminUser]
            return [permission() for permission in permission_classes]

You can also create custom permissions:

.. code-block:: python

    # api/permissions.py
    from rest_framework import permissions

    class IsOwnerOrReadOnly(permissions.BasePermission):
        """
        Custom permission to only allow owners of an object to edit it.
        """
        def has_object_permission(self, request, view, obj):
            # Read permissions are allowed to any request
            if request.method in permissions.SAFE_METHODS:
                return True
                
            # Write permissions are only allowed to the owner
            return obj.owner == request.user

Filtering and Pagination
------------------------

Filtering
*********

.. code-block:: python

    # api/views.py
    from django_filters.rest_framework import DjangoFilterBackend
    from rest_framework import filters

    class BookViewSet(viewsets.ModelViewSet):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
        filterset_fields = ['author', 'published_date']
        search_fields = ['title', 'author']
        ordering_fields = ['published_date', 'title']

You'll need to install django-filter:

.. code-block:: python

    pip install django-filter

And add it to your INSTALLED_APPS:

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'django_filters',
    ]

    REST_FRAMEWORK = {
        # ...
        'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    }


Pagination
**********

.. code-block:: python

    # settings.py
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,
    }

You can also create custom pagination classes:

.. code-block:: python

    # api/pagination.py
    from rest_framework.pagination import PageNumberPagination

    class LargeResultsSetPagination(PageNumberPagination):
        page_size = 100
        page_size_query_param = 'page_size'
        max_page_size = 1000

    class StandardResultsSetPagination(PageNumberPagination):
        page_size = 10
        page_size_query_param = 'page_size'
        max_page_size = 100

Then apply it to your view:

.. code-block:: python

    # api/views.py
    from .pagination import StandardResultsSetPagination

    class BookViewSet(viewsets.ModelViewSet):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        pagination_class = StandardResultsSetPagination


Nested Resources
----------------

Let's add a new model for book reviews:

.. code-block:: python

    # api/models.py
    class Review(models.Model):
        book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
        reviewer = models.CharField(max_length=100)
        content = models.TextField()
        rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
        created_at = models.DateTimeField(auto_now_add=True)
        
        class Meta:
            ordering = ['-created_at']

Add a serializer for the review model and update the book serializer:

.. code-block:: python

    # api/serializers.py
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ['id', 'reviewer', 'content', 'rating', 'created_at']
            
    class BookSerializer(serializers.ModelSerializer):
        reviews = ReviewSerializer(many=True, read_only=True)
        
        class Meta:
            model = Book
            fields = ['id', 'title', 'author', 'isbn', 'published_date', 'reviews']

Create a nested view for reviews:

.. code-block:: python

    # api/views.py
    class ReviewViewSet(viewsets.ModelViewSet):
        serializer_class = ReviewSerializer
        
        def get_queryset(self):
            return Review.objects.filter(book_id=self.kwargs['book_pk'])
        
        def perform_create(self, serializer):
            serializer.save(book_id=self.kwargs['book_pk'])

Update the URL configuration for nested resources:

.. code-block:: python

    # api/urls.py
    from rest_framework_nested import routers
    from .views import BookViewSet, ReviewViewSet

    router = routers.DefaultRouter()
    router.register(r'books', BookViewSet)

    books_router = routers.NestedDefaultRouter(router, r'books', lookup='book')
    books_router.register(r'reviews', ReviewViewSet, basename='book-reviews')

    urlpatterns = [
        path('', include(router.urls)),
        path('', include(books_router.urls)),
    ]

You'll need to install the DRF nested routers package:

.. code-block:: python

    pip install drf-nested-routers


Versioning
----------

DRF provides API versioning to help you manage changes to your API over time:

.. code-block:: python

    # settings.py
    REST_FRAMEWORK = {
        'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
        'DEFAULT_VERSION': 'v1',
        'ALLOWED_VERSIONS': ['v1', 'v2'],
        'VERSION_PARAM': 'version',
    }


Update your URLs:

.. code-block:: python

    # myproject/urls.py
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/<str:version>/', include('api.urls')),
        path('api-auth/', include('rest_framework.urls')),
    ]


Then in your views:

.. code-block:: python

    # api/views.py
    class BookViewSet(viewsets.ModelViewSet):
        queryset = Book.objects.all()
        
        def get_serializer_class(self):
            if self.request.version == 'v1':
                return BookSerializerV1
            return BookSerializerV2


Testing
-------

DRF provides testing utilities that extend Django's existing test framework:

.. code-block:: python

    # api/tests.py
    from django.urls import reverse
    from rest_framework import status
    from rest_framework.test import APITestCase
    from .models import Book

    class BookTests(APITestCase):
        def test_create_book(self):
            """
            Ensure we can create a new book object.
            """
            url = reverse('book-list')
            data = {
                'title': 'Django REST Framework',
                'author': 'Django Team',
                'isbn': '9781234567890',
                'published_date': '2020-01-01'
            }
            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Book.objects.count(), 1)
            self.assertEqual(Book.objects.get().title, 'Django REST Framework')
            
        def test_get_books(self):
            """
            Ensure we can retrieve the book list.
            """
            Book.objects.create(
                title='Django REST Framework',
                author='Django Team',
                isbn='9781234567890',
                published_date='2020-01-01'
            )
            url = reverse('book-list')
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data['results']), 1)


Throttling
----------

Throttling is used to control the rate of requests that clients can make to your API:

.. code-block:: python

    # settings.py
    REST_FRAMEWORK = {
        'DEFAULT_THROTTLE_CLASSES': [
            'rest_framework.throttling.AnonRateThrottle',
            'rest_framework.throttling.UserRateThrottle'
        ],
        'DEFAULT_THROTTLE_RATES': {
            'anon': '100/day',
            'user': '1000/day'
        }
    }

For specific views:

.. code-block:: python

    # api/views.py
    from rest_framework.throttling import UserRateThrottle

    class BookViewSet(viewsets.ModelViewSet):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        throttle_classes = [UserRateThrottle]


Content Negotiation
-------------------

DRF supports rendering responses in multiple formats:

.. code-block:: python

    # settings.py
    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
            'rest_framework.renderers.XMLRenderer',
        ],
    }

Conclusion
----------

Django REST Framework is a comprehensive toolkit that simplifies the process of building RESTful APIs. 
It provides powerful features like serialization, authentication, viewsets, and more, all while maintaining the ease of use that Django is known for.

This tutorial covered the basics to get you started, but DRF offers much more. Check the official documentation for advanced features and best practices.

.. include::  /_templates/components/footer-links.rst
