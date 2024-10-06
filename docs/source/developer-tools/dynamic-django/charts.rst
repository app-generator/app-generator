Dynamic Charts
==============

.. title:: Dynamic Charts -  Dynamic Django Starter      
.. meta::
    :description: Showcase different chart types for any model without coding using Dynamic Charts feature via Dynamic Django  
    :keywords: dynamic charts, dynamic shocase data, dynamic django, dynamic programming, dynamic patterns

This page explains how to use the **Dynamic Charts** feature of `Dynamic Django Tool <./index.html>`__ that allows to showcase different chart types for any model without coding. 

.. include::  /_templates/components/signin-invite.rst

Configuration 
-------------

Extracting reports from a source can be a challenging task and Dynamic Charts module aims to solve this task in an easy way.
In order to activate the reports extraction, the model needs to be added in settings. 

The section is a list of rules saved in a dictionary where the key is the path where the **Dynamic Chart** feature is provided and the value is the import path of the model.  

.. code-block:: python
    :caption: core/settings.py  

    # Syntax: URI -> Import_PATH
    DYNAMIC_CHARTS = {
        "product": "home.models.Product",
        "sales": "home.models.Sales",
    }  

How it works 
------------

The information is extracted and later showcased using a chart template where the user can edit a few properties like:

* **Chart Type**: almost every popular type is supported: LINE, BAR, DONUT, RADAR .. etc 
* **X-Axis** column 
* **Y-Axis** column 
* Other column requsted by that speficic chart type 
* Each property can be preprocessed via filter like date-processor, uppercase .. etc 

In the end, the `chart template` is applied on the model data and the charts displayed to the users using real data. 

UI Sections 
------------

All models registered in "settings.DYNAMIC_CHARTS" are shown in the home page of `charts <https://dynamic-django.onrender.com/dynamic-charts/>`__ section: 

.. image:: https://github.com/user-attachments/assets/9bcc0f74-fafa-4431-a237-61938c3834c2
   :alt: Dynamic Django - HOMEpage of the Dynamic Charts module 

When a model is selected, we can see all defined templates and also we can inspect the information on page or the embedded format, that can be integrated in external services. 

- Top section exposes three TABS
    - DataTable for data saved in the model 
    - Add Item can be used to add a new item on the model 
    - Add Chart: define a new chart 
- 2nd Section
    - Table with all the charts defined for the current model 

.. image:: https://github.com/user-attachments/assets/b7c12989-365b-4838-b5c3-305b638b63aa
   :alt: Dynamic Charts - The table with all defined chart templates 
    
- Chart Section (bottom)
    - This section becomes visible when the user clicks the `view` link for a specific chart. For instance this is shown for a POLAR chart 

.. image:: https://github.com/user-attachments/assets/18765f7c-7a46-448d-8998-e1d6b93f1fc9
   :alt: Dynamic Charts - POLAR Chart Sample, extracted from the sales DB Table      

- Embeddable Form 
    - Each defined chart can be integrated into external systems via external link that provides the chart without any styles
    - For a DONUT Chart, here is the `Embeddable Link <https://dynamic-django.onrender.com/dynamic-charts/embed/10/>`__  

.. image:: https://github.com/user-attachments/assets/5d60998d-db12-477b-a323-ea1dae5e1e21
   :alt: Dynamic Charts - DONUT Chart Sample, embeddable form  

Resources
---------

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
