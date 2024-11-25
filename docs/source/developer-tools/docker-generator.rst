Docker Generator
================

Docker Generator is a powerful tool that automates the creation of `Dockerfile` and `docker-compose.yml` files for web applications directly from GitHub repositories. Leveraging AI technology from **GROQ**, the tool analyzes your project and generates optimal Docker configurations with minimal manual effort.

Features
--------

**Automated Workflow**

- Clone GitHub repository.
- Analyze the project structure using AI.
- Detect application frameworks, ports, databases, and commands.
- Generate `Dockerfile` and `docker-compose.yml` tailored to the repository.

**Framework Detection**

Supports frameworks across:

- **JavaScript/Node.js**: React, Next.js, Vue.js
- **Python**: Flask, Django
- Detects unknown frameworks for manual input if necessary.

**Dynamic Configurations**

- **Port Detection**: Automatically detects exposed ports or applies default framework ports.
- **Database Detection**: Identifies database usage and includes it in `docker-compose.yml` if required.
- **Custom Commands**: Scans for commands to run the app or prompts the user for manual input when undetected.

**File Validation**

- Ensures the validity of generated files.
- Saves invalid files for debugging.

Configuration
-------------

**Environment Setup**

Set the `GROQ_API_KEY` environment variable. Obtain your API key from `GROQ Console <https://console.groq.com>`_.

Example::

   export GROQ_API_KEY=<your_groq_api_key>

Running Docker Generator
------------------------

Run the tool using the command::

   python manage.py tool_docker_generator -r <repo_url>

Replace `<repo_url>` with the URL of the repository you want to generate Docker configurations for.

Generated Files
---------------

The tool generates:
- `Dockerfile`
- `docker-compose.yml`

Both files are stored in a timestamped directory for easy tracking::

   cloned_repository/<repo_name>-<timestamp>/

Tested Repositories
-------------------

**JavaScript/Node.js**

- `deploypro-react <https://github.com/app-generator/deploypro-react>`_
- `deploypro-nextjs <https://github.com/app-generator/deploypro-nextjs>`_
- `deploypro-vue <https://github.com/app-generator/deploypro-vue>`_

**Python**

- `deploypro-flask <https://github.com/app-generator/deploypro-flask>`_
- `deploypro-django <https://github.com/app-generator/deploypro-django>`_

Result
------

After running the tool, you'll receive:

- A `Dockerfile` customized for your application framework.
- A `docker-compose.yml`:

  - Includes database service if detected or required.
  - Excludes database service if not needed.

Both files are validated and ready for deployment.
