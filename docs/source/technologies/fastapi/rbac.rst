:og:description: Role-Based Access Control (RBAC) in FastAPI

Role-Based Access
=================

.. title:: Role-Based Access Control (RBAC) in FastAPI
.. meta::
    :description: Learn how to implement Role-Based Access Control in FastAPI - a practical guide 


.. include::  /_templates/components/banner-top.rst

**Role-Based Access Control (RBAC)** enables secure resource access based on user roles and their associated permissions.
This guide demonstrates a practical RBAC implementation in **FastAPI**, including user authentication, token management, and permission validation.

Key Features
------------
- JWT-based user authentication.
- Role and permission management using `OAuth2PasswordBearer`.
- Dynamic permission enforcement with reusable dependencies.

Prerequisites
-------------
1. Install the required libraries:
   .. code-block:: bash

       pip install fastapi uvicorn bcrypt pyjwt

2. Set up a basic understanding of OAuth2 and FastAPI dependency injection.

Implementation
--------------

1. **User Data and Models**
   Users are associated with roles and permissions. In a real-world app, this data would be stored in a database.

   .. code-block:: python

       import datetime
       from typing import List, Dict
       from fastapi import FastAPI, Depends, HTTPException, status
       from fastapi.security import OAuth2PasswordBearer
       from pydantic import BaseModel
       import jwt
       import bcrypt

       app = FastAPI()

       # Simulated in-memory user data
       users_db = [
           {
               "id": 1,
               "username": "admin",
               "hashed_password": bcrypt.hashpw(b"admin123", bcrypt.gensalt()).decode(),
               "roles": ["admin"],
               "permissions": ["read:items", "write:items", "read:users"]
           },
           {
               "id": 2,
               "username": "editor",
               "hashed_password": bcrypt.hashpw(b"editor123", bcrypt.gensalt()).decode(),
               "roles": ["editor"],
               "permissions": ["read:items", "write:items"]
           },
           {
               "id": 3,
               "username": "viewer",
               "hashed_password": bcrypt.hashpw(b"viewer123", bcrypt.gensalt()).decode(),
               "roles": ["viewer"],
               "permissions": ["read:items"]
           }
       ]

       class User(BaseModel):
           username: str
           roles: List[str]
           permissions: List[str]

2. **Authentication and Token Handling**
   Authenticate users and issue JWT tokens with payloads containing role and permission information.

   .. code-block:: python

       oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

       def authenticate_user(username: str, password: str) -> User:
           for user in users_db:
               if user["username"] == username and bcrypt.checkpw(password.encode(), user["hashed_password"].encode()):
                   return User(username=user["username"], roles=user["roles"], permissions=user["permissions"])
           raise HTTPException(
               status_code=status.HTTP_401_UNAUTHORIZED,
               detail="Invalid username or password"
           )

       def create_access_token(data: dict) -> str:
           payload = {
               "sub": data["username"],
               "roles": data["roles"],
               "permissions": data["permissions"],
               "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
           }
           token = jwt.encode(payload, "secret_key", algorithm="HS256")
           return token

       class LoginRequest(BaseModel):
        username: str
        password: str

        @app.post("/login")
        def login(request: LoginRequest):
            user = authenticate_user(request.username, request.password)
            token = create_access_token(user.dict())
            return {"access_token": token, "token_type": "bearer"}

3. **Permission Checker**
   A custom dependency to validate required permissions before accessing protected resources.

   .. code-block:: python

       class PermissionChecker:
           def __init__(self, required_permissions: List[str]) -> None:
               self.required_permissions = required_permissions

           def __call__(self, token: str = Depends(oauth2_scheme)) -> None:
               try:
                   payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
                   user_permissions = payload.get("permissions", [])
                   for perm in self.required_permissions:
                       if perm not in user_permissions:
                           raise HTTPException(
                               status_code=status.HTTP_403_FORBIDDEN,
                               detail=f"Permission '{perm}' is required"
                           )
               except jwt.ExpiredSignatureError:
                   raise HTTPException(status_code=401, detail="Token has expired")
               except jwt.DecodeError:
                   raise HTTPException(status_code=401, detail="Invalid token")

4. **Secure API Endpoints**
   Endpoints are secured based on user roles and permissions.

   .. code-block:: python

       @app.get("/items", dependencies=[Depends(PermissionChecker(["read:items"]))])
       def read_items():
           return {"message": "You can view items"}

       @app.post("/items", dependencies=[Depends(PermissionChecker(["write:items"]))])
       def create_item():
           return {"message": "You can create items"}

       @app.get("/users", dependencies=[Depends(PermissionChecker(["read:users"]))])
       def read_users():
           return {"message": "You can view users"}

Using curl Commands
-------------------
Here are examples of curl commands to interact with the API endpoints:

1. **Login**:
   .. code-block:: bash

       curl -X POST "http://127.0.0.1:8000/login" \
       -H "Content-Type: application/json" \
       -d '{"username": "admin", "password": "admin123"}'

2. **Get Items**:
   .. code-block:: bash

       curl -X GET "http://127.0.0.1:8000/items" \
       -H "Authorization: Bearer <ACCESS_TOKEN>"

3. **Create Item**:
   .. code-block:: bash

       curl -X POST "http://127.0.0.1:8000/items" \
       -H "Authorization: Bearer <ACCESS_TOKEN>" \
       -H "Content-Type: application/json" \
       -d '{"name": "new item"}'

4. **Get Users**:
   .. code-block:: bash

       curl -X GET "http://127.0.0.1:8000/users" \
       -H "Authorization: Bearer <ACCESS_TOKEN>"

Conclusion
----------
Implementing RBAC in FastAPI provides a robust framework for controlling access to resources based on user roles and permissions. By leveraging JWT for authentication and reusable dependencies for permission checks, this approach ensures security and scalability in real-world applications. With the modular structure demonstrated here, you can adapt the system to fit any application, integrating with databases or external identity providers as needed. This setup not only simplifies role management but also ensures maintainability and clarity as your application grows.

.. include::  /_templates/components/footer-links.rst
