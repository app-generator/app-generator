Getting Started
===============

**FastAPI** is a powerful and modern web framework for building API with Python 3. 
What It does is that it lets you build APIs lightning fast and with boatloads of clarity, high performance code and provide support for asynchronous programming. Of course however like all tools, it does have some downsides.

- 👉 `FastAPI Starter <https://github.com/app-generator/core-fastapi>`__ - Free Coding Sample 
- 👉 Get `Support <https://app-generator.dev/ticket/create/>`__ via email and Discord 

This document dives into why FastAPI is a top choice for building APIs, along with some of its drawbacks. Plus, this will guide you through creating a simple, secure API with FastAPI, so you can see its power in action!

.. include::  /_templates/components/banner-top.rst

Why Using FastAPI
-----------------

- **Performance**
    FastAPI is constructed with Starlette in the web portion and Pydantic concerning the data - parts related.The two are highly optimized libraries.Therefore, FastAPI performance is closed to that
    It is excellent for applications requiring high throughput or immediate processing, since it can process huge numbers of intuition sparsely.

- **Type Hints for Validation and Documentation**
    FastAPI will instantiate live API documentation from your codebase using Swagger UI and ReDoc out-of-the-box.
    Thanks to Python's type hints, FastAPI provides automatic request validation and serializes/deserializes incoming and outgoing data from unauthorized access.
- **Easy to Use**
    FastAPI is developer-friendly, focusing on simplicity while leveraging Python's modern features. You can create APIs production-ready in literally just a few lines of code. It won't even take up that much space on your hard disk! Just how easy can this be?
    You get automatic validation of incoming requests, saving definitional work, which may reduce the number of bugs related to incorrect inputs.

- **Asynchronous Support**
    FastAPI is designed with Asynchronous programming in mind, making it easy to work with async I/O operations. This is crucial for applications that need non-blocking services, such as interacting with multiple databases or coping with large amounts of real-time data.

- **Built-in Security and Authentication**
    MiToT recognises OAuth2 and JWT verification by default. In addition, using FastAPI, it can be implemented CORS policies. This not only relieves the burden of workload on your servers but takes the sting out of accessing your APIs illegally.

Cons Of FastAPI
---------------

- **Can't manage bigger codebases**.
    If your application is small then you might not need this, but as the project scales to becoming a giant web app with more and more routes , managing all these manually can become painful.

- **Support for asynchronous can get complicated**.
    While there are asynchronous functions (async/await) inside FastAPI, using them could require some know-how. If used incorrectly, async can become a performance killer — or just very confusing to debug!

- **Web Projects (Non-API) Only Supported to a Limited Degree**.
    While FastAPI is very good at what it does (i.e. API), dealing with full-fledged web applications and server-side rendering or session handling can be something else entirely! But for these types of use cases, Django could be betterfit.

- **Handling Validation Errors in FastAPI**.
    My worst experience while working with FastAPI was handling request validations.FastAPI uses Pydantic for validation and there isn't an obvious way to how we can modify the output of a validation error from pydantic into our response which is where ErrorResponse class comes to play. RequestValidationError is actually an object with its own set of predefined messages which by default will return those messages instead, unlike in the automatically easier example above; so it can be limiting sometimes if you wish to customize them. Either you have to use the default messages by Pydantic or create your own custom validator. Here is an example,


.. code-block:: python

    app = FastAPI()

    class ExampleDTO(BaseModel):
        data: str = Field(min_length=3, description="Data must be at least 3 characters long",
                          title="Custom validation message")

    @app.post("/submit")
    async def submit_data(request: ExampleDTO):
        return {"message": "Data received successfully"}

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return PlainTextResponse(str(exc.errors()), status_code=400)

    In this case, exc. errors() will return a list of validation errors with Pydantic' predefined messages, and there is no easy way of directly passing custom messages to the response from Pydantic validation you have set as description or title fields. Error messages are something that you can normally only set custom through a manual validator or by overriding default behavior.

- **Crowded Main File**.
    In FastAPI, everything route-wise and exception-wise is connected to the FastAPI app directly, making messy main. py file as the project grows. 
    Keeping many routers or exceptions in one file can be hard to maintain and scale. Although, you can refactor to decorate the application parts more explicitly with routers, errors and utilities.

