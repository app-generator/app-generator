Frameworks
==========

When choosing a `Node.js <./index.html>`__ framework, it's essential to understand the unique features and use cases of each.
Here, we compare **Nest**, **Hono**, and **Hapi** to help you decide which framework best suits your project needs.

.. include::  /_templates/components/banner-top.rst

NestJS
------

NestJS is a progressive Node.js framework for building efficient, reliable, and scalable server-side applications.

**Features**

- **Architecture**: Based on TypeScript and heavily inspired by Angular.
- **Extensibility**: Easily integrates with other libraries.
- **Modularity**: Encourages modular development with decorators.
- **Support for GraphQL**: Built-in support for GraphQL and WebSockets.

**Use Cases**

- Enterprise applications requiring robust structure.
- Applications needing extensive scalability and testability.

**Getting Started**

To install NestJS and start a new project, run:

.. code-block:: bash

    npm install -g @nestjs/cli
    nest new project-name

**Basic Server Example**

Create a controller (e.g. `src/app.controller.ts`) in your src folder to handle HTTP requests.

.. code-block:: typescript

    import { Controller, Get } from '@nestjs/common';

    @Controller()
    export class AppController {
        @Get()
        getHello(): string {
            return 'Hello from NestJS!';
        }
    }

Then update the main module (`src/app.module.ts`) to include this controller.

.. code-block:: typescript

    import { Module } from '@nestjs/common';
    import { AppController } from './app.controller';

    @Module({
        imports: [],
        controllers: [AppController],
        providers: [],
    })
    export class AppModule {}

Finally, start the server.

.. code-block:: bash

    npm run start

Now, visit http://localhost:3000 to see the message "Hello from NestJS!"

NestJS Built-in Modules
^^^^^^^^^^^^^^^^^^^^^^^

NestJS offers various native modules that support different functionalities right out of the box, without requiring additional dependencies. Here’s an overview of some of these modules:

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Module
     - Description
   * - ``@nestjs/graphql``
     - Provides GraphQL support in NestJS with schema-first and code-first approaches. Includes decorators for defining resolvers, schemas, and allows the creation of GraphQL APIs in a structured, type-safe manner.
   * - ``@nestjs/microservices``
     - Supports building microservice-based applications, with transport layers such as TCP, Redis, NATS, MQTT, and Kafka. This module allows efficient communication and scalability between services.
   * - ``@nestjs/testing``
     - Built-in testing utilities for writing unit and end-to-end (e2e) tests. Integrates well with popular testing frameworks like Jest and provides a `TestingModule` to isolate and test modules independently.
   * - ``@nestjs/websockets`` & ``@nestjs/platform-socket.io``
     - WebSocket support with decorators for handling events and messages. The `@nestjs/platform-socket.io` package provides the Socket.IO platform adapter for real-time communication.
   * - ``@nestjs/jwt``
     - Adds JSON Web Token (JWT) support to facilitate secure authentication. Commonly used in conjunction with ``@nestjs/passport`` for building JWT-based authentication systems.
   * - ``@nestjs/cli``
     - Command-line interface to scaffold and manage NestJS applications, generate components, and streamline the development process.
   * - ``@nestjs/swagger``
     - Module for integrating Swagger OpenAPI documentation in NestJS applications. Automatically generates interactive API documentation based on decorators in the code.
   * - ``@nestjs/config``
     - Configuration management for handling environment variables and centralized configuration across modules. Integrates well with the ``ConfigService`` for safe and type-checked access to configuration variables.

Hono
----

Hono is an ultrafast web framework for the Edge, built for speed and simplicity.

**Features**

- **Performance**: Optimized for speed; ideal for edge computing.
- **Minimalistic Design**: Simple API for quick development.
- **Middleware Support**: Chainable middleware functions.

**Use Cases**

- High-performance applications where speed is critical.
- Applications running on edge networks.

**Getting Started**

To install Hono, set up your project with:

.. code-block:: bash

    npm install hono

**Basic Server Example**

Create a file for your server (e.g `server.js`).

.. code-block:: javascript

    import { Hono } from 'hono';

    const app = new Hono();

    app.get('/', (c) => c.text('Hello from Hono!'));

    app.fire();

Start the server.

.. code-block:: bash

    node server.js

Visit http://localhost:8787 to see "Hello from Hono!" (port may vary based on setup).

Hono Built-in Modules
^^^^^^^^^^^^^^^^^^^^^

