Getting Started
===============

`NestJS <https://nestjs.com/>`__ is a progressive Node.js framework for building efficient, reliable, and scalable server-side applications. 
It is one of the most popular NodeJS frameworks and was built on the battle-tested Express framework.

This documentation provides a complete guide to getting started with and understanding NestJS.

It includes a comprehensive overview, NestJS's pros and cons, setup, configuration, middleware, modules, community resources, authentication setup, ORM integration, amd more.

.. include::  /_templates/components/banner-top.rst

Overview
--------

NestJS is built on TypeScript and inspired by Angular's architecture, making it highly modular and well-suited for scalable, enterprise-grade applications.

NestJS uses decorators to define modules and controllers, streamlining the development process.

Pros
^^^^

- **Type Safety**: Full TypeScript support, enhancing maintainability and readability.
- **Modular Architecture**: Built around modules, which makes structuring large applications manageable.
- **Built-in Testing**: Offers native support for unit and end-to-end testing.
- **Extensive Ecosystem**: Compatible with a wide range of libraries, including those for microservices, WebSockets, and GraphQL.

Cons
^^^^

- **Learning Curve**: Requires familiarity with TypeScript and may be challenging for beginners.
- **Dependency on Decorators**: Heavy reliance on decorators, which can be challenging to debug.
- **Complexity**: Designed for complex applications, potentially overkill for small projects.

Quickstart
----------

To install NestJS and start a new project, run:

.. code-block:: bash

    npm install -g @nestjs/cli
    nest new project-name

Basic Server Example
^^^^^^^^^^^^^^^^^^^^

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

Routing
-------

In NestJS, routing is handled by controllers, which define endpoints and HTTP methods for managing incoming requests.

Routes can be organized by creating controllers within different modules, making it easy to structure large applications.

Define a Controller
^^^^^^^^^^^^^^^^^^^

Use the ``@Controller`` decorator to specify a base route path.

Within the controller, use decorators like ``@Get()``, ``@Post()``, ``@Put()``, and ``@Delete()`` to define specific HTTP methods.

.. code-block:: typescript

    import { Controller, Get, Post, Body, Param } from '@nestjs/common';

    @Controller('users')
    export class UsersController {

        @Get()
        getAllUsers() {
            return 'This action returns all users';
        }

        @Get(':id')
        getUserById(@Param('id') id: string) {
            return `This action returns user with id ${id}`;
        }

        @Post()
        createUser(@Body() createUserDto: any) {
            return `This action creates a user with data ${JSON.stringify(createUserDto)}`;
        }
    }

NestJS Router Module
^^^^^^^^^^^^^^^^^^^^

For advanced routing configurations, NestJS provides a RouterModule, which allows you to configure nested routes and apply middleware to specific routes.

.. code-block:: typescript

    import { Module } from '@nestjs/common';
    import { RouterModule } from '@nestjs/core';
    import { UsersModule } from './users/users.module';
    import { AuthModule } from './auth/auth.module';

    @Module({
        imports: [
            UsersModule,
            AuthModule,
            RouterModule.register([
                { path: 'api/v1', module: UsersModule },
                { path: 'api/v1/auth', module: AuthModule },
            ]),
        ],
    })
    export class AppModule {}

This setup allows the ``UsersModule`` routes to be prefixed with ``/api/v1`` and ``AuthModule`` routes with ``/api/v1/auth``, making it easier to organize versioned and modular routes within the application.

Configuration
-------------

NestJS offers several configuration options for different environments, utilizing the ``@nestjs/config`` package.

This package provides a flexible way to manage configuration using environment variables.

To install and set up ``@nestjs/config``:

.. code-block:: bash

    npm install @nestjs/config

Then, in your app module:

.. code-block:: typescript

    import { Module } from '@nestjs/common';
    import { ConfigModule } from '@nestjs/config';

    @Module({
        imports: [ConfigModule.forRoot()],
    })
    export class AppModule {}

This setup enables environment-based configurations for any imported modules, using ``process.env`` variables to manage different configurations.

Middleware
----------

NestJS middleware functions operate between request handling and response, enabling tasks like logging, authentication, or error handling.

