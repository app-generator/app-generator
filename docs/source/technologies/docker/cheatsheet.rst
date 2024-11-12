:og:description: Docker Cheatsheet - The basics of Docker and Docker Compose

Cheatsheet
==========

.. title:: Docker Cheatsheet - The basics of Docker and Docker Compose
.. meta::
    :description: Learn how to use Docker and control containers lifecycle, manipulate volumes and services 

`Docker <./index.html>`__ is a platform for developing, shipping, and running applications in containers. 
Created in 2013, **Docker** has revolutionized application deployment by enabling developers to package applications with all their dependencies into standardized units (containers) for software development. 
Containers are lightweight, portable, and ensure consistent behavior across different environments.

.. include::  /_templates/components/banner-top.rst

**Container Lifecycle Management**

.. code-block:: bash    

    # Start a container
    docker run -d --name myapp nginx:latest
    docker run -it ubuntu bash  # Interactive mode

    # Container operations
    docker start myapp
    docker stop myapp
    docker restart myapp
    docker pause myapp
    docker unpause myapp

    # Remove containers
    docker rm myapp  # Remove stopped container
    docker rm -f myapp  # Force remove running container
    docker container prune  # Remove all stopped containers

    # View containers
    docker ps  # List running containers
    docker ps -a  # List all containers
    docker stats  # Container resource usage


**Image Management**

.. code-block:: bash    

    # Image operations
    docker pull nginx:latest
    docker push myregistry/myapp:v1
    docker images  # List all images
    docker rmi nginx:latest  # Remove image
    docker image prune  # Remove unused images
    docker image prune -a  # Remove all unused images

    # Build image from Dockerfile
    docker build -t myapp:v1 .
    docker build --no-cache -t myapp:v1 .

    # Save and load images
    docker save myapp:v1 > myapp.tar
    docker load < myapp.tar

    # Tag images
    docker tag myapp:v1 myregistry/myapp:latest


**Network Management**

.. code-block:: bash    

    # Network operations
    docker network create mynetwork
    docker network ls
    docker network rm mynetwork

    # Connect containers to network
    docker run --network mynetwork myapp
    docker network connect mynetwork myapp
    docker network disconnect mynetwork myapp

    # Network drivers
    docker network create --driver bridge mybridge
    docker network create --driver overlay myoverlay
    docker network create --driver host myhost

    # Network inspection
    docker network inspect mynetwork


**Volume Management**

.. code-block:: bash    

    # Volume operations
    docker volume create myvolume
    docker volume ls
    docker volume rm myvolume
    docker volume prune

    # Mount volume in container
    docker run -v myvolume:/app/data myapp
    docker run --mount source=myvolume,target=/app/data myapp

    # Bind mounts
    docker run -v $(pwd):/app myapp
    docker run --mount type=bind,source=$(pwd),target=/app myapp

    # Temporary mounts
    docker run --tmpfs /app/temp myapp


**Container Resource Management**

.. code-block:: bash    

    # Memory limits
    docker run --memory="512m" myapp
    docker run --memory-swap="1g" myapp

    # CPU limits
    docker run --cpus=".5" myapp  # Use half CPU
    docker run --cpu-shares=512 myapp

    # Resource constraints
    docker run --pids-limit=100 myapp
    docker run --device-read-bps=/dev/sda:1mb myapp

    # Update running container
    docker update --cpus=".75" myapp
    docker update --memory="1g" myapp


**Docker Compose**

.. code-block:: bash    

    # docker-compose.yml
    version: '3.8'
    services:
    webapp:
        build: .
        ports:
        - "3000:3000"
        environment:
        - NODE_ENV=production
        volumes:
        - ./data:/app/data
        depends_on:
        - db
    
    db:
        image: postgres:13
        environment:
        - POSTGRES_PASSWORD=secret
        volumes:
        - db-data:/var/lib/postgresql/data

    volumes:
    db-data:

    # Commands
    docker-compose up -d
    docker-compose down
    docker-compose logs -f
    docker-compose ps
    docker-compose exec webapp bash


**Logging and Debugging**

.. code-block:: bash    

    # View logs
    docker logs myapp
    docker logs -f myapp  # Follow logs
    docker logs --tail 100 myapp
    docker logs --since 1h myapp

    # Debug containers
    docker exec -it myapp bash
    docker exec myapp ps aux
    docker top myapp
    docker inspect myapp

    # Copy files
    docker cp myapp:/app/log.txt ./log.txt
    docker cp ./config.json myapp:/app/


**Security Best Practices**

.. code-block:: bash    

    # Run as non-root user
    docker run --user 1000:1000 myapp

    # Read-only root filesystem
    docker run --read-only myapp

    # Security options
    docker run --security-opt no-new-privileges myapp
    docker run --cap-drop ALL --cap-add NET_BIND_SERVICE myapp

    # Scan images
    docker scan myapp:latest


**Multi-stage Builds**

.. code-block:: dockerfile    

    # Build stage
    FROM node:16 AS builder
    WORKDIR /app
    COPY package*.json ./
    RUN npm install
    COPY . .
    RUN npm run build

    # Production stage
    FROM node:16-slim
    WORKDIR /app
    COPY --from=builder /app/dist ./dist
    COPY package*.json ./
    RUN npm install --production
    CMD ["npm", "start"]


**Health Checks and Auto-healing**

.. code-block:: dockerfile    

    # Dockerfile health check
    HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost/ || exit 1

    # Docker run health check
    docker run --health-cmd="curl -f localhost:3000 || exit 1" \
            --health-interval=30s \
            --health-retries=3 \
            --health-timeout=3s \
            myapp

    # Check container health
    docker inspect --format='{{.State.Health.Status}}' myapp


**Pro Tips**

- Use .dockerignore to exclude unnecessary files
- Always specify image versions, avoid 'latest' tag
- Use multi-stage builds to reduce final image size
- Implement proper logging strategies
- Use docker-compose for development environments
- Regularly update base images for security
- Cache build dependencies efficiently
- Use environment variables for configuration
- Implement proper backup strategies for volumes
- Monitor container resource usage
- Use container orchestration for production (Kubernetes/Swarm)
- Keep images minimal - only include what's necessary

.. include::  /_templates/components/footer-links.rst
