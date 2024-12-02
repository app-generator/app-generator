NestJS API Server
=================

.. title:: NestJS API Server - Open-source Starter | App Generator
.. meta::
    :description: Start fast with an open-source API server powered by NestJS

This documentation provides a step-by-step guide to building a secure
NestJS backend server with Auth0 for authentication, role-based access control, and TypeORM for database (PostgreSQL) management.

The server will also have features such as pagination, public
and private API endpoints, and role-based permissions for **Admins** and
**Users**.

.. include::  /_templates/components/banner-top.rst

Project Setup
-------------

You will need the following:

-  **Node.js and npm**: You’ll need Node.js installed on your machine.
   It comes with npm (Node Package Manager), which is used to manage
   dependencies. You can download it from the official `Next.js
   website <https://nextjs.org/>`__.
-  **Database**: We’ll use
   `PostgreSQL <https://www.postgresql.org/download/>`__ in this guide.
   Ensure it’s installed and running on your machine.

Step 1: Set up a NestJS Project
-------------------------------

First, install the NestJS CLI globally by running:

.. code:: bash 

   npm install -g @nestjs/cli

Run the following command to create a new NestJS project:

.. code:: bash 
   
   nest new my-nest-app

Replace ``my-nest-app`` with your desired project name.
During the setup, choose a package manager (e.g., npm, yarn, or pnpm).

Step 2: Set Up Auth0 for GitHub Authentication
----------------------------------------------

We’ll integrate Auth0 to allow users to authenticate using their GitHub
accounts.

Prerequisites
~~~~~~~~~~~~~

-  **Auth0 Account**: Sign up for a free `Auth0
   account <https://auth0.com/>`__.
-  **GitHub Account**: Sign up for a free `GitHub
   account <https://github.com/>`__.

Create an Auth0 Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Log in to your Auth0 dashboard.
2. Navigate to **Applications** and click on **Create Application**.
3. Enter a name for your application (e.g. ``NestJS Backend API``) and
   select **Regular Web Applications**.
4. Click **Create**.

Configure GitHub as a Social Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. In the Auth0 dashboard, navigate to **Authentication** > **Social**.
2. Find **GitHub** in the list and click on it.
3. Click **Create Connection**.

Register a New OAuth App in GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to your GitHub account settings and navigate to **Developer
   settings** > **OAuth Apps**.
2. Click **New OAuth App**.
3. Fill in the details:

   -  **Application Name**: Your app’s name (e.g.
      ``NestJS Backend API``).
   -  **Homepage URL**: ``https://YOUR_AUTH0_DOMAIN/``
   -  **Authorization Callback URL**:
      ``https://YOUR_AUTH0_DOMAIN/login/callback``

   Replace ``YOUR_AUTH0_DOMAIN`` with your Auth0 domain, which you can
   find in your Auth0 dashboard under **Applications** > **Settings** >
   **Domain**.

4. Click **Register Application**.
5. After registration, you’ll receive a **Client ID** and **Client
   Secret**.

Configure GitHub Connection in Auth0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Back in Auth0, in the GitHub connection settings, enter the **Client
   ID** and **Client Secret** obtained from GitHub.
2. Optionally, select the permissions (scopes) you want to request from
   GitHub users.
3. Click **Save**.

Enable the GitHub Connection for Your Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. After saving, you’ll be redirected to the GitHub connection page.
2. Under **Applications**, enable the GitHub connection for your
   application by toggling the switch next to your application’s name.

Test connection
~~~~~~~~~~~~~~~

Finally, test your connection by following `these instructions <https://auth0.com/docs/dashboard/guides/connections/test-connections-social>`__.

Install Required Packages
~~~~~~~~~~~~~~~~~~~~~~~~~

Next install necessary libraries with the following code:

.. code:: bash
   npm install passport @nestjs/passport passport-jwt jwks-rsa dotenv

Here's what these packages do:

- **passport**: Express-compatible authentication middleware for Node.js.

- **@nestjs/passport**: The Passport utility module for Nest.

- **passport-jwt**: Passport Strategy for authenticating with a JSON Web Token (JWT).

- **jwks-rsa**: A library to retrieve RSA signing keys from a JWKS (JSON Web Key Set) endpoint.

Create an JWT Strategy
~~~~~~~~~~~~~~~~~~~~~~~~

Now we define a JWT Strategy. A strategy in NestJS is a reusable and pluggable component used in the Passport authentication framework to handle various authentication mechanisms.

