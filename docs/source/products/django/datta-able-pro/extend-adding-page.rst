Extend - Adding Page  
====================

This page explains how to extend Django Datta PRO by adding a new page.

Prerequisites
-------------

The source code of `Django Datta Able PRO </product/datta-able-pro/django/>`__ needs to be downloaded locally. 

Templates Directory
-------------------

Navigate and inspect the `templates` directory located in the root of the project. The structure is the one presented bellow   

.. code-block:: bash   

    < PROJECT ROOT >
    |
    |-- templates/                   # Pages & Templates   
    |    |
    |    |-- includes/               # UI Components
    |    |-- layouts/                # Master pages
    |    |-- pages/                  # Pages provided by the Datta Able Kit
    |         |
    |         |-- index.html         # Index Page 
    |         |-- landingpage.html   # Sample Landing page 
    |         |-- *.html             # All other pages
    |
    |-- ************************************************************************


Duplicate Existing Page
-----------------------

To keep this tutorial simple, we will copy the **landingpage.html** into a new page named **mypage.html**. Once we do this, the templates directory becomes: 


.. code-block:: bash   

    < PROJECT ROOT >
    |
    |-- templates/                   # Pages & Templates   
    |    |
    |    |-- pages/                  # Pages provided by the Datta Able Kit
    |         |
    |         |-- landingpage.html    
    |         |-- mypage.html        # <-- Our NEW page  
    |
    |-- ************************************************************************


Use the Page
------------

The page can be used now and presented to the users. For this let's create a new route in the **home** application. 

.. code-block:: bash   

    < PROJECT ROOT >
    |
    |-- home/              # HOME Application
    |    |-- urls.py       # Application routes
    |    |-- views.py      # Application controlers
    |
    |-- ************************************************************************


**Edit views.py** - addind a new controller for the new page   

.. code-block:: python

    # Landing Page                                           # Existing CODE  
    @login_required(login_url='/accounts/login-v1/')         # Existing CODE
    def landing_page(request):                               # Existing CODE
        return render(request, 'pages/landingpage.html')     # Existing CODE


    # My NEW Page                                            # <-- NEW CODE  
    def my_page(request):                                    # <-- NEW CODE
        return render(request, 'pages/my.html')              # <-- NEW CODE


**Edit urls.py** - addind a new route for the page 

.. code-block:: python

    urlpatterns = [                                                        # Existing CODE
        path('', views.default, name='index'),                             # Existing CODE
        path('landing-page/', views.landing_page, name="landing_page"),    # Existing CODE 
        ... 
        path('my_page/', views.my_page, name="my_page"),                   # <-- NEW CODE
        ... 
    ]

Once the above edits are finished and saved, our new page is rendered when we access the new `route`:

**Access the page**: `http://localhost:8000/my_page/`

.. include::  /_templates/components/footer-links.rst
