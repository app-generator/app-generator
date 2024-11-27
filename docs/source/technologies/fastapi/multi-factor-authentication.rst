Multi-factor Authentication
===========================

.. title:: Multi-factor Authentication (MFA) for FastAPI - A practical guide
.. meta::
    :description: Learn how to implement Multi-factor Authentication in FastAPI - A practical guide

This page explains how to add Multi-factor Authentication (MFA) mechanism to a `FastAPI <./index.html>`__ project.
MFA is a security mechanism that requires users to verify their identity using multiple factors. 

**These factors are typically categorized into**:

1. **Something you know**: A password or PIN.
2. **Something you have**: A smartphone or a hardware token.
3. **Something you are**: Biometrics, such as a fingerprint or facial recognition.

By combining multiple factors, MFA significantly reduces the risk of unauthorized access, even if one factor (e.g., a password) is compromised.

.. include::  /_templates/components/banner-top.rst

**Advantages of MFA**:

- **Enhanced Security**: Even if passwords are stolen, attackers cannot access the system without the additional authentication factor.
- **Reduced Risk of Identity Theft**: MFA makes it harder for attackers to impersonate users.
- **Compliance with Regulations**: Many industries require MFA to comply with standards like GDPR or HIPAA.
- **User Trust**: Implementing MFA shows users that their security is a priority.

This document demonstrates how to implement MFA in a FastAPI application using **PyOTP** for OTP generation and verification.

Overview
--------

This example uses the following:
- **FastAPI**: For building the web application.
- **PyOTP**: For generating and verifying one-time passwords (OTPs).
- **Pydantic**: For data validation.
- **SQLite**: As the database for simplicity (can be replaced with other DB systems).

Step 1: Install Dependencies
----------------------------

Install the required Python libraries using pip:

.. code-block:: bash

    pip install fastapi uvicorn sqlalchemy pyotp sqlite3 pydantic

Step 2: Create the Database
----------------------------

Define a simple SQLite database to store user data.

.. code-block:: python

    from sqlalchemy import create_engine, Column, Integer, String, Boolean
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker

    Base = declarative_base()
    engine = create_engine("sqlite:///mfa_demo.db")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    class User(Base):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True, index=True)
        username = Column(String, unique=True, index=True)
        password = Column(String)
        otp_secret = Column(String)  # Stores the OTP secret
        is_otp_verified = Column(Boolean, default=False)

    Base.metadata.create_all(bind=engine)

Step 3: Implement MFA Logic
---------------------------

1. **Register Users**: Allow users to register and generate a unique OTP secret.
2. **Login**: Validate username and password, and then request OTP.
3. **Verify OTP**: Verify the OTP provided by the user.

.. code-block:: python

    from fastapi import FastAPI, Depends, HTTPException
    from sqlalchemy.orm import Session
    import pyotp

    app = FastAPI()

    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    @app.post("/register")
    def register_user(username: str, password: str, db: Session = Depends(get_db)):
        otp_secret = pyotp.random_base32()
        new_user = User(username=username, password=password, otp_secret=otp_secret)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "User registered!", "otp_secret": otp_secret}

    @app.post("/login")
    def login_user(username: str, password: str, db: Session = Depends(get_db)):
        user = db.query(User).filter(User.username == username).first()
        if not user or user.password != password:
            raise HTTPException(status_code=400, detail="Invalid credentials")
        return {"message": "Login successful, provide OTP"}

    @app.post("/verify-otp")
    def verify_otp(username: str, otp: str, db: Session = Depends(get_db)):
        user = db.query(User).filter(User.username == username).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        totp = pyotp.TOTP(user.otp_secret)
        if not totp.verify(otp):
            raise HTTPException(status_code=400, detail="Invalid OTP")
        user.is_otp_verified = True
        db.commit()
        return {"message": "OTP verified successfully"}

Step 4: Test the Application
----------------------------

1. **Start the Application**:

   Run the FastAPI application using Uvicorn:

   .. code-block:: bash

       uvicorn main:app --reload

2. **Register a User**:

   Use a tool like Postman or cURL to register a new user:

   .. code-block:: json

       POST /register
       {
           "username": "testuser",
           "password": "securepassword"
       }

   Response:

   .. code-block:: json

       {
           "message": "User registered!",
           "otp_secret": "JBSWY3DPEHPK3PXP"
       }

   Use the `otp_secret` to set up an OTP generator, such as Google Authenticator.

3. **Login**:

   Authenticate the user using their username and password:

   .. code-block:: json

       POST /login
       {
           "username": "testuser",
           "password": "securepassword"
       }

   Response:

   .. code-block:: json

       {
           "message": "Login successful, provide OTP"
       }

4. **Verify OTP**:

   Verify the OTP provided by the user:

   .. code-block:: json

       POST /verify-otp
       {
           "username": "testuser",
           "otp": "123456"
       }

   Response:

   .. code-block:: json

       {
           "message": "OTP verified successfully"
       }


Conclusion
----------

This demonstrates a simple implementation of Multi-factor Authentication (MFA) in FastAPI. 
For production-grade applications, ensure to use encrypted passwords (e.g., `bcrypt`) and secure storage mechanisms for secrets and sensitive data.

.. include::  /_templates/components/footer-links.rst