In ``src/auth/strategies/jwt.strategy.ts``, add:

.. code:: typescript

   import { Injectable } from '@nestjs/common';
   import { PassportStrategy } from '@nestjs/passport';
   import { ExtractJwt, Strategy } from 'passport-jwt';
   import { passportJwtSecret } from 'jwks-rsa';
   import * as dotenv from 'dotenv';

   dotenv.config();

   @Injectable()
   export class JwtStrategy extends PassportStrategy(Strategy) {
      constructor() {
         super({
            secretOrKeyProvider: passportJwtSecret({
            cache: true,
            rateLimit: true,
            jwksRequestsPerMinute: 5,
            jwksUri: `${process.env.AUTH0_ISSUER_URL}.well-known/jwks.json`,
            }),

            jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
            audience: process.env.AUTH0_AUDIENCE,
            issuer: `${process.env.AUTH0_ISSUER_URL}`,
            algorithms: ['RS256'],
         });
      }

      validate(payload: unknown): unknown {
         return payload;
      }
   }

Now, configure Environment Variables by add the following variables to your ``.env`` file:

.. code:: plaintext

   AUTH0_AUTH0_AUDIENCE=your-auth0-audience
   AUTH0_ISSUER_URL=your-auth0-issuer_url

Create an Auth Module
~~~~~~~~~~~~~~~~~~~~~

Create an auth module by running:

.. code:: bash

   nest generate module auth

Define the Auth Module in ``src/auth/auth.module.ts`` as follows:

.. code:: typescript

   import { Module } from '@nestjs/common';
   import { PassportModule } from '@nestjs/passport';
   import { JwtStrategy } from './jwt.strategy';

   @Module({
   imports: [PassportModule.register({ defaultStrategy: 'jwt' })],
   providers: [JwtStrategy],
   exports: [PassportModule],
   })

   export class AuthModule {}

You should now be able to login via GitHub, we will test this later after creating endpoints.

Step 3: Configure the Database
------------------------------

We’ll use TypeORM with PostgreSQL.

Install Dependencies
~~~~~~~~~~~~~~~~~~~~

Install TypeORM and the PostgreSQL driver dependencies by running the following command:

.. code:: bash

   npm install --save @nestjs/typeorm typeorm pg

Configure TypeORM
~~~~~~~~~~~~~~~~~

Configure TypeORM in your ``app.module.ts`` to connect to a running PostgreSQL database. Open the ``src/app.module.ts`` file and add:

.. code:: typescript

   import { Module } from '@nestjs/common';
   import { TypeOrmModule } from '@nestjs/typeorm';

   @Module({
     imports: [
       TypeOrmModule.forRoot({
         type: 'postgres', // Database type
         host: 'localhost', // Your database host
         port: 5432,        // Your database port
         username: 'your_db_username', // Replace with your DB username
         password: 'your_db_password', // Replace with your DB password
         database: 'your_db_name',     // Replace with your DB name
         entities: [__dirname + '/**/*.entity{.ts,.js}'], // Entities path
         synchronize: true, // Auto-sync entities with the database 
       }),
       UsersModule, // Import UsersModule
     ],
   })
   export class AppModule {}

**What’s Happening?**

-  **TypeORM Configuration**: We set up a connection to our PostgreSQL
   database using TypeORM.
-  **Entities**: Specifies the path where TypeORM can find the entity
   files.

Step 4: Create the User Entity
------------------------------

Now let's define our users.

Generate the Users Module
~~~~~~~~~~~~~~~~~~~~~~~~~

To create the users entity, generate the Users module using the Nest CLI command:

.. code:: bash

   nest generate module users

Create the User Entity
~~~~~~~~~~~~~~~~~~~~~~

Generate the User entity class with the Nest CLI:

.. code:: bash

   nest generate class users/user --no-spec

This command generates a ``user.ts`` file in the ``src/users/user`` directory.

Defining the User Entity
~~~~~~~~~~~~~~~~~~~~~~~~

Define the ``User`` entity with profile fields and authentication details. In ``src/users/user.ts``, define the entity:

