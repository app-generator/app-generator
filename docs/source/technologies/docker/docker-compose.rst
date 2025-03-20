Docker-Compose
==============

Docker Compose is a tool for defining and running multi-container Docker applications. 
It uses a YAML file to configure application services, networks, and volumes, allowing you to manage complex application stacks with a single command.

.. include::  /_templates/components/banner-top.rst

Key features
------------

1. **Declarative Configuration**: Define your entire application stack in a docker-compose.yml file.

2. **Service Orchestration**: Run multiple containers as a cohesive application.

3. **Environment Management**: Define environment variables for different deployment scenarios.

4. **Network Management**: Automatically create networks between containers.

5. **Volume Management**: Define persistent data storage.

6. **Service Dependencies**: Specify the order in which services start.

A simple docker-compose.yml example:

.. code-block:: yaml

    version: '3'
    services:
    web:
        build: ./web
        ports:
        - "8000:8000"
        depends_on:
        - db
        environment:
        - DATABASE_URL=postgres://postgres:postgres@db:5432/app
    
    db:
        image: postgres:13
        volumes:
        - postgres_data:/var/lib/postgresql/data
        environment:
        - POSTGRES_PASSWORD=postgres
        - POSTGRES_USER=postgres
        - POSTGRES_DB=app

    volumes:
        postgres_data:

Common Docker Compose commands
------------------------------

- `docker-compose up` - Create and start containers
- `docker-compose down` - Stop and remove containers
- `docker-compose build` - Build or rebuild services
- `docker-compose logs` - View output from containers
- `docker-compose ps` - List running containers
- `docker-compose exec service_name command` - Run a command in a service

Docker Compose is particularly useful for development, testing, and staging environments, though it can also be used in production for simpler deployments. 
For more complex production deployments, tools like Kubernetes or Docker Swarm might be preferred.

.. include::  /_templates/components/footer-links.rst
