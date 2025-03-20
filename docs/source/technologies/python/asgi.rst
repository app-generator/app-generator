ASGI
====

ASGI (Asynchronous Server Gateway Interface) is the asynchronous counterpart to WSGI, designed for modern Python web applications that need to handle asynchronous operations. 
While `WSGI <./wsgi.html>`__ was built around a synchronous request-response model, ASGI extends this to support asynchronous code patterns and other protocols like WebSockets, HTTP/2, and Server-Sent Events.

.. include::  /_templates/components/banner-top.rst

Key aspects of ASGI
-------------------

1. It supports asynchronous request handling, allowing servers to process multiple requests concurrently without blocking
2. It's protocol-agnostic, supporting not just HTTP but also WebSockets and other bidirectional communication protocols
3. It enables long-lived connections necessary for real-time applications
4. It maintains backward compatibility with WSGI applications

An ASGI application is a callable that:
- Takes three parameters: scope (connection information), receive (async function to receive messages), and send (async function to send messages)
- Is typically defined using Python's async/await syntax

Popular ASGI frameworks and servers include:
- FastAPI
- Django Channels
- Starlette
- Quart
- Uvicorn
- Daphne
- Hypercorn

ASGI is particularly valuable for applications that:
- Need to handle many concurrent connections
- Require real-time features like chat applications or live updates
- Benefit from WebSocket support for bidirectional communication
- Need to perform I/O operations like database queries without blocking the server

The transition from WSGI to ASGI represents the Python web ecosystem's evolution to better support modern web development requirements, especially for real-time and high-performance applications.

.. include::  /_templates/components/footer-links.rst
