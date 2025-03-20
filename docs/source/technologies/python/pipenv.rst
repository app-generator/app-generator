Pipenv
=======

Pipenv is a Python dependency management tool that combines pip (package installation) and virtualenv (environment management) into a single, streamlined interface. 
Created by Kenneth Reitz, it aims to bring the best of all packaging worlds to the Python ecosystem.

.. include::  /_templates/components/banner-top.rst

Key features of Pipenv
----------------------

1. **Simplified Workflow**: Combines virtual environment creation, package installation, and dependency tracking in one tool.

2. **Pipfile and Pipfile.lock**: Uses these files instead of requirements.txt to track dependencies. Pipfile is for declaring dependencies, while Pipfile.lock ensures deterministic builds by locking exact versions.

3. **Automatic Virtual Environment Management**: Creates and manages virtual environments automatically, typically in a centralized location.

4. **Dependency Resolution**: Automatically resolves dependencies between packages to prevent conflicts.

5. **Development vs. Production Dependencies**: Distinguishes between packages needed for development and those required in production.

6. **Security Features**: Can scan your dependency graph for known security vulnerabilities.


Common Pipenv commands
----------------------

- `pipenv install` - Create a virtual environment and install dependencies
- `pipenv install package_name` - Install a package
- `pipenv install --dev package_name` - Install a development dependency
- `pipenv shell` - Activate the virtual environment
- `pipenv run python script.py` - Run a command in the virtual environment
- `pipenv lock` - Generate Pipfile.lock
- `pipenv graph` - Show a dependency graph
- `pipenv check` - Check for security vulnerabilities

Example Pipfile:

.. code-block:: ini

    [[source]]
    url = "https://pypi.org/simple"
    verify_ssl = true
    name = "pypi"

    [packages]
    requests = "*"
    django = ">=3.2"

    [dev-packages]
    pytest = "*"
    black = "*"

    [requires]
    python_version = "3.9"

Pipenv sits somewhere between basic pip/virtualenv usage and more comprehensive tools like Poetry, offering a balance of simplicity and powerful dependency management.

.. include::  /_templates/components/footer-links.rst
