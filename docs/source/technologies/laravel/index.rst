Getting Started
=====================

Getting started with Laravel, a popular PHP framework for web application development, involves a series of steps to set up your environment, install Laravel, and create a basic project.
Here’s a step-by-step guide to help you begin

**Step 1: Prerequisites**

Before you can install Laravel, ensure you have the following installed on your system:

- PHP: Laravel requires PHP 7.3 or higher.
- Composer: Composer is a dependency manager for PHP that you’ll use to install Laravel.

**Step 2: Install Composer**

If you don't have Composer installed, you can download and install it from getcomposer.org. Follow the installation instructions specific to your operating system.

**Step 3: Install Laravel**

Once Composer is installed, you can install Laravel globally by running the following command in your terminal or command prompt:

.. code-block:: bash 

    composer global require laravel/installer

Make sure to place Composer’s system-wide vendor bin directory in your PATH so the laravel executable can be located by your system. This directory exists in different locations based on your operating system:

- macOS/Linux: `$HOME/.composer/vendor/bin``
- Windows: `%USERPROFILE%\AppData\Roaming\Composer\vendor\bin`


**Step 4: Create a New Laravel Project**

With Laravel installed, you can create a new Laravel project by running:

.. code-block:: bash 

    laravel new my-project

Alternatively, if you prefer not to install Laravel globally, you can use Composer to create a new project:

.. code-block:: bash 

    composer create-project --prefer-dist laravel/laravel my-project

Replace my-project with the desired name of your project directory.

**Step 5: Navigate to Your Project Directory**

Navigate to the newly created project directory:

.. code-block:: bash 

    cd my-project

**Step 6: Configure Your Environment**

Laravel uses an environment configuration file (.env) to manage settings specific to your development environment. 
The .env file is located in the root directory of your project. Make sure to set your database connection details here:

.. code-block:: text

    DB_CONNECTION=mysql
    DB_HOST=127.0.0.1
    DB_PORT=3306
    DB_DATABASE=your_database
    DB_USERNAME=your_username
    DB_PASSWORD=your_password

**Step 7: Run the Development Server**

Laravel includes a local development server. You can start it using Artisan, Laravel’s command-line interface:

.. code-block:: bash

    php artisan serve

By default, this command will start the server at `http://localhost:8000`.

**Step 8: Access Your Application**

Open your web browser and navigate to `http://localhost:8000`. You should see the Laravel welcome page, indicating that your setup is successful.

**Step 9: Create a Basic Route**

To create a basic route, open the routes/web.php file and add a new route:

.. code-block:: php 

    Route::get('/hello', function () {
        return 'Hello, World!';
    });

Now, when you navigate to http://localhost:8000/hello, you should see "Hello, World!" displayed.

**Learn and Explore** 

Laravel has extensive documentation and a vibrant community. Here are some resources to help you learn more:

- Official Documentation: `Laravel Documentation <https://laravel.com/docs>`__ 
- `Laracasts <https://laracasts.com/>`__ : Laracasts, a platform with video tutorials on Laravel and other web development topics.
- `Laravel News <https://laravel-news.com/>`__ : Laravel News, a community-driven portal with news, tutorials, and packages.

By following these steps, you'll have a Laravel development environment set up and be ready to start building applications. 
Laravel's rich feature set and elegant syntax make it a powerful tool for modern web development.

******************************
Resources
******************************

- 👉 New to **AppSeed**? Join our 8k+ Community using GitHub `One-Click SignIN  </users/signin/>`__.
- 👉 ``Download`` `products </product/>`__ and start fast a new project 
- 👉 Bootstrap your startUp, MVP or Legacy project with a `custom development </custom-development/>`__  sprint
