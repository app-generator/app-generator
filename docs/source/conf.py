# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# project = 'appseed-docs'
# copyright = '2024, appseed'
# author = 'appseed'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    'sphinx.ext.viewcode',
    'sphinx_copybutton',
    'sphinxcontrib.googleanalytics',
    'sphinx_sitemap',
    'sphinxcontrib.youtube',
    "sphinxext.opengraph",
]

html_title = 'Documentation'

sitemap_locales = [None]
html_baseurl = 'https://app-generator.dev/docs/'

googleanalytics_id = 'G-H6RJ2DSXP4' 

templates_path = ['_templates']
exclude_patterns = []

html_css_files = [
    'custom.css',
    'overlay.css',
]

html_extra_path = [
    'robots.txt','favicon.ico',
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_book_theme'

html_static_path = ['_static']

html_logo = '_static/logo.png'

html_theme_options = {
    "use_download_button": False,
    "repository_url": "https://github.com/app-generator/app-generator",
    "use_source_button": True,
    "repository_branch": "main",
    "path_to_docs": "docs/source",
    "use_edit_page_button": True,
    "use_repository_button": True,
    "use_issues_button": True,
}

html_sidebars = {
    "**": [
        "custom-navbar-logo.html",
        "sbt-sidebar-nav.html",
        # "search-field.html"
    ]
}

html_js_files = [
    'overlay.js',
]

ogp_site_url = "https://app-generator.dev/"
ogp_image = "https://app-generator.dev/static/common/favicon-196x196.png"
ogp_type = "article"
ogp_site_name = "App-generator.dev - Open-Source Generators and Dev Tools Suite"
