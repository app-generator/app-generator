Getting Started
=====================

`Flask <https://flask.palletsprojects.com/>`__ is a Python-based web framework that emphasizes flexibility and minimalism. 
It provides essential components for web development while allowing developers to choose and integrate additional tools and libraries as needed, making it suitable for both small projects and large applications. 
This approach makes Flask an excellent choice for developers who prefer fine-grained control over their application's architecture and dependencies.

.. include::  /_templates/components/signin-invite.rst
    
Getting Started with **Flask**, the basic steps. 

**Environment Setup: Install Flask using pip:**

.. code-block:: bash

        pip install Flask

**Basic Application Structure** - Forthis we create a file named `app.py`

.. code-block:: python 

    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    if __name__ == '__main__':
        app.run(debug=True)

**Running the Application**

.. code-block:: bash

    python app.py

**Routing**: Add more routes to your application:

.. code-block:: python

    @app.route('/about')
    def about():
        return 'About Page'

    @app.route('/user/<username>')
    def show_user_profile(username):
        return f'User {username}'

**HTTP Methods**: Specify HTTP methods for routes        

.. code-block:: python

    from flask import request

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            return 'Logging in...'
        else:
            return 'Login page'

**Templates**: Create a templates folder and add an HTML file, e.g., index.html:            

.. code-block:: html

    <!DOCTYPE html>
    <html>
    <body>
        <h1>{{ message }}</h1>
    </body>
    </html>

**Render the template** 

.. code-block:: python

    from flask import render_template

    @app.route('/template')
    def template_example():
        return render_template('index.html', message='Hello from template!')

**Static Files**: Create a static folder for CSS, JavaScript, and images. Reference in HTML:        

.. code-block:: html

    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">

**Request Data**: Access form data or URL parameters

.. code-block:: python

    @app.route('/submit', methods=['POST'])
    def submit():
        data = request.form['input_name']
        return f'Received: {data}'

**Redirects and Errors** 

.. code-block:: python

    from flask import redirect, url_for, abort

    @app.route('/redirect')
    def redirect_example():
        return redirect(url_for('hello_world'))

    @app.route('/error')
    def error_example():
        abort(404)

    @app.errorhandler(404)
    def page_not_found(error):
        return 'Page not found', 404

**Sessions**

.. code-block:: python

    from flask import session

    app.secret_key = 'your_secret_key'

    @app.route('/session')
    def session_example():
        if 'visits' in session:
            session['visits'] = session.get('visits') + 1
        else:
            session['visits'] = 1
        return f'Visits: {session.get("visits")}'

**Database Integration (example with SQLite)**

.. code-block:: python

    import sqlite3
    from flask import g

    DATABASE = 'database.db'

    def get_db():
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(DATABASE)
        return db

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    @app.route('/db')
    def db_example():
        cur = get_db().cursor()
        cur.execute("SELECT * FROM users")
        results = cur.fetchall()
        return str(results)

**Configuration**

.. code-block:: python

    app.config['DEBUG'] = True
    app.config['DATABASE_URI'] = 'sqlite:///example.db'

**Extensions:** Install and use Flask extensions for additional functionality, e.g., `Flask-SQLAlchemy` for ORM:    

.. code-block:: bash

    pip install Flask-SQLAlchemy

And the updated code that uses the `Flask-SQLAlchemy` library. 

.. code-block:: python

    from flask_sqlalchemy import SQLAlchemy

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
    db = SQLAlchemy(app)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)

This guide covers the fundamental aspects of Flask. 
As you progress, explore more advanced topics like blueprints for larger applications, Flask-RESTful for API development, and Flask-WTF for form handling.

******************************
Resources
******************************

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
