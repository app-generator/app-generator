:og:description: Bash in Docker Scripts - Learn the basics of using Bash in Docker

Bash in Docker Scripts
======================

.. title:: Bash in Docker Scripts - Learn the basics of using Bash in Docker    
.. meta::
    :description: Bash in Docker Scripts - Learn the basics of using Bash in Docker
    :keywords: bash, docker, docker and bash, bash and docker 

`Bash <./index.html>`__ is commonly used in Docker scripts, particularly in Dockerfiles and as entrypoint scripts. Here's a comprehensive example that demonstrates using Bash in a Docker context.

.. include::  /_templates/components/banner-top.rst
    
This example demonstrates several important concepts: 

- Using Bash in a Dockerfile to set up the environment and install dependencies.
- Creating a flexible entrypoint script that can handle various scenarios.
- Using environment variables to configure the application.
- Implementing a wait mechanism for dependent services (like databases).
- Providing different execution modes (init, migrate, test) through the entrypoint script.
- Basic security practices like not printing sensitive environment variables.

The entrypoint script provides a lot of flexibility

- It can wait for other services to be ready before starting the main application.
- It allows running different commands (init, migrate, test) without modifying the Dockerfile.
- It performs environment checks and setup before running the main application.

When using this setup, you can easily extend the entrypoint script to handle more complex scenarios, such as

- Fetching configuration from a remote source
- Setting up SSL certificates
- Adjusting application configuration based on the environment
- Implementing health checks

Let's move forward and see how the above concepts are implemented in Docker & Bash  

Dockerfile with Bash commands
-----------------------------

.. code-block:: Dockerfile 

    # Use Ubuntu as the base image
    FROM ubuntu:20.04

    # Set environment variables
    ENV DEBIAN_FRONTEND=noninteractive
    ENV APP_HOME=/app

    # Install necessary packages
    RUN apt-get update && apt-get install -y \
        python3 \
        python3-pip \
        curl \
        && rm -rf /var/lib/apt/lists/*

    # Set working directory
    WORKDIR $APP_HOME

    # Copy application files
    COPY . .

    # Install Python dependencies
    RUN pip3 install --no-cache-dir -r requirements.txt

    # Copy the entrypoint script
    COPY docker-entrypoint.sh /usr/local/bin/
    RUN chmod +x /usr/local/bin/docker-entrypoint.sh

    # Set the entrypoint
    ENTRYPOINT ["docker-entrypoint.sh"]

    # Default command
    CMD ["python3", "app.py"]    

Entrypoint script (docker-entrypoint.sh)
----------------------------------------

.. code-block:: bash

    #!/bin/bash
    set -e

    # Function to check if a port is open
    wait_for_port() {
        local host="$1" port="$2"
        local max_tries=30 tries=0

        while ! nc -z "$host" "$port"; do
            tries=$((tries + 1))
            if [ $tries -ge $max_tries ]; then
                echo "Error: Timed out waiting for $host:$port to become available"
                exit 1
            fi
            echo "Waiting for $host:$port... ($tries/$max_tries)"
            sleep 1
        done
        echo "$host:$port is available"
    }

    # Check if we're running the init command
    if [ "${1}" = "init" ]; then
        echo "Initializing application..."
        python3 init_db.py
        echo "Initialization complete."
        exit 0
    fi

    # Wait for database to be ready
    if [ -n "$DB_HOST" ] && [ -n "$DB_PORT" ]; then
        wait_for_port "$DB_HOST" "$DB_PORT"
    fi

    # Perform database migrations if needed
    if [ "${1}" = "migrate" ]; then
        echo "Running database migrations..."
        python3 manage.py db upgrade
        echo "Migrations complete."
        exit 0
    fi

    # Check if we need to run tests
    if [ "${1}" = "test" ]; then
        echo "Running tests..."
        python3 -m pytest tests/
        exit $?
    fi

    # Print environment variables (excluding secrets)
    echo "Environment variables:"
    env | grep -v -E "PASSWORD|SECRET|KEY"

    # Run the main command
    exec "$@"


Using the Docker image
----------------------

.. code-block:: bash

    # Build the Docker image
    docker build -t myapp:latest .

    # Run initialization
    docker run --rm myapp:latest init

    # Run database migrations
    docker run --rm myapp:latest migrate

    # Run tests
    docker run --rm myapp:latest test

    # Run the application
    docker run -d -p 8080:8080 \
        -e DB_HOST=db.example.com \
        -e DB_PORT=5432 \
        myapp:latest

This example provides a solid foundation for using Bash in Docker scripts, which you can adapt and expand based on your specific application requirements.

.. include::  /_templates/components/footer-links.rst
