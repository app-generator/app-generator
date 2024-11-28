:og:description: Internationalization and Localization in FastAPI - A practical guide

i18n and Localization
=====================

.. title:: Internationalization and Localization in FastAPI - A practical guide
.. meta::
    :description: Learn how to add Internationalization (i18n) and Localization to a FastAPI project  

In today’s increasingly global environment, providing your application in various languages is crucial for reaching a broader audience. 
This is particularly important for services that are meant to cater to diverse user bases across different regions. 
By internationalizing your FastAPI application, you can ensure that users from different parts of the world can engage with your service in their preferred language.

.. include::  /_templates/components/banner-top.rst

In this tutorial, you will learn how to build a FastAPI application that automatically adapts its responses based on the user's language preferences.

What is Internationalization (i18n)?
------------------------------------

Internationalization, commonly abbreviated as **i18n**, refers to the process of designing your application in such a way that it can easily be adapted to different languages and regions without requiring major changes to the underlying code.

This approach sets the foundation for **localization**, which is the actual process of translating content and formatting for specific languages or regions. i18n focuses on preparing the application to support localization easily by handling text translation, date formats, and currency conversions without altering the core code.

Key Differences: i18n vs Localization
-------------------------------------

- **Internationalization (i18n)**: Prepares the software for translation by setting up infrastructure, ensuring that the application can support multiple languages.
- **Localization (l10n)**: The specific adaptation of content, such as translating text and adjusting regional elements, like number formats or cultural references, to fit a particular audience.


Steps to Implement i18n in FastAPI
----------------------------------

1. Set Up a Basic FastAPI Application
*************************************

First, let's create a simple FastAPI app. In the beginning, we will have a basic greeting API that returns a message in English.

.. code-block:: python

   from fastapi import FastAPI
   from pydantic import BaseModel

   app = FastAPI()

   class GreetingResponse(BaseModel):
       message: str

   @app.get("/greetings", response_model=GreetingResponse)
   async def greetings():
       return {"message": "Hello, welcome to our multilingual API!"}

2. Implementing Translation Management
**************************************

To handle translation, we will use the `gettext` library. The goal is to create a class that will manage language settings and provide translated strings based on user preferences.

.. code-block:: python

   import gettext
   from pathlib import Path
   from fastapi import Request

   class TranslationManager:
       """
       A class that manages translations and handles the installation of the
       correct language translation at runtime.
       """

       _instance = None

       def __new__(cls):
           if cls._instance is None:
               cls._instance = super().__new__(cls)
               cls._instance.setup_translation()
           return cls._instance

       def setup_translation(self):
           """ Set up translations with a default language (English). """
           lang = "en"  # Default language is English
           locales_dir = Path(__file__).parent / "locales"
           self.translations = gettext.translation(
               "messages", localedir=locales_dir, languages=[lang], fallback=True
           )
           self.translations.install()

       def translate(self, text: str) -> str:
           """ Return the translated string for the given message. """
           return self.translations.gettext(text)

   async def set_language(request: Request):
       """ Middleware function to set language based on the Accept-Language header. """
       translator = TranslationManager()
       lang = request.headers.get("Accept-Language", "en")
       locales_dir = Path(__file__).parent / "locales"
       translator.translations = gettext.translation(
           "messages", localedir=locales_dir, languages=[lang], fallback=True
       )
       translator.translations.install()

   def _(text: str) -> str:
       """ Shortcut function to access translation for a given string. """
       translator = TranslationManager()
       return translator.translate(text)

3. Create Middleware to Handle Language Preference
**************************************************

We will now create custom middleware that reads the `Accept-Language` header from each incoming request. This will allow the application to serve content in the user's preferred language.

.. code-block:: python

   from fastapi import Request
   from starlette.middleware.base import BaseHTTPMiddleware
   from i18n import set_language

   class LanguageMiddleware(BaseHTTPMiddleware):
       """
       Middleware that checks the 'Accept-Language' header and sets the appropriate
       language for the response.
       """
       async def dispatch(self, request: Request, call_next):
           await set_language(request)
           response = await call_next(request)
           return response

4. Integrating i18n in the FastAPI Application
**********************************************

Now that we have the translation management and middleware ready, let's integrate everything into the FastAPI app. This will involve adding the custom middleware to the app and updating our `/greetings` endpoint to return a translated message.

.. code-block:: python

   from fastapi import FastAPI
   from pydantic import BaseModel
   from i18n import _
   from middleware import LanguageMiddleware

   app = FastAPI()

   # Add language middleware to handle language preference
   app.add_middleware(LanguageMiddleware)

   class GreetingResponse(BaseModel):
       message: str

   @app.get("/greetings", response_model=GreetingResponse)
   async def greetings():
       # Use the translation function to get the greeting in the appropriate language
       return {"message": _("Hello, welcome to our multilingual API!")}

5. Set Up Translation Files
***************************

Translation files are essential to manage the actual content of the translations:

- **.pot (Portable Object Template)**: The source file containing all the strings in your application that need translation.
- **.po (Portable Object)**: The translated files for a specific language.
- **.mo (Machine Object)**: Compiled versions of the .po files, used by the application to provide the translations at runtime.

Now, we need to set up our translation files. First, we create the necessary directories and extract translatable strings.

- **Create the locales directory**:

  .. code-block:: bash

     mkdir locales

- **Extract translatable strings**:

  .. code-block:: bash

     pybabel extract -o locales/messages.pot .

- **Generate .po files for each language**:

  .. code-block:: bash

     pybabel init -i locales/messages.pot -d locales -l en
     pybabel init -i locales/messages.pot -d locales -l fr
     pybabel init -i locales/messages.pot -d locales -l de

- **Translate the messages**:

  Edit the `.po` files and provide translations for each string.

- **Compile the .po files**:

  .. code-block:: bash

     pybabel compile -d locales

6. Testing the Multilingual API
*******************************

Now, let's test the FastAPI app by sending requests with different `Accept-Language` headers.

- **Request in English**:

  .. code-block:: bash

     curl -X 'GET' 'http://127.0.0.1:8000/greetings' -H 'Accept-Language: en'

  Response: `{"message": "Hello, welcome to our multilingual API!"}`

- **Request in French**:

  .. code-block:: bash

     curl -X 'GET' 'http://127.0.0.1:8000/greetings' -H 'Accept-Language: fr'

  Response: `{"message": "Bonjour, bienvenue dans notre API multilingue!"}`

Conclusion
----------

By following this guide, you have successfully internationalized your FastAPI application. 
By using the `Accept-Language` header, your app now serves multilingual responses, enhancing the user experience for global users. 

This makes your API more accessible and capable of scaling across diverse regions and languages.

.. include::  /_templates/components/footer-links.rst
