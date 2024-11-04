Working with Webhooks 
=====================

When building APIs or microservices, integrating webhooks can enable external systems to send real-time updates. This guide will walk through implementing webhooks in a FastAPI application, covering project structure, key design choices, and a complete working example. 

.. include::  /_templates/components/banner-top.rst

Setting Up the Project Structure
--------------------------------

Starting with a FastAPI project that’s organized for easy extensibility is essential. Create the following project structure::

    /webhook_project
    │
    ├── main.py
    ├── webhook_handler.py
    ├── dependencies.py
    ├── models.py
    ├── database.py
    └── __init__.py

- **main.py**: The entry point of the application.
- **webhook_handler.py**: Handles incoming webhook requests.
- **dependencies.py**: Manages shared dependencies like authentication checks or database connections.
- **models.py**: Defines any necessary data models.
- **database.py**: Manages database connections and ORM setup.

This modular setup ensures clarity and maintainability, especially as your project grows.

Database and Models Setup
-------------------------

First, we’ll configure the database connection and create models for logging webhook events.

**database.py**

.. code-block:: python

    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker

    DATABASE_URL = "sqlite:///./test.db"

    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

Here, we use SQLite for simplicity, but you can swap it out for any supported database. The ``SessionLocal`` object will be used to interact with the database.

**models.py**

.. code-block:: python

    from sqlalchemy import Column, Integer, String, JSON
    from .database import Base

    class WebhookEvent(Base):
        __tablename__ = "webhook_events"
        
        id = Column(Integer, primary_key=True, index=True)
        event_type = Column(String, index=True)
        payload = Column(JSON)

``WebhookEvent`` models the incoming webhook data, storing the event type and payload for auditing or debugging purposes. JSON columns are ideal for flexible, unstructured data from webhook payloads.

Handling Webhooks in FastAPI
----------------------------

FastAPI makes handling incoming HTTP requests straightforward. Let’s configure a webhook endpoint to accept and process events.

**webhook_handler.py**

.. code-block:: python

    from fastapi import APIRouter, Request, Depends, HTTPException
    from sqlalchemy.orm import Session
    from .database import SessionLocal
    from .models import WebhookEvent

    router = APIRouter()

    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    @router.post("/webhook")
    async def handle_webhook(request: Request, db: Session = Depends(get_db)):
        try:
            payload = await request.json()
            event_type = payload.get("type")
            
            if not event_type:
                raise HTTPException(status_code=400, detail="Event type missing from payload")
            
            webhook_event = WebhookEvent(event_type=event_type, payload=payload)
            db.add(webhook_event)
            db.commit()
            
            return {"message": "Webhook received successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

The ``handle_webhook`` endpoint uses FastAPI’s dependency injection to get a database session. It extracts and validates the webhook payload, then logs it in the database. If the payload lacks an event type, it returns a 400 error, ensuring proper validation.

Dependency Management
---------------------

Centralizing common dependencies like database connections improves code readability and maintainability. The ``get_db`` function creates a database session and ensures it closes correctly, even if an exception occurs.

Integrating with main.py
------------------------

Finally, integrate everything into your main application file.

**main.py**

.. code-block:: python

    from fastapi import FastAPI
    from .webhook_handler import router as webhook_router
    from .database import Base, engine

    app = FastAPI()

    # Initialize database tables
    Base.metadata.create_all(bind=engine)

    app.include_router(webhook_router)

This setup initializes your database and includes the webhook router. Using ``Base.metadata.create_all`` ensures tables are created before handling any requests.

Testing and Running Your Webhook Listener
-----------------------------------------

To run the application, use::

    uvicorn main:app --reload

With the server running, you can test your webhook endpoint using tools like ``curl`` or Postman.

**Example ``curl`` Request**

.. code-block:: bash

    curl -X POST "http://localhost:8000/webhook" \
        -H "Content-Type: application/json" \
        -d '{"type": "user.created", "data": {"id": 123, "name": "John Doe"}}'

This command simulates a webhook payload. The FastAPI app will log this event in the database.

Conclusion
----------

This tutorial has shown how to set up and handle webhooks using FastAPI, from structuring the project to logging incoming events. While simple, this approach can be scaled to include more complex validation, authentication, or event handling workflows. Future improvements could focus on implementing retries or handling webhook failures gracefully, depending on the reliability requirements of your service.
  

.. include::  /_templates/components/footer-links.rst
