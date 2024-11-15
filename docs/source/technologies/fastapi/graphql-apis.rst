:og:description: Building GraphQL APIs in FastAPI

GraphQL APIs
============

.. title:: Building GraphQL APIs in FastAPI
.. meta::
    :description: Learn how to expose GraphQL APIs - a practical guide

This document will guide you through the process of building GraphQL APIs using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python.

**Requirements:**
- Python 3.8+
- FastAPI
- Strawberry (GraphQL library for Python)

.. include::  /_templates/components/banner-top.rst


Setting Up the Project
----------------------

First, install FastAPI, Uvicorn (ASGI server), and Strawberry for GraphQL support:

.. code-block:: shell

   pip install fastapi uvicorn
   pip install 'strawberry-graphql[fastapi]'

Creating the FastAPI Application
--------------------------------

1. **Define a GraphQL Schema**: Using Strawberry, define a schema for API.
2. **Integrate with FastAPI**: Add a route in FastAPI to serve the GraphQL API.

Defining the Schema
-------------------

Start by defining a schema using Strawberry. We will create a `Book` type and a query for retrieving a list of books.

.. code-block:: python

   # main.py
   from typing import List
   import strawberry

   @strawberry.type
   class Book:
       title: str
       author: str

   books = [
       Book(title="The Great Gatsby", author="F. Scott Fitzgerald"),
       Book(title="1984", author="George Orwell"),
       Book(title="To Kill a Mockingbird", author="Harper Lee")
   ]

   @strawberry.type
   class Query:
       @strawberry.field
       def get_books(self) -> List[Book]:
           return books

   schema = strawberry.Schema(query=Query)

Integrating with FastAPI
------------------------

Once the schema is defined, integrate it with FastAPI by adding the route to serve the GraphQL API.

.. code-block:: python

   from fastapi import FastAPI
   from strawberry.asgi import GraphQL

   app = FastAPI()
   graphql_app = GraphQL(schema)

   app.add_route("/graphql", graphql_app)
   app.add_websocket_route("/graphql", graphql_app)

Running the Application
-----------------------

Run the application using Uvicorn:

.. code-block:: shell

   uvicorn main:app --reload

FastAPI server will be available at `http://127.0.0.1:8000`. You can access the GraphQL Playground at `http://127.0.0.1:8000/graphql`.

Testing the GraphQL API
-----------------------

In the GraphQL Playground, test the `get_books` query:

.. code-block:: graphql

   query {
       getBooks {
           title
           author
       }
   }

Expected response:

.. code-block:: json

   {
     "data": {
       "getBooks": [
         {
           "title": "The Great Gatsby",
           "author": "F. Scott Fitzgerald"
         },
         {
           "title": "1984",
           "author": "George Orwell"
         },
         {
           "title": "To Kill a Mockingbird",
           "author": "Harper Lee"
         }
       ]
     }
   }

Adding Mutations
----------------

Next, we will add a mutation for creating a new book. This requires an update to the `Book` and `Mutation` classes.

.. code-block:: python

   from typing import Optional

   @strawberry.type
   class Mutation:
       @strawberry.mutation
       def add_book(self, title: str, author: str) -> Book:
           new_book = Book(title=title, author=author)
           books.append(new_book)
           return new_book

   schema = strawberry.Schema(query=Query, mutation=Mutation)

Testing the Mutation
--------------------

To test the `add_book` mutation, use the following query in the GraphQL Playground:

.. code-block:: graphql

   mutation {
       addBook(title: "The Catcher in the Rye", author: "J.D. Salinger") {
           title
           author
       }
   }

Expected response:

.. code-block:: json

   {
     "data": {
       "addBook": {
         "title": "The Catcher in the Rye",
         "author": "J.D. Salinger"
       }
     }
   }

Update and Delete
=================

Update
------

Add a mutation for updating a book’s details. The mutation will accept the current title and the new details.

.. code-block:: python

   @strawberry.type
   class Mutation:
       @strawberry.mutation
       def update_book(self, title: str, new_title: str, new_author: str) -> Optional[Book]:
           for book in books:
               if book.title == title:
                   book.title = new_title
                   book.author = new_author
                   return book
           return None

Testing Update
--------------

.. code-block:: graphql

   mutation {
       updateBook(title: "1984", newTitle: "1984 (Updated)", newAuthor: "George Orwell (Updated)") {
           title
           author
       }
   }

Expected response:

.. code-block:: json

   {
     "data": {
       "updateBook": {
         "title": "1984 (Updated)",
         "author": "George Orwell (Updated)"
       }
     }
   }

Delete
------

Add a mutation to delete a book by title. This will remove the book from the list.

.. code-block:: python

   @strawberry.type
   class Mutation:
       @strawberry.mutation
       def delete_book(self, title: str) -> bool:
           for book in books:
               if book.title == title:
                   books.remove(book)
                   return True
           return False

Testing Delete
---------------

.. code-block:: graphql

   mutation {
       deleteBook(title: "To Kill a Mockingbird")
   }

Expected response:

.. code-block:: json

   {
      "data": {
        "deleteBook": false
      }
    }

Conclusion
----------
Building GraphQL APIs with FastAPI and Strawberry provides a seamless and efficient way to create high-performance, scalable APIs with modern Python frameworks. By following the steps outlined, you can implement robust CRUD functionality, enabling dynamic interactions with your data through queries and mutations. This approach ensures flexibility, maintainability, and an excellent developer experience, making it ideal for modern API development.

.. include::  /_templates/components/footer-links.rst
