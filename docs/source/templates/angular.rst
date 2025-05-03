Angular 
=======

Angular is a robust, full-featured framework for building web applications developed and maintained by Google. 
It's a complete rewrite of AngularJS and has become one of the most popular enterprise-level frontend frameworks.

.. include::  /_templates/components/banner-top.rst

Here's what makes Angular powerful:

- **Component-based architecture**: Organize your application into reusable, encapsulated components
- **TypeScript integration**: Benefit from strong typing and object-oriented features
- **Dependency injection**: Build services that can be injected where needed
- **RxJS integration**: Handle asynchronous operations using observables
- **Comprehensive tooling**: Angular CLI simplifies project creation, development, and deployment

A simple example of an Angular component:

.. code-block:: typescript

   // hello.component.ts
   import { Component } from '@angular/core';

   @Component({
   selector: 'app-hello',
   template: `
      <h1>Hello, {{ name }}!</h1>
      <button (click)="incrementCount()">
         You clicked me {{ count }} times
      </button>
   `
   })
   export class HelloComponent {
      name = 'World';
      count = 0;
      
      incrementCount() {
         this.count++;
      }
   }

To fetch data from an API:

.. code-block:: typescript

   // data.service.ts
   import { Injectable } from '@angular/core';
   import { HttpClient } from '@angular/common/http';
   import { Observable } from 'rxjs';

   @Injectable({
   providedIn: 'root'
   })
   export class DataService {
   constructor(private http: HttpClient) {}
   
   getData(): Observable<any[]> {
         return this.http.get<any[]>('https://api.example.com/data');
      }
   }

.. include::  /_templates/components/footer-links.rst
   
Resources
---------

.. toctree::
   :maxdepth: 1
   
   angular/index
