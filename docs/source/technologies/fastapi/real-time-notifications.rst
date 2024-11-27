Real-time Notifications
=======================

.. title:: Real-time Notifications in FastAPI - A Practical Guide 
.. meta::
    :description: Practical steps to implement Real-time Notifications in FastAPI

Real-time notifications are an essential feature in modern web applications. They provide users with instant updates, enhancing user engagement and responsiveness.
This document explains how to implement real-time notifications in a web application using WebSockets with Django and Django Channels.

.. include::  /_templates/components/banner-top.rst

Prerequisites
-------------

Before implementing real-time notifications, ensure the following are installed:

- Python 3.x
- Django
- Django Channels
- Redis (for message queuing)

Step-by-step Implementation
---------------------------

1. **Set Up Django Channels**

To enable real-time communication, install Django Channels:

.. code-block:: bash

    pip install channels

Update the `settings.py` file to include Channels:

.. code-block:: python

    # settings.py
    INSTALLED_APPS = [
        ...,
        'channels',
    ]

    ASGI_APPLICATION = 'myproject.asgi.application'

    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {
                'hosts': [('127.0.0.1', 6379)],
            },
        },
    }

This setup enables Redis for message handling.

2. **Create an ASGI Configuration**

Create an `asgi.py` file for your Django project:

.. code-block:: python

    # asgi.py
    import os
    from django.core.asgi import get_asgi_application
    from channels.routing import ProtocolTypeRouter, URLRouter
    from channels.auth import AuthMiddlewareStack
    from myapp.routing import websocket_urlpatterns

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

    application = ProtocolTypeRouter({
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)
        ),
    })

3. **Set Up WebSocket Routing**

Define WebSocket routes in your app:

.. code-block:: python

    # myapp/routing.py
    from django.urls import path
    from . import consumers

    websocket_urlpatterns = [
        path('ws/notifications/', consumers.NotificationConsumer.as_asgi()),
    ]

4. **Create a Consumer**

Implement a WebSocket consumer to handle notifications:

.. code-block:: python

    # myapp/consumers.py
    import json
    from channels.generic.websocket import AsyncWebsocketConsumer

    class NotificationConsumer(AsyncWebsocketConsumer):
        async def connect(self):
            self.group_name = 'notifications'
            await self.channel_layer.group_add(
                self.group_name,
                self.channel_name
            )
            await self.accept()

        async def disconnect(self, close_code):
            await self.channel_layer.group_discard(
                self.group_name,
                self.channel_name
            )

        async def receive(self, text_data):
            message = json.loads(text_data)['message']
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'send_notification',
                    'message': message
                }
            )

        async def send_notification(self, event):
            await self.send(text_data=json.dumps({
                'message': event['message']
            }))

5. **Send Notifications**

Create a Django view to broadcast notifications:

.. code-block:: python

    # myapp/views.py
    from django.http import JsonResponse
    from channels.layers import get_channel_layer
    from asgiref.sync import async_to_sync

    def send_notification(request):
        channel_layer = get_channel_layer()
        message = request.GET.get('message', 'Default Notification')
        async_to_sync(channel_layer.group_send)(
            'notifications',
            {
                'type': 'send_notification',
                'message': message
            }
        )
        return JsonResponse({'status': 'Notification sent!'})

6. **Test the Application**

Start the development server:

.. code-block:: bash

    python manage.py runserver

Use a WebSocket client (e.g., JavaScript or Postman) to connect to `ws://localhost:8000/ws/notifications/`. 
Send messages through the `send_notification` view and observe real-time updates in the WebSocket client.

Conclusion
----------

This guide demonstrates how to set up real-time notifications using Django Channels and WebSockets. 
This implementation can be extended to other use cases like chat applications, live updates, and dashboards.

.. include::  /_templates/components/footer-links.rst
