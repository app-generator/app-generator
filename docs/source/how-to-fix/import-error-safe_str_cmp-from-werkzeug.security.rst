Werkzeug 'safe_str_cmp' Import
==============================

.. title:: Cannot import name 'TextField' from 'wtforms'     
.. meta::
    :description: This page explains How to Fix ImportError: cannot import name 'safe_str_cmp' from 'werkzeug.security'

This page explains How to Fix ImportError: cannot import name 'safe_str_cmp' from 'werkzeug.security'

.. include::  /_templates/components/banner-top.rst

Werkzeug the core dependency of **Flask**, is a comprehensive WSGI web application library. Version **v2.1.0** deprecates a few helpers, including `safe_str_cmp.` Here is the update history:

    v2.0.0

`pbkdf2_hex`, `pbkdf2_bin`, and `safe_str_cmp` are deprecated. `hashlib` and `hmac` provide equivalents.

    v2.1.0

Remove the `pbkdf2_hex`, `pbkdf2_bin`, and `safe_str_cmp` functions. Use equivalents in `hashlib` and `hmac` modules instead.

How to Fix
----------

Freeze the `Werkzeug` to the latest stable version prior to v2.1.0. The recommended version is **Werkzeug==2.0.3.**

Sample Project
--------------

To see this hot fix in action, feel free to check this sample project (MIT License):

- 👉 `Datta Able Flask </product/datta-able/flask/>`__ - Product Page (contains download link)
- 👉 `Datta Able Flask <https://flask-datta-demo.onrender.com>`__ - LIVE Demo 

.. include::  /_templates/components/footer-links.rst