Hono has several built-in modules for different use cases. Here’s an overview of some of its available modules:

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Module
     - Description
   * - ``hono/jsx``
     - Provides support for JSX syntax within Hono, allowing developers to build components with HTML-like syntax in their JavaScript code, improving readability and structure.
   * - ``hono/cookie``
     - A utility module for handling cookies in Hono applications. It offers methods to read, write, and manage cookies for maintaining session or user-specific data.
   * - ``hono/validator``
     - Offers validation functions for request bodies, query parameters, and headers. It simplifies input validation and error handling in web applications.
   * - ``hono/adapter``
     - A collection of adapters for deploying Hono apps on different platforms. The ``hono/adapter/env`` module is particularly useful for deploying to edge environments, enabling seamless deployment to cloud services like Vercel, Cloudflare Workers, and others.
   * - ``hono/css``
     - Provides built-in support for adding CSS to Hono applications, allowing the inclusion of CSS styles directly within the framework for easier styling and layout management.
   * - ``hono/html``
     - A utility module that simplifies rendering HTML pages from JavaScript. This module is used to handle the generation of dynamic HTML content within Hono applications.
   * - ``hono/jwt``
     - Adds JWT (JSON Web Token) support for authentication and authorization in Hono applications. It allows you to verify and decode JWT tokens within your requests.
   * - ``hono/ssg``
     - Static Site Generation (SSG) support for building static pages from dynamic content. Useful for generating SEO-friendly pages and faster server responses by pre-rendering HTML at build time.
   * - ``hono/streaming``
     - Enables server-sent events (SSE) and other real-time streaming capabilities in Hono applications, facilitating real-time data updates and interactions between server and client.
   * - ``hono/testing``
     - Provides utilities for testing Hono applications, including support for writing unit tests, mocking requests, and handling responses, integrating well with testing frameworks like Jest.
   * - ``@hono/node-ws``
     - WebSocket support for Hono applications, using the ``node-ws`` package. This module allows you to build WebSocket-based real-time communication features in Hono applications.

Hapi
----

Hapi is a configuration-driven framework with strong security features for building applications and services in Node.js.

**Features**

- **Configuration-centric**: Focuses on configuration over code.
- **Security**: Built-in support for input validation, authentication, and more.
- **Plugins**: Extensive plugin system for extending framework capabilities.

**Use Cases**

- Applications requiring comprehensive security and configuration.
- API services with complex routing and validation needs.

**Getting Started**

To install Hapi, execute:

.. code-block:: bash

    npm install @hapi/hapi

Then create a file for your server (e.g. `server.js`).

.. code-block:: javascript

    import Hapi from '@hapi/hapi';

    const init = async () => {
    const server = Hapi.server({
        port: 3000,
        host: 'localhost'
    });

    server.route({
        method: 'GET',
        path: '/',
        handler: () => 'Hello from Hapi!'
    });

    await server.start();
    console.log('Server running on %s', server.info.uri);
    };

    init();

Start the server:

.. code-block:: bash

    node server.js

Visit http://localhost:3000 to see "Hello from Hapi!"

Hapi Built-in Modules
^^^^^^^^^^^^^^^^^^^^^

Hapi has a rich set of native modules that extend its capabilities for various use cases. Below is an overview of some Hapi modules:

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Module
     - Description
   * - ``@hapi/basic``
     - Implements Basic Authentication for Hapi applications, allowing user authentication via username and password.
   * - ``@hapi/cookie``
     - Cookie-based authentication scheme for managing user sessions securely with cookies in Hapi applications.
   * - ``@hapi/bell``
     - A third-party login plugin that provides easy integration with popular OAuth providers like Google, GitHub, and Facebook.
   * - ``@hapi/jwt``
     - JSON Web Token (JWT) authentication support for secure API requests, including verification and token handling.
   * - ``@hapi/boom``
     - Utility for creating HTTP-friendly error objects. Provides helpful methods for generating responses with different status codes and error messages.
   * - ``@hapi/inert``
     - Static file and directory handler for Hapi, allowing the serving of static assets such as HTML, CSS, and JavaScript files.
   * - ``@hapi/nes``
     - WebSocket support and real-time messaging for Hapi applications. Enables client-server communication for live updates and interactions.
   * - ``@hapi/crumb``
     - Cross-Site Request Forgery (CSRF) protection plugin for Hapi applications, adding security to forms and requests.
   * - ``@hapi/yar``
     - Session management and data storage plugin for Hapi, often used to manage user sessions or store temporary data across requests.
   * - ``@hapi/vision``
     - Template rendering support in Hapi, compatible with various template engines like Handlebars and EJS. Useful for building dynamic server-side views.
   * - ``@hapi/lab``
     - Testing utility for Hapi, providing a test runner with tools for assertions, coverage reporting, and test organization.
   * - ``@hapi/shot``
     - HTTP assertions library that simulates server requests, ideal for testing route responses in Hapi applications.
   * - ``@hapi/hoek``
     - Utility library with helpful functions for object manipulation, validation, and other common tasks.
   * - ``@hapi/scooter``
     - User-agent parsing for Hapi applications, extracting details about the client's device, browser, and OS from HTTP headers.
   * - ``@hapi/glue``
     - Utility for composing Hapi servers and configuring plugins with predefined options, simplifying the setup process.
   * - ``@hapi/h2o2``
     - Proxy handler for Hapi, enabling the creation of HTTP proxies for forwarding requests to external services.

Conclusion
----------

Each of these frameworks offers unique strengths:

- **NestJS** is ideal for large-scale applications with complex architecture.
- **Hono** is perfect for performance-critical applications on the edge.
- **Hapi** is well-suited for applications needing robust security and configuration capabilities.

Choose based on your specific project requirements and development preferences.

.. include::  /_templates/components/footer-links.rst