Security Best Practices
=======================
Security is essential for any web application, and with FastAPI's simplicity and power, following best practices can ensure your API remains robust and resilient against threats. 
This guide will walk you through key security concepts tailored for FastAPI, covering everything from authentication and encryption to best practices for deployment.

.. include::  /_templates/components/banner-top.rst

Secure Authentication
=====================

OAuth2 with JWT (JSON Web Tokens)
---------------------------------

JWT (JSON Web Tokens) are widely used for secure authentication in APIs. They are compact, easy to verify, and allow stateless sessions, which is ideal for distributed systems.
JWTs provide a secure, token-based authentication approach where tokens are issued for users after they log in. These tokens can then be sent with each request to verify the user's identity.

**How to Implement**: FastAPI supports OAuth2, allowing you to create a token endpoint where users can obtain their tokens.

.. code-block:: python

    from fastapi import Depends, FastAPI, HTTPException, status
    from fastapi.security import OAuth2PasswordBearer
    import jwt
    app = FastAPI()
    # Defines where clients send their username & password to get a token
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    def verify_token(token: str = Depends(oauth2_scheme)):
        """
        Decodes the JWT token to verify it.
        Raises an error if the token is invalid or expired.
        """
        try:
            # Decode the token with the secret key
            payload = jwt.decode(token, "your-secret-key", algorithms=["HS256"])
            return payload  # Return the decoded user data if valid
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    @app.get("/secure-data")
    async def secure_route(token_data: dict = Depends(verify_token)):
        return {"message": "Access granted", "token_data": token_data}

**Token URL**: `OAuth2PasswordBearer(tokenUrl="token")` tells FastAPI that clients will send their username and password to `/token` to receive a JWT.

**Token Verification**: The `verify_token` function decodes the JWT using a secret key:
- If the token is valid, it returns the decoded user information.
- If the token is expired or invalid, it raises a 401 Unauthorized error.

**Secured Route**: In the `/secure-data` endpoint, we use `verify_token` as a dependency, allowing access only if the token is valid. This ensures that users must be authenticated to access the endpoint.


Password Hashing
----------------

**Use Secure Hashing**: Avoid storing passwords as plain text. FastAPI's dependency injection can be leveraged to add a password hashing mechanism using libraries like `passlib` with bcrypt or Argon2.

**Salting**: Ensure each password hash is unique by salting it (adding random data before hashing).

.. code-block:: python

    from passlib.context import CryptContext

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(password: str):
        return pwd_context.hash(password)

    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)


API Permissions & Access Control
================================


Role-Based Access Control (RBAC)
--------------------------------

**Define Roles**: Define different access levels (e.g., admin, user, guest) to control access to endpoints.

**Implementation**: Use FastAPI's dependency injection to enforce permissions based on user roles.

.. code-block:: python

    from fastapi import Depends, HTTPException, status

    def get_current_user_role():
        # Example role fetching logic
        return "admin"

    def admin_only(user_role: str = Depends(get_current_user_role)):
        if user_role != "admin":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")

    @app.get("/admin-only", dependencies=[Depends(admin_only)])
    async def admin_route():
        return {"message": "Welcome Admin"}



Data Validation & Injection Protection
======================================

Data Validation with Pydantic
-----------------------------

FastAPI uses Pydantic for data validation and settings management, making it straightforward to enforce constraints and ensure your data is clean and safe from the start.
Validating user inputs can significantly reduce the risks of injection attacks or malformed data entering your application.

.. code-block:: python

    from fastapi import FastAPI
    from pydantic import BaseModel, constr, PositiveInt

    app = FastAPI()

    class User(BaseModel):
        username: constr(min_length=3, max_length=30)
        age: PositiveInt
        email: constr(regex=r'^[\w\.-]+@[\w\.-]+\.\w{2,}$')

    @app.post("/users/")
    async def create_user(user: User):
        return user

**String Length and Regex**: Enforce minimum and maximum lengths for strings or use regex patterns to validate formats (e.g., email addresses).

**Numeric Validation**: Use Pydantic's types to set constraints on numeric values, such as requiring positive integers.

Preventing Injection Attacks
----------------------------

**SQL Injection**: Avoid direct SQL queries with user input. Use an ORM like SQLAlchemy and parameterized queries to mitigate SQL injection risks.

.. code-block:: python

    from sqlalchemy.orm import Session
    from fastapi import Depends

    def get_user_by_username(db: Session, username: str):
        return db.execute("SELECT * FROM users WHERE username = :username", {"username": username}).fetchone()



How to secure FastAPI API against CSRF
======================================

Cross-Site Request Forgery (CSRF) attacks can be mitigated with CSRF tokens or by using secure HTTP-only cookies for stateful APIs.

.. code-block:: python

    from fastapi import FastAPI, Depends, HTTPException
    from starlette.middleware.csrf import CSRFMiddleware

    app = FastAPI()
    app.add_middleware(CSRFMiddleware, secret="your-secret-key")

    @app.post("/protected-endpoint")
    async def protected(data: dict, csrf_protection: bool = Depends()):
        return {"message": "CSRF protected endpoint"}


Secure CORS (Cross-Origin Resource Sharing)
-------------------------------------------

**Restrict Origins**: Only allow trusted origins to interact with your API. Use FastAPI's `CORSMiddleware` to enforce specific origin policies.

.. code-block:: python

    from fastapi.middleware.cors import CORSMiddleware

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["https://trusted-domain.com"],
        allow_credentials=True,
        allow_methods=["GET", "POST"],
        allow_headers=["Authorization"],
    )



Rate Limiting and DDoS Protection
=================================

Implement Rate Limiting with `fastapi-limiter`
----------------------------------------------


**Why Rate Limiting?** Protect your application from abuse and brute-force attacks. `fastapi-limiter` is a library specifically for FastAPI that can enforce rate limits with Redis.

.. code-block:: python

    from fastapi import FastAPI
    from fastapi_limiter import FastAPILimiter
    from fastapi_limiter.depends import RateLimiter
    import aioredis

    app = FastAPI()

    @app.on_event("startup")
    async def startup():
        redis = await aioredis.create_redis_pool("redis://localhost")
        await FastAPILimiter.init(redis)

    @app.get("/limit", dependencies=[Depends(RateLimiter(times=5, seconds=60))])
    async def limited_access():
        return {"message": "This endpoint is rate-limited"}


Conclusion
==========

Securing your FastAPI application is a combination of using built-in tools, third-party libraries, and following good practices. 

By implementing these security measures, you'll reduce vulnerabilities and create a safer experience for your users. 
FastAPI's design helps enforce security, but the responsibility is ultimately on developers to follow these best practices diligently.

With FastAPI, staying secure doesn't have to be a chore, it can be a streamlined part of your development workflow, building confidence and reliability in your application.


.. include::  /_templates/components/footer-links.rst