# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import django


project = 'Appseed'
copyright = '2024, Appseed'
author = 'Appseed'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    # Other extensions...
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']



# Include the Django project directory in the Python path
sys.path.insert(0, os.path.abspath('../../'))

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

# Setup Django
django.setup()


# conf.py


def generate_toctree():
    toctree = ".. toctree::\n"
    toctree += "   :maxdepth: 2\n"
    toctree += "   :caption: Contents:\n\n"

    for root, dirs, files in os.walk(".", topdown=True):
        for name in sorted(files):
            if name.endswith(".md"):
                path = os.path.relpath(os.path.join(root, name), ".")
                toctree += f"   {os.path.splitext(path)[0]}\n"

    return toctree

# Add the dynamically generated TOC to the master_doc
master_doc = "index"
toctree = generate_toctree()
