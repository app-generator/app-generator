Gunicorn
========

Gunicorn, short for "Green Unicorn," is a Python WSGI HTTP server for Unix systems. 
It's a pre-fork worker model server that's widely used to deploy Python web applications, particularly those built with frameworks like Flask and Django.

.. include::  /_templates/components/banner-top.rst


Key features of Gunicorn
------------------------

1. **Production-Ready**: Designed specifically for production environments with reliability and performance in mind.

2. **Process Management**: Uses a master-worker architecture where a master process manages multiple worker processes that handle requests.

3. **Worker Types**: Supports various worker types including sync, async, gevent, and eventlet to handle different concurrency models.

4. **Auto-Worker Restart**: Automatically restarts workers that crash or exceed memory limits.

5. **Configuration Options**: Highly configurable through command-line options or config files.

6. **Integration**: Works well with Nginx or other reverse proxies in front of it.

7. **Signal Handling**: Graceful application reloading without dropping connections.

A typical deployment architecture:

- Nginx as the front-facing web server (handling static files, SSL, etc.)
- Gunicorn as the application server
- Your Python web application (Django, Flask, etc.)

Example of starting Gunicorn:

.. code-block:: bash

    gunicorn myapp.wsgi:application --workers=4 --bind=0.0.0.0:8000


Example configuration file (gunicorn.conf.py):

.. code-block:: python

    bind = "0.0.0.0:8000"
    workers = 4
    worker_class = "gevent"
    worker_connections = 1000
    timeout = 30
    keepalive = 2

Gunicorn is valued for its simplicity, reliability, and performance characteristics, making it one of the most popular choices for deploying Python web applications in production.

.. include::  /_templates/components/footer-links.rst
