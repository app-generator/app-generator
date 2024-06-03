# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'appseed-docs'
copyright = '2024, appseed'
author = 'appseed'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    'sphinx.ext.viewcode',
    # 'myst_parser',
    # 'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_book_theme'


html_static_path = ['_static']

html_logo = '_static/logo-text.png'


html_theme_options = {
    "light_logo": "logo-text.png",
    "dark_logo": "logo-text.png",
    # "sidebar_hide_name": True,
    # "navigation_with_keys": True,
    # "top_of_page_buttons": ["view", "edit"],
    # "announcement": "We will launch the stable version on July 1st, 2024. We are seeking your feedback",
    # "source_repository": "https://github.com/nxtbn-com/nxtbn-docs",
    # "source_branch": "main",
    # "source_directory": "source",
}