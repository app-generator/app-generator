WTForms TextField Import
========================

.. title:: Cannot import name 'TextField' from 'wtforms'     
.. meta::
    :description: This page explains How to Fix ImportError: cannot import name 'TextField' from 'wtforms'

This page explains How to Fix ImportError: cannot import name 'TextField' from 'wtforms'

.. include::  /_templates/components/banner-top.rst

WTForms is a flexible forms validation and rendering library for Python web development. 
It can work with whatever web framework and template engine you choose. It supports data validation, CSRF protection, internationalization (I18N).

.. image:: https://github.com/app-generator/assets/assets/51070104/00f679e5-6dc4-4c44-a11b-056a205915bd
   :alt: WTForms TextField import Error

Error Text
----------

.. code-block:: python

    from wtforms import TextField
    >> ImportError: cannot import name 'TextField' from 'wtforms'

The above error occurs when the `TextField` property is used with [WTForms](https://pypi.org/project/WTForms/) version 3.0 or above 
because the `wtforms.TextField` deprecated in favor of `wtforms.StringField`.

Solution 1
----------

Replace `TextField` type with `StringField`. This solution works with WTForms 3.x and 2.x versions

.. code-block:: python

    from wtforms import StringField
    // replace all TextField usages with StringField type

Solution 2 
----------

Use the latest stable 2.x version of WTForms

.. code-block:: bash

    // Use 2.x version
    pip install WTForms==2.3.3

Using an older version provides a quick fix for your codebase but is not recommended in the long run.

.. include::  /_templates/components/footer-links.rst
