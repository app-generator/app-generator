Getting Started
===============

Angular is a platform and framework for building single-page client applications using HTML and TypeScript. Let's go through the essential steps to get started with Angular development.

.. include::  /_templates/components/banner-top.rst
    
Prerequisites
-------------

Before you begin, ensure you have:

1. **Node.js and npm**: Angular requires Node.js version 16.14.0 or later.

- Check your version: `node -v` and `npm -v`
- Download from [nodejs.org](https://nodejs.org/) if needed

Step 1: Install Angular CLI
---------------------------

The Angular CLI is a command-line interface tool for creating, developing, scaffolding, and maintaining Angular applications.

.. code-block:: bash

    npm install -g @angular/cli


Verify installation:

.. code-block:: bash

    ng version


Step 2: Create a New Angular Project
------------------------------------

.. code-block:: bash

    ng new my-first-app


During the setup process, the CLI will ask you:

- If you want to add Angular routing (recommended for most applications)
- Which CSS preprocessor you want to use (CSS, SCSS, SASS, LESS, etc.)

Step 3: Navigate to Your Project Directory
------------------------------------------

.. code-block:: bash

    cd my-first-app


Step 4: Serve the Application
-----------------------------

.. code-block:: bash

    ng serve


This builds and serves your app, rebuilding on file changes. Open your browser to `http://localhost:4200/` to see the application.

Step 5: Understanding the Project Structure
-------------------------------------------

- **src/app**: This is where most of your code will go
    - **app.component.ts**: The main component
    - **app.module.ts**: The root module that defines how the application parts fit together
- **src/assets**: For images and other assets
- **src/environments**: For environment-specific configuration
- **angular.json**: Angular CLI configuration
- **package.json**: npm dependencies and scripts

Step 6: Create a New Component
------------------------------

.. code-block:: bash

    ng generate component hello-world


Or the shorthand:

.. code-block:: bash

    ng g c hello-world


Step 7: Understanding Angular Concepts
--------------------------------------

Components
**********

Components are the fundamental building blocks of Angular applications.

.. code-block:: typescript

    // hello-world.component.ts
    import { Component } from '@angular/core';

    @Component({
    selector: 'app-hello-world',
    templateUrl: './hello-world.component.html',
    styleUrls: ['./hello-world.component.css']
    })
    export class HelloWorldComponent {
    message = 'Hello, Angular!';
    }


Templates
*********

Templates define the component's UI with HTML and Angular-specific syntax.

.. code-block:: html

    <!-- hello-world.component.html -->
    <div>
        <h1>{{ message }}</h1>
        <button (click)="message = 'Hello, World!'">Change Message</button>
    </div>

Services
********

Services are used for data sharing and business logic.

.. code-block:: bash

    ng generate service data


.. code-block:: typescript

    // data.service.ts
    import { Injectable } from '@angular/core';

    @Injectable({
        providedIn: 'root'
    })
    export class DataService {
        getItems() {
            return ['Item 1', 'Item 2', 'Item 3'];
        }
    }


Modules
*******

Modules help organize your application into cohesive blocks of functionality.

.. code-block:: typescript

    // app.module.ts
    import { NgModule } from '@angular/core';
    import { BrowserModule } from '@angular/platform-browser';
    import { AppComponent } from './app.component';
    import { HelloWorldComponent } from './hello-world/hello-world.component';

    @NgModule({
    declarations: [
        AppComponent,
        HelloWorldComponent
    ],
    imports: [
        BrowserModule
    ],
    providers: [],
    bootstrap: [AppComponent]
    })
    export class AppModule { }


Step 8: Building for Production
-------------------------------

When you're ready to deploy:

.. code-block:: bash

    ng build --prod

This creates a `dist/` folder with all the files needed to deploy your application.

Next Steps
----------

- Explore Angular's `official documentation <https://angular.io/docs>`__
- Add routing to navigate between components
- Connect to APIs using HttpClient
- Implement forms (template-driven and reactive)
- Set up testing with Karma and Jasmine

Common Commands
---------------

- `ng new` - Create a new project
- `ng serve` - Develop locally
- `ng generate` (or `ng g`) - Generate components, services, etc.
- `ng test` - Run tests
- `ng build` - Build for production
- `ng update` - Update Angular version

.. include::  /_templates/components/footer-links.rst