- **Bad structure for larger projects**.
    Nothing built-in: FastAPI doesn't have any built in way for structuring large applications
    The Problem: As the project grows, our own challenges on how to keep a cleaner and scalable architecture. 
    Unlike frameworks like Django or Rails, FastAPI does not natively support feature-rich methods for structuring codebase abstraction across complex functionalities 
    including managing dependencies and business logic over various modules. 
    This requires developers to implement their own structure, often generating inconsistencies and more complexity if the project grows.

- **Lack of Mature Ecosystem**.
    FastAPI is not as mature as Django or Flask yet. This means there is not a lot of community and ecosystem as in terms of 3rd party packages, plugins or detailed tutorials.


Code a simple API
-----------------

This guide will walk you through building a simple FastAPI project that serves a secure API using JWT for authentication.

Prerequisites
*************

- Python 3.x installed on your system.
- Install FastAPI, Uvicorn, and other dependencies by running:

.. code-block:: bash

    pip install fastapi uvicorn
    pip install "passlib[bcrypt]"
    pip install pyjwt[crypto]
    pip install pydantic python-jose python-multipart py-bcrypt

Project Structure
*****************

.. code-block:: bash

   project_folder
   ├── app.py
   ├── auth.py
   └── models.py

Create models.py file
*********************

.. code-block:: python

    class User(BaseModel):
    username: str
    password: str


    class UserInDB(User):
        hashed_password: str


    class Token(BaseModel):
        access_token: str
        token_type: str


Create auth.py file
*******************

.. code-block:: python

    import secrets
    from datetime import datetime, timedelta
    from typing import Union

    from jose import JWTError, jwt
    from passlib.context import CryptContext

    SECRET_KEY = 'secretkey'

    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    # Password context for bcrypt
    # Set up the password hashing context
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


    # Function to hash passwords
    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)


    # Function to verify passwords
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)


    def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


    def decode_token(token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise JWTError("Invalid credentials")
            return username
        except JWTError:
            return None

Create app.py file
******************

.. code-block:: python

    from fastapi import FastAPI, Depends, HTTPException, status
    from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
    from auth import create_access_token, verify_password, get_password_hash, decode_token
    from models import UserInDB, Token
    from datetime import timedelta

    app = FastAPI()

    # For OAuth2 scheme (token-based authentication)
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    # Example in-memory user database (replace with real DB in production)
    fake_users_db = {
        "john": {
            "username": "john",
            "hashed_password": get_password_hash("secret"),
            "password": 'secret'
        }
    }


    # Dependency to get the current user based on token
    def get_current_user(token: str = Depends(oauth2_scheme)):
        username = decode_token(token)
        if not username:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        user = fake_users_db.get(username)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return UserInDB(**user)


    # Route to get a token (authentication)
    @app.post("/token", response_model=Token)
    async def login(form_data: OAuth2PasswordRequestForm = Depends()):
        user = fake_users_db.get(form_data.username)
        if not user or not verify_password(form_data.password, user["hashed_password"]):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
        access_token = create_access_token(data={"sub": form_data.username}, expires_delta=timedelta(minutes=30))
        return {"access_token": access_token, "token_type": "bearer"}


    # A secure endpoint that requires token authentication
    @app.get("/secure-data")
    async def get_secure_data(current_user: UserInDB = Depends(get_current_user)):
        return {"msg": f"Hello, {current_user.username}. You have access to secure data!"}


    # Public route (no authentication required)
    @app.get("/public")
    async def public_route():
        return {"msg": "This is a public route!"}


Start the FastAPI Project
*************************

.. code-block:: python

    uvicorn app:app --reload

Endpoint
--------

At this point, we have:

- **A public endpoint (/public) that anyone can access**.

- **A secure endpoint (/secure-data) that requires a valid JWT token**.

- **Getting a Token**.

    You can import that directly for testing.

.. code-block:: python

    curl -X POST "http://127.0.0.1:8000/token" -H "Content-Type: application/x-www-form-urlencoded" -d "username=john&password=secret"

.. include::  /_templates/components/footer-links.rst