.. code:: typescript

   import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

   export enum Role {
     ADMIN = 'admin',
     USER = 'user',
   }

   @Entity()
   export class User {
     @PrimaryGeneratedColumn()
     id: number;

     @Column({ unique: true })
     sub: string; // Auth0 user identifier

     @Column({ type: 'enum', enum: Role, default: Role.USER })
     role: Role;

     @Column()
     name: string;

     @Column()
     surname: string;

     @Column({ nullable: true })
     bio: string;

     @Column({ nullable: true })
     country: string;

     @Column({ nullable: true })
     address: string;

     @Column({ nullable: true })
     job: string;

     @Column({ unique: true })
     email: string;

     @Column({ nullable: true })
     password: string; // Password may be null if using social login
   }

**What’s Happening?**

-  **User Entity**: Defines the structure of the ``User`` table in the
   database.
-  **Role Enum**: Specifies possible user roles (``ADMIN`` and
   ``USER``).
-  **TypeORM Decorators**: We use decorators like ``@Entity()``,
   ``@PrimaryGeneratedColumn()``, and ``@Column()`` to map the class
   properties to database columns.

Step 5: Creating Roles and Guards
---------------------------------

Now let's create various user roles and apporpriate guards for them.

Create Roles Decorator
~~~~~~~~~~~~~~~~~~~~~~

Create a custom decorator to specify required roles for route handlers. Create a ``src/auth/roles.decorator.ts`` file and add the following:

.. code:: typescript

   import { SetMetadata } from '@nestjs/common';

   export const Roles = (...roles: string[]) => SetMetadata('roles', roles);

Create Roles Guard
~~~~~~~~~~~~~~~~~~

Create a guard to enforce role-based access control. Create a ``src/auth/roles.guard.ts`` file and add this code:

.. code:: typescript

   import { Injectable, CanActivate, ExecutionContext } from '@nestjs/common';
   import { Reflector } from '@nestjs/core';
   import { Role } from '../users/user';

   @Injectable()
   export class RolesGuard implements CanActivate {
     constructor(private reflector: Reflector) {}

     canActivate(context: ExecutionContext): boolean {
       const requiredRoles = this.reflector.getAllAndOverride('roles', [
         context.getHandler(),
         context.getClass(),
       ]);

       if (!requiredRoles) {
         // No roles required, allow access
         return true;
       }

       const { user } = context.switchToHttp().getRequest();
       return user && requiredRoles.includes(user.role);
     }
   }

Step 6: Implement User Profiles
-------------------------------

Now let's implement user profiles.

Update Users Module
~~~~~~~~~~~~~~~~~~~

Update the ``UsersModule`` to register the ``User`` entity and provide services and controllers. Open the ``src/users/users.module.ts`` file and update as follows:

.. code:: typescript

   import { Module } from '@nestjs/common';
   import { TypeOrmModule } from '@nestjs/typeorm';
   import { User } from './user'; // Import User entity
   import { UsersService } from './users.service';
   import { UsersController } from './users.controller';

   @Module({
     imports: [TypeOrmModule.forFeature([User])], // Register User entity
     providers: [UsersService],
     controllers: [UsersController],
     exports: [UsersService],
   })

   export class UsersModule {}

Develop the Users Service
~~~~~~~~~~~~~~~~~~~~~~~~~

Implement the ``UsersService`` to handle database operations for users. Create a ``src/users/users.service.ts`` file and add the following code to it:

.. code:: typescript

   import { Injectable } from '@nestjs/common';
   import { Repository } from 'typeorm';
   import { User, Role } from './user';
   import { InjectRepository } from '@nestjs/typeorm';

   @Injectable()
   export class UsersService {
     constructor(
       @InjectRepository(User)
       private usersRepository: Repository,
     ) {}

     // Find all users with pagination
     async findAll(page: number, limit: number): Promise {
       return this.usersRepository.find({
         skip: (page - 1) * limit,
         take: limit,
         select: ['id', 'name', 'surname', 'bio', 'country', 'address', 'job'],
       });
     }

     // Find a user by ID
     async findById(id: number): Promise {
       return this.usersRepository.findOne(id, {
         select: ['id', 'name', 'surname', 'bio', 'country', 'address', 'job'],
       });
     }

     // Find or create a user by 'sub' (Auth0 identifier)
     async findOrCreate(userData: Partial): Promise {
       let user = await this.usersRepository.findOne({ sub: userData.sub });
       if (!user) {
         user = this.usersRepository.create(userData);
         user.role = Role.USER;
         await this.usersRepository.save(user);
       }
       return user;
     }

     // Update an existing user
     async update(id: number, userData: Partial): Promise {
       await this.usersRepository.update(id, userData);
       return this.usersRepository.findOne(id);
     }

     // Delete a user
     async delete(id: number): Promise {
       await this.usersRepository.delete(id);
     }
   }

