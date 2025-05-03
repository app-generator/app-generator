Jinja Templates
===============

.. title:: Jinja Templates - Learn how to use the Jinja2 templating engine with Flask
.. meta::
    :description: Jinja Templates - Learn how to use the Jinja2 templating engine with Flask
    :keywords: jinja templates, flask templates, jinja2, flask jinja2

Jinja is a fast, expressive, and extensible templating engine for Python. It's most commonly associated with Flask, but it's also used in many other Python frameworks and applications.

Here's what makes Jinja powerful:

- **Template inheritance**: Create base templates and extend them with specific content
- **Control structures**: Use if/else conditions, for loops, and macros in your templates
- **Filters**: Transform values directly in templates using built-in or custom filters
- **Automatic escaping**: Helps prevent XSS vulnerabilities by escaping HTML

A simple example of a Jinja template:

.. code-block:: jinja

    <!DOCTYPE html>
    <html>
    <head>
        <title>{{ page_title }}</title>
    </head>
    <body>
        <h1>Hello, {{ name }}!</h1>
        
        {% if items %}
            <ul>
            {% for item in items %}
                <li>{{ item }}</li>
            {% endfor %}
            </ul>
        {% else %}
            <p>No items found.</p>
        {% endif %}
    </body>
    </html>


When used with Flask, you'd render this template with something like:

.. code-block:: python

    @app.route('/')
    def index():
        return render_template('index.html', 
                            page_title='My App', 
                            name='User', 
                            items=['Item 1', 'Item 2', 'Item 3'])

.. include::  /_templates/components/footer-links.rst
