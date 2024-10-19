Getting Started
=====================   

To start using `React <https://react.dev/>`__, you typically need: 

- **Node.js and npm**: Install Node.js, which includes npm (Node Package Manager) to manage dependencies.
- **Create a React App**: Use Create React App, a command-line tool to set up a new React project with a sensible default configuration.

.. include::  /_templates/components/banner-top.rst
    
.. code-block:: bash 

    npx create-react-app my-app
    cd my-app
    npm start

Once React is installed, here is a simple, reusable UI Component: 

.. code-block:: javascript 

    import React from 'react';

    function HelloWorld() {
        return (
            Hello, World!
        );
    }

    export default HelloWorld;

This component renders a simple `Hello, World!` message.

In conclusion, React is a powerful tool for modern web development, enabling the creation of dynamic and responsive user interfaces with relative ease.

.. include::  /_templates/components/footer-links.rst