Build the Users Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~

Create the ``UsersController`` to define the API endpoints for user operations. Open a ``src/users/users.controller.ts`` file and add:

.. code:: typescript

   import {
     Controller,
     Get,
     Put,
     Delete,
     Param,
     Body,
     UseGuards,
     Request,
     Query,
     ForbiddenException,
   } from '@nestjs/common';
   import { UsersService } from './users.service';
   import { AuthGuard } from '@nestjs/passport';
   import { RolesGuard } from '../auth/roles.guard';
   import { Roles } from '../auth/roles.decorator';
   import { Role } from './user';

   @Controller('users')
   export class UsersController {
     constructor(private usersService: UsersService) {}

     // Public Access: Get all users with pagination
     @Get()
     async getAll(@Query('page') page = 1, @Query('limit') limit = 10) {
       return this.usersService.findAll(page, limit);
     }

     // Public Access: Get a user by ID
     @Get(':id')
     getById(@Param('id') id: number) {
       return this.usersService.findById(id);
     }

     // Private Access: Update user information
     @UseGuards(AuthGuard('jwt'), RolesGuard)
     @Roles(Role.USER, Role.ADMIN)
     @Put(':id')
     async update(@Param('id') id: number, @Body() userData, @Request() req) {
       const userId = req.user.id;
       if (userId !== +id && req.user.role !== Role.ADMIN) {
         throw new ForbiddenException('You can only update your own profile');
       }
       return this.usersService.update(id, userData);
     }

     // Private Access: Delete a user
     @UseGuards(AuthGuard('jwt'), RolesGuard)
     @Roles(Role.ADMIN)
     @Delete(':id')
     async delete(@Param('id') id: number) {
       await this.usersService.delete(id);
       return { message: 'User deleted successfully' };
     }
   }

**What's Happening?**

-  **UsersController**: Exposes API endpoints for user operations.
-  **UseGuards**: Protects routes with authentication and role-based
   authorization.
-  **Roles**: Ensures only users with specific roles can access certain
   endpoints.
-  **Access Checks**: Correctly compares ``req.user.id`` with the ``id``
   parameter to verify if the user can perform the action.

Step 7: Define API Endpoints
----------------------------

Let's now define our API endpoints.

Public Endpoints
~~~~~~~~~~~~~~~~

-  **GET `/users`**: Retrieve all users with pagination.
-  **GET `/users/:id`**: Get a specific user by ID.

Private Endpoints
~~~~~~~~~~~~~~~~~

-  **PUT `/users/:id`**: Update a user’s information (Authenticated
   user or Admin).
-  **DELETE `/users/:id`**: Delete a user (Admin only).

**Roles and Permissions:**

-  **Admin**:

   -  Can view, update, and delete any user.

-  **User**:

   -  Can view and update only their own information.

Step 8: Implement Role-Based Access Control
-------------------------------------------

Use the ``@Roles()`` decorator to specify required roles for route
handlers.

Apply the ``RolesGuard`` to protect routes based on user roles. Here's an example of protecting a route with role-based access control:

.. code:: typescript

   @UseGuards(AuthGuard('jwt'), RolesGuard)
   @Roles(Role.ADMIN)
   @Delete(':id')
   async delete(@Param('id') id: number) {
     await this.usersService.delete(id);
     return { message: 'User deleted successfully' };
   }

This restricts access to sensitive operations based on user roles.

Step 9: Test the API
---------------------

You can test the API endpoints using tools like
`Postman <https://www.postman.com/>`__ or `cURL <https://curl.se/>`__.

Obtain an Access Token
~~~~~~~~~~~~~~~~~~~~~~

To access protected routes, you’ll need a valid JWT access token issued
by Auth0.

Using Auth0’s Authentication Flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set up a simple frontend application that initiates the authentication flow using Auth0’s SDKs, we'll get to this in a later tutorial.

Access Protected Routes
~~~~~~~~~~~~~~~~~~~~~~~

Include the access token in the ``Authorization`` header when making requests to protected routes:

.. code:: plaintext

   Authorization: Bearer YOUR_ACCESS_TOKEN

Conclusion
----------

We’ve built a NestJS backend API with role-based
access control, user profiles, and authentication using Auth0 and GitHub
as a social connection. 

This setup provides a robust foundation for
building scalable and secure applications.

.. include:: /_templates/components/footer-links.rst
