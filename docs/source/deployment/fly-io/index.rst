Getting Started
===============

.. title:: Getting Started with Fly.io
.. meta::
    :description: Learn more about Fly.io - how to deploy projects and websites  
    :keywords: fly.io, fly.io cloud, fly.io deployment, fly.io cloud tools, deploy, ci-cd, deployment  

Fly.io is a deployment platform that enables application deployment across a global network of edge-servers. 
It utilizes container-based deployment strategies and provides automated load balancing, SSL management, and horizontal scaling capabilities.

.. include::  /_templates/components/banner-top.rst

Prerequisites
-------------

Required components:

- Terminal access
- Git
- Fly.io account
- Application codebase
- Docker installed locally (recommended)

CLI Installation
----------------

The Fly CLI is the primary interface for managing deployments and resources.

MacOS
*****

..	code-block:: bash

        brew install flyctl

Linux
*****

..	code-block:: bash

    curl -L https://fly.io/install.sh | sh

Windows
*******

..	code-block:: powershell

    powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"

Authentication
--------------

Initialize CLI authentication:

..	code-block:: bash
    
    fly auth login


This command initiates an OAuth flow in your default browser for account authentication.

Application Configuration
-------------------------

Python/Flask Configuration
**************************

Required files for Flask deployments:

..	code-block:: dockerfile
        
        FROM python:3.9-slim

        WORKDIR /app

        COPY requirements.txt .
        RUN pip install -r requirements.txt

        COPY . .

        ENV FLASK_APP=app.py
        ENV FLASK_ENV=production

        CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]

..	code-block:: text

        flask
        gunicorn


Node.js/NestJS Configuration
****************************

Required files for NestJS deployments:

..	code-block:: dockerfile

        FROM node:16-slim

        WORKDIR /app

        COPY package*.json ./
        RUN npm install

        COPY . .
        RUN npm run build

        CMD ["npm", "run", "start:prod"]


Deployment Process
------------------

Initialize deployment configuration:

..	code-block:: bash
    
    fly launch


This command executes the following operations:

1. Application name assignment
2. Framework/runtime detection
3. `fly.toml` configuration generation
4. Initial deployment setup

Deployment Configuration
------------------------

Standard `fly.toml` configuration file:

..	code-block:: toml

    app = "application-name"

    [build]
        builder = "paketobuildpacks/builder:base"

    [env]
        PORT = "8080"

    [http_service]
        internal_port = 8080
        force_https = true

    [[services.ports]]
        handlers = ["http"]
        port = 80

    [[services.ports]]
        handlers = ["tls", "http"]
        port = 443


Core CLI Commands
-----------------

Application Management:

..	code-block:: bash
    
    # Deploy application updates
    fly deploy

    # Monitor application status
    fly status

    # Access application logs
    fly logs

    # Launch application in browser
    fly open

    # Configure application scaling
    fly scale count 2  # Horizontal scaling to 2 instances


Best Practices
--------------

1. **Deployment Strategy**
   - Initialize with minimal configuration
   - Implement incremental feature additions
   - Validate each deployment phase

2. **Monitoring**
   - Implement comprehensive logging
   - Monitor resource utilization
   - Track performance metrics

3. **Security**
   - Utilize `fly secrets` for sensitive data
   - Implement proper access controls
   - Regular security audits

Troubleshooting Protocol
------------------------

When encountering deployment issues:

1. Execute log analysis:

..	code-block:: bash
    
    fly logs


2. Validate configuration integrity in `fly.toml`
3. Verify container functionality locally
4. Consult error-specific documentation

Advanced Configuration
----------------------

Post-deployment considerations:
- Domain configuration and DNS management
- SSL/TLS certificate implementation
- Database integration and management
- CI/CD pipeline integration
- Scaling and performance optimization

Resource Management
-------------------

Key considerations for resource allocation:
- CPU and memory allocation
- Network bandwidth utilization
- Storage requirements
- Cost optimization strategies

For detailed specifications and advanced configurations, refer to the official Fly.io documentation or contact technical support through their official channels.

.. include::  /_templates/components/footer-links.rst
