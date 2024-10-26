DRF Security
============

Using Django REST Framework (DRF) to build an API offers you the possibility to integrate many authentication and permission tools. 
Let`s quickly discuss the pros and cons of the most popular ones.

.. include::  /_templates/components/banner-top.rst

Djoser
------

Djoser simplifies user authentication and authorization in DRF by providing a set of endpoints for managing user login, registration, password reset or changes, and a lot more.

**Pros:**

- Easy to implement and comes with pre-built endpoints for user management.
- Supports token-based and JWT authentication out of the box.
- Built-in features like password reset, email verification, and account activation.

**Cons:**

- May require customization for complex user management workflows.

The Djoser package is useful when you need a quick basic token authentication flow with minimal setup.

**Coding Sample**

An integration sample of Djoser, DRRF and django can be found in this documentation page: `Django & DRF Sample <./drf-sample.html>`__ 

Django Rest Simple JWT
----------------------

Django Rest Simple JWT offers stateless authentication using JSON Web Tokens (JWT), making it a popular and safe choice for DRF APIs.

**Pros:**
  
- Stateless, so no need to store tokens on the server, which improves scalability.
- JWTs can be used across multiple services and allow for easy session management.
- Supports token refresh and expiration handling.

**Cons:**

- If a token is stolen, it can be used until it expires, posing a security risk.
- Managing token invalidation (e.g., logout) is more complex than session-based methods. However, you can check for solutions on their `docs <https://django-rest-framework-simplejwt.readthedocs.io/en/latest/blacklist_app.html>`_.

This package is ideal for distributed systems or microservices where scalability and stateless authentication are key.

Django Rest API Key
-------------------

Django REST API key is a package that provides API key authentication that is simple and effective.

**Pros:**

- Simple to implement.
- API keys are easy to revoke if compromised.
- Well-suited for machine-to-machine communication.

**Cons:**

- API keys can be easily leaked if not properly secured.
- Lacks advanced features like token expiration or refresh mechanisms.
- Can be slow.

This package is useful when you need to implement an authentication mechanism between two servers.

Django Rest Knox
----------------

Django Rest Knox extends DRF's token authentication, offering more control and security features, such as token expiration and logout functionality.

**Pros:**

- Supports token expiration and rotation.
- Allows token-based user logout, addressing a common issue with token authentication.

**Cons:**

- Requires additional setup to manage token lifecycle effectively.

Django Rest Knox is perfect for applications that already use DRF token-based auth and that need token-based authentication with user logout and session control.

Django OAuth Toolkit
--------------------

The Django OAuth Toolkit provides OAuth2 authentication, which is an industry-standard protocol widely used for secure, delegated access (e.g., third-party logins like Google or Github).

**Pros:**

- OAuth2 is widely adopted and supports various types of clients (e.g., web, mobile).
- Access and refresh tokens provide flexible session management.
- Granular scopes allow fine-tuned permission control.

**Cons:**

- Complex to implement compared to other authentication methods.
- Overhead with setting up and managing an OAuth2 server.

This package is perfect for applications requiring third-party authentication or integrations with external services (e.g., social logins, APIs).

Django Rest Authemail
---------------------

This package provides an authentication method that focuses on using email-based login, providing an easy-to-use solution for users who prefer email-first workflows, such as passwordless logins.

**Pros:**

- Easy for users, reducing friction in the login process.
- Supports passwordless authentication, improving security.
- Encourages the use of email verification for account activation.

**Cons:**

- Users without regular email access may face difficulties.
- Passwordless flow could be less familiar to users expecting traditional username/password login.

Django Rest Authemail is ideal for applications looking to simplify user login and reduce reliance on passwords.

DRF Passwordless
----------------

Passwordless authentication removes the need for passwords, using one-time passwords (OTPs) or magic links for logging in. DRF Passwordless provides methods to implement this authentication system in your DRF app.

**Pros:**

- Enhances security by eliminating the risk of password breaches.
- Improves user experience by reducing the need for password management.
- Supports both email and SMS-based OTPs.

**Cons:**

- Relies on external factors (e.g., email delivery, SMS reliability).
- May require fallback methods if OTPs fail to deliver.

This package is suitable for applications prioritizing security and user convenience by offering a modern login experience using OTPs.


Conclusion
------------

These are the most common tools used for authentication in the DRF ecosystem. Here is a summary if you need to choose:

- **For stateless, and token-based solutions**, use DRF-JWT and Knox.
- **For machine-to-machine or third-party access**, use API Keys or OAuth2.
- **For user-friendly login experiences**, passwordless authentication via DRF Passwordless or Authemail could be interesting.

.. include::  /_templates/components/footer-links.rst
