:og:description: HTMX - Resources for students and developers | App-Generator.dev

htmx
====

.. title:: HTMX - Resources for students and developers | App-Generator.dev
.. meta::
    :description: Unified index for HTMX resources: tutorials, starters, best practices and dev tips

HTMX is a modern JavaScript library that allows you to access AJAX, CSS transitions, WebSockets, and Server-Sent Events directly in HTML, without writing JavaScript. 
When paired with a backend framework like `Django </docs/technologies/django/index.html>`__, it creates a powerful combination that simplifies building dynamic web applications.

.. include::  /_templates/components/banner-top.rst

By `using HTMX with Django </docs/products/django/rocket-htmx/index.html>`__ , you can create interactive user experiences while keeping most of your logic server-side. HTMX works by adding special attributes to your HTML elements that trigger HTTP requests when certain events occur. 
Django then processes these requests and returns HTML fragments that HTMX seamlessly incorporates into the page.

This approach offers several benefits: it reduces the complexity of building interactive applications, eliminates the need for a separate JavaScript frontend framework, 
maintains Django's templates as the single source of truth for your UI, and allows for progressive enhancement of your web applications. 
The result is a more maintainable codebase with less context-switching between languages and frameworks.

For developers familiar with Django's templating system, HTMX feels like a natural extension that brings modern interactivity without the overhead of a complex JavaScript ecosystem.

`Rocket HTMX </product/rocket-htmx/django/>`__ 
-----------------------------------------------

**Django Rocket HTMX** is an open-source starter built with basic modules, authentication, data tables, charts, API and `HTMX </docs/technologies/htmx/index.html>`__ support.
The product UI is styled with **Flowbite**, an open source collection of UI components built with the utility classes from Tailwind CSS. 

- 👉 `Django Rocket HTMX </product/rocket-htmx/django/>`__ - Product Page (contains download link)
- 👉 `Django Rocket HTMX <https://rocket-django-htmx.onrender.com/>`__ - LIVE Demo

Features
********

- Simple, Easy-to-Extend codebase
- Styling: Flowbite/Tailwind
- Extended User Model
- ApexJS Charts
- DataTables via `HTMX </docs/technologies/htmx/index.html>`__
- API
- DB Persistence: SQLite (default), can be used with MySql, PgSql
- Docker 
- CI/CD integration for Render 

.. image:: https://github.com/user-attachments/assets/d7527d5e-046c-4679-8f72-525290a5edd5
   :alt: Django Rocket HTMX - Open-source Starter powered by HTMX and Tailwind 

Resources
---------

.. toctree::
   :maxdepth: 1
   
   htmx/index
