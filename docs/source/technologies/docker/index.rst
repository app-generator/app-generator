:og:description: Getting Started with Docker - Learn the basics and beyond

Getting Started
===============

.. title:: Getting Started with Docker - Learn the basics and beyond
.. meta::
    :description: Learn how to install it, start your first container, list images and manage services with ease 

Docker can be installed on various operating systems including Linux, macOS, and Windows. Follow the instructions on the official Docker installation page for your specific OS.

.. include::  /_templates/components/banner-top.rst
    
**Verify Installation**

To verify Docker is installed correctly, open a terminal (or command prompt) and run:

.. code-block:: bash

    docker --version

**Running Your First Container**

Run a simple container using the hello-world image:

.. code-block:: bash

    docker run hello-world

This command downloads the hello-world image from Docker Hub (if not already present) and runs it in a container.

**Working with Docker Images**

- Pull an Image:

.. code-block:: bash

    docker pull ubuntu

- List Images:

.. code-block:: bash

    docker images

**Creating a Dockerfile**

Create a simple Dockerfile to define a custom image:

.. code-block:: dockerfile

    # Use an official Node.js runtime as a parent image
    FROM node:14

    # Set the working directory in the container
    WORKDIR /usr/src/app

    # Copy the current directory contents into the container at /usr/src/app
    COPY . .

    # Install the application dependencies
    RUN npm install

    # Make port 8080 available to the world outside this container
    EXPOSE 8080

    # Define the command to run the application
    CMD ["node", "app.js"]


Save this file as `Dockerfile` in your project directory.

**Building and Running a Docker Image**

- Build the Image

.. code-block:: bash

    docker build -t my-node-app .

- Run a Container

.. code-block:: bash

    docker run -p 8080:8080 my-node-app

This command maps port 8080 on the host to port 8080 on the container.

**Managing Containers** 

- List Running Containers

.. code-block:: bash

    docker ps

- Stop a Container

.. code-block:: bash

    docker stop <container_id>

- Remove a Container

.. code-block:: bash

    docker rm <container_id>

**Using Docker Compose**

Docker Compose is a tool for defining and running multi-container Docker applications. Use a `docker-compose.yml` file to configure your application’s services.

Example `docker-compose.yml`:

.. code-block:: yaml

    version: '3'
    services:
    web:
        build: .
        ports:
        - "8080:8080"
    redis:
        image: "redis:alpine"


**Benefits of Using Docker**

- `Consistency` and Reproducibility: Containers ensure applications run the same in development, testing, and production.
- `Isolation`: Containers isolate applications from each other and the host system.
- `Efficiency`: Containers are lightweight and use system resources more efficiently than VMs.
- `Portability`: Docker containers can run on any system that supports Docker, making deployment straightforward.
- `Scalability`: Docker can easily scale applications horizontally by adding more containers.

**Conclusion**

Docker revolutionizes how applications are developed, deployed, and managed by providing a consistent environment across various stages of the development lifecycle. 
By encapsulating applications and their dependencies in containers, Docker ensures reliability, portability, and efficiency, making it an essential tool in modern software development and DevOps practices.

.. include::  /_templates/components/footer-links.rst
