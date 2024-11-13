Deploy Flask
============

.. title:: Flask Deployment Guide for Fly.io
.. meta::
    :description: Learn how to deploy Flask projects on Fly.io  
    :keywords: flask fly.io, flask fly.io cloud, flask fly.io deployment, fly.io cloud tools, deploy, ci-cd, deployment  

This page explains how to deploy a `Flask <../../technologies/flask/index.html>`__ project on `Fly.io <./index.html>`__, the popular deployment platform for developers. 

.. include::  /_templates/components/banner-top.rst

Framework Overview
------------------

Flask is a lightweight WSGI web application framework written in Python. It implements a minimalistic core that can be extended with numerous official and community-created extensions. 
Flask's modular architecture makes it particularly suitable for microservices and API development, while maintaining the capability to scale into complex applications.

Deployment Configuration
------------------------

Project Structure
*****************

A standard Flask application structure for deployment:

..	code-block:: bash


    ├── app/
    │   ├── __init__.py
    │   ├── models.py
    │   ├── routes.py
    │   └── templates/
    ├── Dockerfile
    ├── requirements.txt
    ├── gunicorn.conf.py
    └── wsgi.py

Essential Files Configuration
*****************************

1. `requirements.txt`:

..	code-block:: text 

    Flask==3.0.0
    gunicorn==21.2.0
    python-dotenv==1.0.0
    Werkzeug==3.0.1
    # Add other dependencies as needed


2. `wsgi.py`:

..	code-block:: python

    from app import create_app

    app = create_app()

    if __name__ == "__main__":
        app.run()

3. `gunicorn.conf.py`:

..	code-block:: python

    # Gunicorn configuration
    workers = 4
    bind = "0.0.0.0:8080"
    worker_class = "gthread"
    threads = 2
    timeout = 120


4. `Dockerfile`:

..	code-block:: dockerfile

    # Use Python 3.11 slim image
    FROM python:3.11-slim

    # Set working directory
    WORKDIR /app

    # Install system dependencies
    RUN apt-get update && apt-get install -y \
        build-essential \
        python3-dev \
        && rm -rf /var/lib/apt/lists/*

    # Install Python dependencies
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy application code
    COPY . .

    # Set environment variables
    ENV FLASK_APP=wsgi.py
    ENV FLASK_ENV=production
    ENV PYTHONUNBUFFERED=1

    # Expose port
    EXPOSE 8080

    # Start Gunicorn
    CMD ["gunicorn", "--config", "gunicorn.conf.py", "wsgi:app"]


5. `.dockerignore`:

..	code-block:: bash

    __pycache__
    *.pyc
    *.pyo
    *.pyd
    .Python
    env/
    venv/
    .env
    *.log
    .git/
    .gitignore


Fly.io Configuration
********************

1. `fly.toml`:

..	code-block:: toml

    app = "your-flask-app"
    primary_region = "dfw"

    [build]
        dockerfile = "Dockerfile"

    [env]
        PORT = "8080"

    [http_service]
        internal_port = 8080
        force_https = true
        auto_stop_machines = true
        auto_start_machines = true
        min_machines_running = 1
        processes = ["app"]

    [[vm]]
        cpu_kind = "shared"
        cpus = 1
        memory_mb = 256

Deployment Process
------------------

1. Initialize Fly.io application:

..	code-block:: bash 

    fly launch

2. Configure environment variables:

..	code-block:: bash 

    fly secrets set FLASK_SECRET_KEY="your-secret-key"
    fly secrets set DATABASE_URL="your-database-url"

3. Deploy the application:

..	code-block:: bash 

    fly deploy

4. Validate deployment:

..	code-block:: bash 

    fly status

Database Integration
--------------------

For PostgreSQL database integration:

1. Create a Fly PostgreSQL cluster:

..	code-block:: bash 

    fly postgres create


2. Attach database to your application:

..	code-block:: bash 

    fly postgres attach <database-name>

3. Update Flask configuration:

..	code-block:: python

    # config.py
    import os

    class Config:
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    ```

    ## SSL Configuration

    SSL certificates are automatically managed by Fly.io. Configure your Flask application to handle HTTPS:

    ```python
    # app/__init__.py
    from flask_talisman import Talisman

    def create_app():
        app = Flask(__name__)
        if not app.debug:
            Talisman(app, force_https=True)
        return app

Monitoring and Logging
----------------------

1. View application logs:

..	code-block:: bash 

    fly logs

2. Monitor application metrics:

..	code-block:: bash 

    fly status
    fly monitor

Scaling Configuration
---------------------

1. Horizontal scaling:

..	code-block:: bash 

    fly scale count 2  # Scale to 2 instances

2. Vertical scaling:

..	code-block:: bash 
    
    fly scale vm shared-cpu-1x


Health Checks
-------------

Implement a health check endpoint:

..	code-block:: python

    @app.route('/health')
    def health_check():
        return jsonify({"status": "healthy"}), 200

Update `fly.toml` to include health check:

..	code-block:: toml

    [checks]
        [checks.health]
            port = 8080
            type = "http"
            interval = "15s"
            timeout = "2s"
            grace_period = "5s"
            method = "GET"
            path = "/health"

Performance Optimization
------------------------

1. Configure Gunicorn workers:

Update `gunicorn.conf.py` based on available resources:

..	code-block:: python 

    import multiprocessing

    workers = multiprocessing.cpu_count() * 2 + 1
    threads = 2
    worker_class = "gthread"
    worker_connections = 1000

2. Implement caching:

..	code-block:: python 

    from flask_caching import Cache

    cache = Cache(config={'CACHE_TYPE': 'simple'})

    @app.route('/cached-endpoint')
    @cache.cached(timeout=300)
    def cached_endpoint():
        return expensive_operation()

Common Issues and Solutions
---------------------------

1. **Database Connection Issues**
   - Verify DATABASE_URL in environment variables
   - Check database firewall rules
   - Validate connection pool settings

2. **Memory Issues**
   - Monitor memory usage with `fly monitor`
   - Adjust Gunicorn worker settings
   - Implement proper connection pooling

3. **Static Files**
   - Use WhiteNoise for static file serving
   - Configure proper caching headers
   - Consider using a CDN for large applications

This documentation provides a comprehensive guide for deploying Flask applications on Fly.io. 
Regular monitoring and maintenance of your deployed application is recommended for optimal performance.

.. include::  /_templates/components/footer-links.rst
