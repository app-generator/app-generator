Cheatsheet
==========

`Flask <./index.html>`__ is a lightweight WSGI web application framework written in Python. Created by Armin Ronacher in 2010, **Flask** is considered a microframework because it doesn't require particular tools or libraries. 
It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

.. include::  /_templates/components/banner-top.rst

**Basic Application Setup and Routing**

.. code-block:: python    

    from flask import Flask, request, jsonify, render_template
    from werkzeug.middleware.proxy_fix import ProxyFix

    # Basic app setup
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    # Configuration
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['DEBUG'] = True

    # Basic routes
    @app.route('/')
    def home():
        return 'Hello, World!'

    # Multiple HTTP methods
    @app.route('/api/resource', methods=['GET', 'POST'])
    def handle_resource():
        if request.method == 'POST':
            return jsonify({"message": "Created"}), 201
        return jsonify({"message": "Retrieved"})

    # URL variables
    @app.route('/user/<username>')
    def show_user(username):
        return f'User: {username}'

    # URL variables with converters
    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        return f'Post: {post_id}'

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
    

**Request Handling and Response**

.. code-block:: python    

    from flask import request, jsonify, make_response, abort

    @app.route('/api/data', methods=['POST'])
    def handle_data():
        # Access JSON data
        data = request.get_json()
        
        # Access form data
        form_data = request.form.get('field_name')
        
        # Access URL parameters
        param = request.args.get('param')
        
        # Access headers
        header_value = request.headers.get('X-Custom-Header')
        
        # Custom response
        response = make_response(jsonify({'message': 'Success'}))
        response.headers['X-Custom-Header'] = 'Value'
        response.status_code = 200
        return response

    # Error handling
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'error': 'Resource not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500

    # Abort example
    @app.route('/resource/<id>')
    def get_resource(id):
        if not valid_resource(id):
            abort(404)
        return jsonify({'id': id})
    

**Templates and Static Files**

.. code-block:: python    

    from flask import render_template, send_file, url_for

    # Basic template rendering
    @app.route('/template')
    def show_template():
        return render_template('index.html',
                            title='Home',
                            user={'name': 'John'})

    # Template with loops and conditions
    @app.route('/items')
    def show_items():
        items = ['item1', 'item2', 'item3']
        return render_template('items.html',
                            items=items,
                            show_items=True)

    # Static files
    @app.route('/static-file')
    def serve_static():
        return send_file('static/file.pdf')

    # Template inheritance example
    """
    # base.html
    <!DOCTYPE html>
    <html>
        <head>
            <title>{% block title %}{% endblock %}</title>
        </head>
        <body>
            {% block content %}{% endblock %}
        </body>
    </html>

    # child.html
    {% extends "base.html" %}
    {% block title %}Page Title{% endblock %}
    {% block content %}
        <h1>Content goes here</h1>
    {% endblock %}
    """
    

**Database Integration (SQLAlchemy)**

.. code-block:: python    

    from flask_sqlalchemy import SQLAlchemy

    # Database setup
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    # Models
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        posts = db.relationship('Post', backref='author', lazy=True)

    class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(120), nullable=False)
        content = db.Column(db.Text, nullable=False)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Database operations
    @app.route('/create_user', methods=['POST'])
    def create_user():
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created'})

    # Query examples
    @app.route('/users')
    def get_users():
        users = User.query.all()
        return jsonify([{
            'id': user.id,
            'username': user.username
        } for user in users])
    

**Authentication and Sessions**

.. code-block:: python    

    from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
    from werkzeug.security import generate_password_hash, check_password_hash
    from flask import session

    # Login manager setup
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    class User(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True)
        password_hash = db.Column(db.String(120))

        def set_password(self, password):
            self.password_hash = generate_password_hash(password)

        def check_password(self, password):
            return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Login route
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            login_user(user)
            return jsonify({'message': 'Logged in successfully'})
        return jsonify({'message': 'Invalid credentials'}), 401

    # Protected route
    @app.route('/protected')
    @login_required
    def protected_route():
        return jsonify({'message': f'Hello {current_user.username}'})

    # Session handling
    @app.route('/set_session')
    def set_session():
        session['key'] = 'value'
        return 'Session set'

    @app.route('/get_session')
    def get_session():
        return session.get('key', 'not set')
    

