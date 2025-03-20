Poetry
======

WSGI (Web Server Gateway Interface) is a specification for a standardized interface between web servers and Python web applications or frameworks. 
It defines how a web server communicates with Python web applications and how these applications can be chained together to process a request.

.. include::  /_templates/components/banner-top.rst


Poetry is a package management and dependency resolution tool for Python. It's designed to help developers manage project dependencies, virtual environments, and packaging in a more robust and user-friendly way than traditional tools like pip and setup.py.

Key features of Poetry include:

1. **Dependency Management**: Poetry uses a single pyproject.toml file to declare dependencies with precise version constraints.

2. **Lockfile System**: Poetry generates a poetry.lock file that ensures reproducible installations across different environments.

3. **Virtual Environment Management**: Poetry automatically creates and manages virtual environments for your projects.

4. **Package Building and Publishing**: Poetry simplifies packaging Python projects and publishing them to PyPI.

5. **Dependency Resolution**: Poetry has a sophisticated dependency resolver that handles complex dependency trees and conflicts.

6. **Script Running**: Poetry allows you to define and run project-specific scripts.

7. **Project Scaffolding**: Poetry can initialize new projects with a standard structure.

Basic commands
--------------

- `poetry new project-name` - Create a new project
- `poetry add package-name` - Add a dependency
- `poetry install` - Install dependencies
- `poetry update` - Update dependencies
- `poetry run python script.py` - Run a script in the project's virtual environment
- `poetry build` - Build your package
- `poetry publish` - Publish your package to PyPI

Poetry has gained significant popularity in the Python community as an alternative to traditional tooling because it provides a more consistent and reliable development workflow, 
particularly for larger projects with complex dependency requirements.

.. include::  /_templates/components/footer-links.rst
