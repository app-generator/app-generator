Testing FastAPI 
===============

.. include::  /_templates/components/banner-top.rst


The document provides an in-depth overview of testing FastAPI applications, including handling asynchronous endpoints, dependency overrides, background tasks, and mocking external services. FastAPI's design makes it highly suitable for efficient and reliable testing.

Prerequisites
-------------

Ensure you have the following libraries installed:

- `fastapi` - for building the application.
- `pytest` - a popular testing framework.
- `httpx` - for making async HTTP requests.
- `pytest-asyncio` - to support asynchronous tests in `pytest`.

Install these with:

.. code-block:: bash

    pip install fastapi pytest httpx pytest-asyncio

The Project Structure
---------------------

Below is a simple project structure for testing a FastAPI application:

.. code-block:: text

    my_fastapi_app/
    ├── main.py                # Main application file
    ├── test_main.py           # Test file for application tests

Sample FastAPI Application
--------------------------

Here's a sample FastAPI application with basic routes and dependency injection in `main.py`:

.. code-block:: python

    # main.py
    from fastapi import FastAPI, Depends, HTTPException
    from pydantic import BaseModel

    app = FastAPI()

    class Item(BaseModel):
        name: str
        description: str

    fake_items_db = {"item123": {"name": "item123", "description": "A test item"}}

    def get_item(item_id: str):
        item = fake_items_db.get(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    @app.get("/")
    def read_root():
        return {"message": "Hello, World!"}

    @app.get("/items/{item_id}")
    def read_item(item_id: str, item: dict = Depends(get_item)):
        return item

    @app.post("/items/")
    def create_item(item: Item):
        fake_items_db[item.name] = item.dict()
        return item

Writing Basic Tests
-------------------

Using FastAPI's `TestClient` and `pytest`, create a `test_main.py` file for tests. Here's how to write basic tests for the endpoints defined in `main.py`:

.. code-block:: python

    # test_main.py
    import pytest
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)

    def test_read_root():
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, World!"}

    def test_create_item():
        response = client.post("/items/", json={"name": "bar", "description": "A new item"})
        assert response.status_code == 200
        assert response.json() == {"name": "bar", "description": "A new item"}

    def test_read_item():
        response = client.get("/items/item123")
        assert response.status_code == 200
        assert response.json() == {"name": "item123", "description": "A test item"}

    def test_item_not_found():
        response = client.get("/items/notfound")
        assert response.status_code == 404
        assert response.json() == {"detail": "Item not found"}

Testing Asynchronous Endpoints
------------------------------

For asynchronous endpoints, `pytest-asyncio` and `httpx` allow you to run async tests. This example modifies `test_main.py` with an async test:

.. code-block:: python

    import pytest
    from httpx import AsyncClient
    from main import app

    @pytest.mark.asyncio
    async def test_async_read_root():
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.get("/")
            assert response.status_code == 200
            assert response.json() == {"message": "Hello, World!"}

Testing with Dependency Overrides
---------------------------------

Testing with dependency overrides allows you to control dependencies in a test environment. Here, we override the `get_item` dependency to return a fixed value:

.. code-block:: python

    from main import app, get_item

    def override_get_item(item_id: str):
        return {"name": "test_item", "description": "Mocked item"}

    app.dependency_overrides[get_item] = override_get_item

    def test_dependency_override():
        response = client.get("/items/item123")
        assert response.status_code == 200
        assert response.json() == {"name": "test_item", "description": "Mocked item"}



Testing Error Responses
-----------------------

Check that error handling functions correctly by triggering specific errors and verifying response messages:

.. code-block:: python

    def test_item_not_found():
        response = client.get("/items/nonexistent")
        assert response.status_code == 404
        assert response.json() == {"detail": "Item not found"}

Mocking External Service Calls
------------------------------

When endpoints rely on external APIs, mock these calls to avoid dependency on external systems.

Note: This following test will fail because There is No module named 'main.external_service', its just to show how we can mock external service, like 'stripe api, smtp or etc.'
.. code-block:: python

    from unittest.mock import patch
    from main import app

    @patch("main.external_service.get_data")

    def test_external_service_call(mock_get_data):
        mock_get_data.return_value = {"key": "mocked_data"}
        response = client.get("/items/external")
        assert response.status_code == 200
        assert response.json() == {"key": "mocked_data"}

How to Run Your Tests
---------------------

To execute your tests, use `pytest` from the command line within your project directory. This command will automatically discover and run all test files prefixed with `test_`:

.. code-block:: bash

    pytest

For more detailed output, you can run:

.. code-block:: bash

    pytest -v

This provides information on each test's pass/fail status. To run specific tests or test files, specify the file path:

.. code-block:: bash

    pytest test_main.py

After executing, `pytest` will display results in the terminal, detailing the success or failure of each test.

Sample Test Output
------------------

Upon running tests with `pytest`, you should see output similar to:

.. code-block:: text

    =========================== test session starts ============================
    collected 5 items

    test_main.py .....                                                      [100%]

    ============================ 5 passed in 0.42s ============================

Conclusion
----------

Testing FastAPI applications involves various techniques, from simple endpoint testing to handling asynchronous code, dependencies, and mocking external APIs. By using `pytest`, `httpx`, and FastAPI's testing tools, you can create comprehensive tests that ensure the reliability and maintainability of your application.



.. include::  /_templates/components/footer-links.rst