**Forms and Validation**

.. code-block:: python    

    from flask_wtf import FlaskForm
    from wtforms import StringField, PasswordField, SubmitField
    from wtforms.validators import DataRequired, Email, Length

    # Form class
    class RegistrationForm(FlaskForm):
        username = StringField('Username', 
                            validators=[DataRequired(), Length(min=4, max=20)])
        email = StringField('Email', 
                        validators=[DataRequired(), Email()])
        password = PasswordField('Password', 
                            validators=[DataRequired(), Length(min=6)])
        submit = SubmitField('Register')

    # Form handling
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(
                username=form.username.data,
                email=form.email.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        return render_template('register.html', form=form)
    

**Blueprints and Application Factory**

.. code-block:: python    

    # auth/routes.py
    from flask import Blueprint

    auth = Blueprint('auth', __name__)

    @auth.route('/login')
    def login():
        return 'Login'

    # admin/routes.py
    admin = Blueprint('admin', __name__, url_prefix='/admin')

    @admin.route('/')
    def admin_index():
        return 'Admin Index'

    # Application factory
    def create_app(config_object=None):
        app = Flask(__name__)
        
        if config_object:
            app.config.from_object(config_object)
        
        # Initialize extensions
        db.init_app(app)
        login_manager.init_app(app)
        
        # Register blueprints
        app.register_blueprint(auth)
        app.register_blueprint(admin)
        
        return app
    

**API Development and RESTful Resources**

.. code-block:: python    

    from flask_restful import Api, Resource, reqparse

    api = Api(app)

    # Request parser
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True)
    parser.add_argument('age', type=int)

    # Resource class
    class UserResource(Resource):
        def get(self, user_id):
            user = User.query.get_or_404(user_id)
            return {'name': user.name, 'age': user.age}
        
        def put(self, user_id):
            args = parser.parse_args()
            user = User.query.get_or_404(user_id)
            user.name = args['name']
            user.age = args['age']
            db.session.commit()
            return {'message': 'User updated'}
        
        def delete(self, user_id):
            user = User.query.get_or_404(user_id)
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted'}

    # Add resource to API
    api.add_resource(UserResource, '/api/user/<int:user_id>')
    

**Testing**

.. code-block:: python    

    import unittest
    from app import create_app, db

    class TestConfig:
        TESTING = True
        SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.app = create_app(TestConfig)
            self.client = self.app.test_client()
            self.ctx = self.app.app_context()
            self.ctx.push()
            db.create_all()

        def tearDown(self):
            db.session.remove()
            db.drop_all()
            self.ctx.pop()

        def test_home_page(self):
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)

        def test_create_user(self):
            response = self.client.post('/api/users', 
                                    json={'username': 'test',
                                        'email': 'test@test.com'})
            self.assertEqual(response.status_code, 201)
    

**Deployment and Configuration**

.. code-block:: python    

    # config.py
    class Config:
        SECRET_KEY = 'dev'
        SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
        MAIL_SERVER = 'smtp.googlemail.com'
        MAIL_PORT = 587
        MAIL_USE_TLS = True
        MAIL_USERNAME = 'your-email@gmail.com'
        MAIL_PASSWORD = 'your-password'

    class ProductionConfig(Config):
        DEBUG = False
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    class DevelopmentConfig(Config):
        DEBUG = True

    class TestingConfig(Config):
        TESTING = True
        SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    # WSGI file (wsgi.py)
    from app import create_app

    app = create_app(ProductionConfig)

    if __name__ == '__main__':
        app.run()

    # Gunicorn configuration
    """
    # gunicorn.conf.py
    workers = 4
    bind = '0.0.0.0:8000'
    worker_class = 'gevent'
    timeout = 120
    """
    

**Pro Tips**

- Use application factory pattern for larger applications
- Implement proper error handling and logging
- Use environment variables for sensitive configuration
- Implement proper password hashing
- Use Flask-Migrate for database migrations
- Implement proper CSRF protection
- Use blueprints to organize code
- Implement proper caching strategy
- Use Flask-Admin for quick admin interfaces
- Write comprehensive tests
- Use Flask-Caching for performance optimization
- Implement proper security headers 

.. include::  /_templates/components/footer-links.rst
