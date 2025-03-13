:og:description: NestJS - Resources for students and developers | App-Generator.dev

NestJS
======

.. title:: NestJS - Resources for students and developers | App-Generator.dev
.. meta::
    :description: Unified index for NestJS resources: tutorials, starters, best practices and dev tips

NestJS is a progressive Node.js framework for building efficient, reliable, and scalable server-side applications. 
It uses TypeScript and combines elements of OOP (Object Oriented Programming), FP (Functional Programming), and FRP (Functional Reactive Programming).

.. include::  /_templates/components/banner-top.rst

Key Features
------------

- **TypeScript-based**: Built with and fully supports TypeScript
- **Architectural**: Implements a modular architecture inspired by Angular
- **Versatile**: Supports REST, GraphQL, WebSockets, and microservices
- **Dependency Injection**: Built-in powerful DI container
- **Testing**: Testing utilities included out of the box
- **ORM Integration**: Works with any database through ORM support
- **Middleware**: Robust middleware system with built-in guards and interceptors

Quick Start
-----------

.. code-block:: typescript

    import { Controller, Get, Module, NestFactory } from '@nestjs/core';

    @Controller()
    class AppController {
    @Get()
    getHello(): string {
        return 'Hello World!';
    }
    }

    @Module({
    controllers: [AppController],
    })
    class AppModule {}

    async function bootstrap() {
    const app = await NestFactory.create(AppModule);
    await app.listen(3000);
    }
    bootstrap();


Install and run:

.. code-block:: bash

    npm i -g @nestjs/cli
    nest new project-name
    cd project-name
    npm run start:dev

NestJS provides an out-of-the-box application architecture that enables developers to create highly testable, scalable, loosely coupled, and easily maintainable applications, 
making it ideal for enterprise-grade applications.

.. include::  /_templates/components/footer-links.rst
       
Resources
---------

.. toctree::
   :maxdepth: 1
   
   nestjs/index
