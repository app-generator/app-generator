:og:description: Multitenancy with FastAPI - A practical guide

Multitenancy
============

.. title:: Multitenancy with FastAPI - A practical guide
.. meta::
    :description: Learn how to implement multitenancy in FastAPI - a production-ready guide

.. include::  /_templates/components/banner-top.rst


Implementing Multi-Tenancy in FastAPI: A Practical Guide
======================================================

This page explains how to implement Multi-Tenancy in a FastAPI project - A Practical Guide. When building software solutions that serve multiple organizations or clients, the need for a multi-tenant architecture arises. 
This allows a single instance of the application to serve different customers, while keeping their data isolated. 

In FastAPI, multi-tenancy can be implemented using different strategies for database isolation and schema management.
This guide will walk you through how to implement multi-tenancy in FastAPI, focusing on the **Single Database, Multiple Schemas** approach. 

We'll use dynamic database configuration, schema separation, and API endpoints to provide an isolated environment for each tenant.

Project Structure
------------------

Here is the recommended structure for the project:

.. code-block:: text

    multi_tenant_fastapi/
    ├── app/
    │   ├── __init__.py
    │   ├── main.py                  # Main application entry point
    │   ├── database.py              # Database connection and schema creation
    │   ├── schemas.py               # Pydantic response models
    │   ├── base_models.py           # Common mixin classes for models
    │   ├── tenant_a/
    │   │   ├── __init__.py
    │   │   ├── models.py            # Tenant-specific models
    │   ├── tenant_b/                # Additional tenant (optional)
    │   │   ├── __init__.py
    │   │   ├── models.py
    │   ├── routers/
    │       ├── __init__.py
    │       ├── tenant.py            # API routing logic
    ├── .env                         # Environment variables
    ├── requirements.txt             # Dependencies
    ├── README.rst                   # Documentation

---

Strategies for Data Isolation
-----------------------------

1. **Multiple Databases**:
   Each tenant has its own database. While this offers the highest isolation, it requires managing multiple database connections and can be more resource-intensive.

2. **Single Database, Shared Schema**:
   All tenants share the same database and schema. Data isolation is achieved through tenant-specific identifiers. This is efficient but requires careful query design to ensure data separation.

3. **Single Database, Multiple Schemas**:
   Each tenant has its own schema within a shared database. This is a balanced approach, providing a high level of data separation without the overhead of managing multiple databases.

For this guide, we will implement the **Single Database, Multiple Schemas** strategy.


Multi-Tenancy Implementation Steps
==================================

1. Setting Up the Database
--------------------------

We’ll use **SQLAlchemy** for ORM-based interactions with the PostgreSQL database. To begin, you’ll need to configure the database connection in your FastAPI app.

**File**: `app/database.py`

.. code-block:: python

    import os
    from sqlalchemy import create_engine, MetaData
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.schema import CreateSchema

    from dotenv import load_dotenv

    load_dotenv()

    # Database connection configuration
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    db_port = int(os.getenv("DB_PORT", 5432))

    SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base = declarative_base()

    def create_schema_if_not_exists(schema_name: str):
        """Create schema if not already present."""
        with engine.connect() as conn:
            conn.execute(CreateSchema(schema_name, if_not_exists=True))
            conn.commit()

2. Define a Dynamic Base Class for Each Tenant
----------------------------------------------

Each tenant will have their own schema, so we need to dynamically generate a base class tied to the tenant's schema. This will allow tenant-specific models to inherit from it.

**File**: `app/database.py`

.. code-block:: python

    def get_base(tenant_name: str):
        """Get a base class tied to a tenant's schema."""
        create_schema_if_not_exists(tenant_name)
        metadata = MetaData(schema=tenant_name)
        return declarative_base(metadata=metadata)

3. Defining Tenant-Specific Models
----------------------------------

We now define tenant-specific models like **`Product`** and **`Order`**. These models will use the schema of the tenant to ensure data isolation.

**File**: `app/tenant_a/models.py`

.. code-block:: python

    from base_models import ProductMixin, OrderMixin
    from database import get_base

    Base = get_base('tenant_a')

    class Product(Base, ProductMixin):
        __tablename__ = 'products'

    class Order(Base, OrderMixin):
        __tablename__ = 'orders'

4. Creating Mixins for Common Model Fields
------------------------------------------

We define mixins to avoid repeating common fields across multiple models. These mixins will be inherited by tenant-specific models.

**File**: `app/base_models.py`

.. code-block:: python

    from sqlalchemy import Column, Integer, String, DateTime, Float

    class ProductMixin:
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String)
        price = Column(Float)
        created_at = Column(DateTime, default=datetime.datetime.utcnow)

    class OrderMixin:
        id = Column(Integer, primary_key=True, index=True)
        product_id = Column(Integer, index=True)
        quantity = Column(Integer)
        total_price = Column(Float)
        order_date = Column(DateTime, default=datetime.datetime.utcnow)

5. Creating the Tables Dynamically
----------------------------------

We use SQLAlchemy’s `metadata.create_all()` method to create the necessary tables in the tenant’s schema. Here’s how you can create the tables for **tenant_a**.

**File**: `app/main.py`

.. code-block:: python

    from tenant_a.models import Base as TenantABase
    from database import engine

    TenantABase.metadata.create_all(bind=engine)

6. Handling Tenant-Specific Routing
----------------------------------

In FastAPI, we need to route requests dynamically based on the tenant. This can be done by using headers to identify the tenant and then loading the appropriate models.

**File**: `app/routers/tenant.py`

.. code-block:: python

    from fastapi import APIRouter, Depends, Header
    from sqlalchemy.orm import Session

    from database import get_db
    from tenant_a.models import Product, Order
    from schemas import Domain  # Enum for domain names

    router = APIRouter()

    @router.get("/products")
    def get_all_products(db: Session = Depends(get_db), domain: Domain = Header(None)):
        # Based on the domain header, select the tenant's schema
        tenant = get_tenant_model(domain)
        products = db.query(tenant.Product).all()
        return products

    @router.get("/orders")
    def get_all_orders(db: Session = Depends(get_db), domain: Domain = Header(None)):
        tenant = get_tenant_model(domain)
        orders = db.query(tenant.Order).all()
        return orders

Summary
-------

In this guide, we implemented multi-tenancy in FastAPI using the **Single Database, Multiple Schemas** strategy. 
By dynamically generating models and schemas for each tenant, we ensured that data is isolated while leveraging the same codebase. 

FastAPI's powerful dependency injection system, SQLAlchemy ORM, and Pydantic models make it easy to manage multi-tenancy effectively.

This approach is scalable, allowing you to easily add new tenants and manage tenant-specific data without altering the core application logic. 
Whether you're building SaaS platforms or managing data for multiple clients, multi-tenancy provides a flexible solution for serving multiple users while maintaining clean data isolation.

.. include::  /_templates/components/footer-links.rst
