Pip
====

Pip is the standard package manager for Python. It's used to install and manage software packages written in Python that are available in the Python Package Index (PyPI) 
repository and other package indexes.

.. include::  /_templates/components/banner-top.rst

Key features of pip
-------------------

1. **Package Installation**: Install Python packages from PyPI or other sources.

2. **Dependency Management**: Automatically installs dependencies required by packages.

3. **Version Control**: Allows installing specific versions of packages.

4. **Requirements Files**: Supports installing multiple packages defined in a requirements.txt file.

5. **Package Uninstallation**: Removes installed packages and their dependencies.

6. **Package Listing**: Shows installed packages and their versions.

7. **Package Freezing**: Creates a list of installed packages with exact versions.

Common pip commands
-------------------

- `pip install package-name` - Install a package
- `pip install package-name==1.2.3` - Install a specific version
- `pip install -r requirements.txt` - Install from a requirements file
- `pip uninstall package-name` - Remove a package
- `pip list` - Show installed packages
- `pip freeze > requirements.txt` - Export installed packages to a file
- `pip show package-name` - Display information about an installed package
- `pip install --upgrade package-name` - Upgrade a package

Pip comes pre-installed with Python installations from Python 3.4+ and Python 2.7.9+. It's the most widely used tool for installing Python packages, 
though alternatives like Poetry, Pipenv, and conda are also popular for more advanced dependency management.

.. include::  /_templates/components/footer-links.rst
