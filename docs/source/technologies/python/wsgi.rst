WSGI
====

WSGI (Web Server Gateway Interface) is a specification for a standardized interface between web servers and Python web applications or frameworks. 
It defines how a web server communicates with Python web applications and how these applications can be chained together to process a request.

.. include::  /_templates/components/banner-top.rst

Key aspects of WSGI
-------------------

1. It acts as a common interface between Python web applications and web servers
2. It allows Python web applications to be portable across different web servers
3. It enables middleware components that can process requests and responses

WSGI consists of two sides:
- The "server side" or "gateway side" (web servers like Apache, Nginx with uWSGI)
- The "application side" or "framework side" (Flask, Django, etc.)

A WSGI application is essentially a callable (function or class with a `__call__` method) that:
- Takes two parameters: a dictionary containing environment variables and a callback function
- Returns an iterable of response body content

Simple WSGI applications can be written directly, while more complex ones are typically built using frameworks like Flask or Django, which handle the WSGI interface internally.

Popular WSGI servers include:
- Gunicorn
- uWSGI
- mod_wsgi (Apache module)
- Waitress

WSGI was developed to solve the problem of Python web framework proliferation without standardization, making it easier to deploy Python web applications in production environments.

.. include::  /_templates/components/footer-links.rst