Here’s an example of a simple logger middleware:

.. code-block:: typescript

    import { Injectable, NestMiddleware } from '@nestjs/common';
    import { Request, Response, NextFunction } from 'express';

    @Injectable()
    export class LoggerMiddleware implements NestMiddleware {
        use(req: Request, res: Response, next: NextFunction) {
            console.log(`Request...`);
            next();
        }
    }

You can apply middleware globally or for specific routes using ``app.use`` or by configuring it within modules.

Modules
-------

NestJS embraces a modular structure with support for a variety of built-in & third-party modules, including support for GraphQL, WebSockets, microservices, and more.

Here's a non-exhaustive list of widely-used NestJS modules:

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

Authentication
--------------

NestJS supports multiple authentication strategies, including JWT (JSON Web Tokens), which is commonly used for stateless, token-based authentication.

To set up JWT authentication:

1. **Install dependencies**:

    .. code-block:: bash

        npm install @nestjs/jwt @nestjs/passport passport-jwt

2. **Configure JWT module** in ``auth.module.ts``:

    .. code-block:: typescript

        import { Module } from '@nestjs/common';
        import { JwtModule } from '@nestjs/jwt';
        import { AuthService } from './auth.service';
        import { JwtStrategy } from './jwt.strategy';

        @Module({
            imports: [
                JwtModule.register({
                    secret: 'YOUR_SECRET_KEY',
                    signOptions: { expiresIn: '60m' },
                }),
            ],
            providers: [AuthService, JwtStrategy],
        })
        export class AuthModule {}

3. **Create a JWT strategy** to validate tokens:

    This will define things like the secret to sign the tokens, the algorithm, etc.

    .. code-block:: typescript

        import { Injectable } from '@nestjs/common';
        import { PassportStrategy } from '@nestjs/passport';
        import { ExtractJwt, Strategy } from 'passport-jwt';

        @Injectable()
        export class JwtStrategy extends PassportStrategy(Strategy) {
            constructor() {
                super({
                    jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
                    secretOrKey: 'YOUR_SECRET_KEY',
                });
            }

            async validate(payload: any) {
                return { userId: payload.sub, username: payload.username };
            }
        }

Setting Up ORM
--------------

While it has no native ORM framework, NestJS supports various third-party ORMs, including TypeORM and Prisma, for database management.

Here's a setup example using TypeORM:

1. **Install TypeORM and database driver**:

    .. code-block:: bash

        npm install @nestjs/typeorm typeorm mysql

2. **Configure TypeORM** in ``app.module.ts``:

    .. code-block:: typescript

        import { Module } from '@nestjs/common';
        import { TypeOrmModule } from '@nestjs/typeorm';
        import { User } from './user.entity';

        @Module({
            imports: [
                TypeOrmModule.forRoot({
                    type: 'mysql',
                    host: 'localhost',
                    port: 3306,
                    username: 'root',
                    password: 'password',
                    database: 'test',
                    entities: [User],
                    synchronize: true,
                }),
                TypeOrmModule.forFeature([User]),
            ],
        })
        export class AppModule {}

3. **Create an entity** (e.g., ``user.entity.ts``):

    .. code-block:: typescript

        import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';

        @Entity()
        export class User {
            @PrimaryGeneratedColumn()
            id: number;

            @Column()
            name: string;

            @Column()
            email: string;
        }

4. **Inject repository in a service**:

    .. code-block:: typescript

        import { Injectable } from '@nestjs/common';
        import { InjectRepository } from '@nestjs/typeorm';
        import { Repository } from 'typeorm';
        import { User } from './user.entity';

        @Injectable()
        export class UserService {
            constructor(
                @InjectRepository(User)
                private userRepository: Repository<User>,
            ) {}

            async findAll(): Promise<User[]> {
                return this.userRepository.find();
            }
        }

Community and Resources
-----------------------

NestJS has an active community, regularly updated documentation, and a robust set of plugins available. For community support, explore the following resources:

- `Official Docs <https://docs.nestjs.com/>`__
- `Official GitHub Repo <https://github.com/nestjs/nest/>`__

.. include::  /_templates/components/footer-links.rst
