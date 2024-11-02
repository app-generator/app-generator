Docker Generator
==============================

Docker Generator is a tool that simplifies the process for developers to create Dockerfile and docker-compose.yml files from GitHub repositories. This tool leverages AI technology from GROQ to analyze the code, resulting in a suitable and optimal Docker configuration with minimal effort.

Configuration
-------------
To configure your environment for the Docker Generator, Set Environment Variables:

   Add the `GROQ_API_KEY` variable to your environment. You can obtain this key from the `GROQ <https://console.groq.com>`__.

Running the Docker Generator
----------------------------
You can run the Docker Generator from the terminal or command line interface (CLI) using the following command:

.. code-block:: shell

   python manage.py tool_docker_generator -r <repo_url>

Replace `<repo_url>` with the URL of the repository you wish to generate the Docker configuration for.

Result
------
After running the command, the tool will generate the following files:

- `Dockerfile.generate`
- `docker-compose.generate.yml`

These files will be created in the designated location according to your project setup.
