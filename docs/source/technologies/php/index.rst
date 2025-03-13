Getting Started
===============

PHP (PHP: Hypertext Preprocessor) is a popular server-side scripting language designed specifically for web development. 
PHP code is executed on the server, generating HTML that is then sent to the client's browser.

.. include::  /_templates/components/banner-top.rst

PHP code is typically embedded within HTML and executed on the server, with only the resulting HTML being sent to the client. 

Setting Up Your Environment
---------------------------

Option 1: Using XAMPP 
*********************

1. Download XAMPP from `apachefriends.org <https://www.apachefriends.org/>`__
2. Install XAMPP, which includes Apache, MySQL, PHP, and phpMyAdmin
3. Start the Apache and MySQL services from the XAMPP Control Panel
4. Place your PHP files in the `htdocs` folder (e.g., `C:\xampp\htdocs` on Windows)
5. Access your projects via `http://localhost/your-project-folder`

Option 2: Installing PHP Separately
***********************************

1. Download PHP from `php.net/downloads <https://www.php.net/downloads.php>`__
2. Follow installation instructions for your operating system
3. Install a web server like Apache or Nginx
4. Configure the web server to work with PHP

Your First PHP Script
---------------------

Create a file named `index.php` in your web server's document root folder:

.. code-block:: php

    <!DOCTYPE html>
    <html>
    <head>
        <title>My First PHP Page</title>
    </head>
    <body>
        <h1>Hello, PHP World!</h1>
        
        <?php
        // This is a PHP code block
        echo "<p>The current date and time is: " . date("Y-m-d H:i:s") . "</p>";
        
        // Variables
        $name = "Developer";
        $age = 25;
        
        // Outputting variables
        echo "<p>Hello, my name is $name and I am $age years old.</p>";
        ?>
    </body>
    </html>


Access this file through your web browser by visiting `http://localhost/index.php`.

PHP Basics
----------

Variables
*********

.. code-block:: php

    $text = "Hello World";  // String
    $number = 42;           // Integer
    $float = 3.14;          // Float
    $boolean = true;        // Boolean
    $array = [1, 2, 3];     // Array
    $null = null;           // Null value


Control Structures
******************

.. code-block:: php

    // If-else statement
    if ($age >= 18) {
        echo "You are an adult.";
    } else {
        echo "You are a minor.";
    }

    // Loops
    for ($i = 1; $i <= 5; $i++) {
        echo "Number: $i <br>";
    }

    $colors = ["red", "green", "blue"];
    foreach ($colors as $color) {
        echo "Color: $color <br>";
    }


Functions
*********

.. code-block:: php

    function greet($name) {
        return "Hello, $name!";
    }

    echo greet("John");  // Outputs: Hello, John!


Working with Forms
------------------

Create a form file (`form.php`):

.. code-block:: php

    <!DOCTYPE html>
    <html>
    <head>
        <title>PHP Form Example</title>
    </head>
    <body>
        <form method="post" action="process.php">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required><br><br>
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br><br>
            
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>


Create a processing file (`process.php`):

.. code-block:: php

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $name = $_POST["name"];
        $email = $_POST["email"];
        
        echo "<h2>Form Submission Received</h2>";
        echo "<p>Name: " . htmlspecialchars($name) . "</p>";
        echo "<p>Email: " . htmlspecialchars($email) . "</p>";
    } else {
        echo "No form data submitted.";
    }
    ?>


Database Connection (MySQL)
---------------------------

.. code-block:: php

    <?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "my_database";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Query the database
    $sql = "SELECT id, name, email FROM users";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Output data of each row
        while($row = $result->fetch_assoc()) {
            echo "ID: " . $row["id"] . " - Name: " . $row["name"] . " - Email: " . $row["email"] . "<br>";
        }
    } else {
        echo "0 results";
    }

    $conn->close();
    ?>


Next Steps
----------

1. Learn about PHP arrays and array functions
2. Explore PHP sessions and cookies for state management
3. Study PHP object-oriented programming principles
4. Try a PHP framework like Laravel, Symfony, or CodeIgniter
5. Practice proper security techniques (input validation, prepared statements)

Resources
---------

- [PHP Official Documentation](https://www.php.net/docs.php)
- [W3Schools PHP Tutorial](https://www.w3schools.com/php/)
- [PHP The Right Way](https://phptherightway.com/)
- [Stack Overflow PHP Community](https://stackoverflow.com/questions/tagged/php)
- [PHP Fig - PHP Standards Recommendations](https://www.php-fig.org/psr/)

The PHP ecosystem has evolved tremendously over the years, embracing modern development practices while maintaining its accessibility. 
Whether you're building a personal blog, an e-commerce platform, or the next revolutionary web application, PHP provides the tools and flexibility to bring your vision to life.

.. include::  /_templates/components/footer-links.rst
