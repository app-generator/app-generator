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

Conclusion
----------

Each of these frameworks offers unique strengths:

- **NestJS** is ideal for large-scale applications with complex architecture.
- **Hono** is perfect for performance-critical applications on the edge.
- **Hapi** is well-suited for applications needing robust security and configuration capabilities.

Choose based on your specific project requirements and development preferences.

.. include::  /_templates/components/footer-links.rst