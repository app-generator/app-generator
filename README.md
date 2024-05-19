# [AppSeed](https://appseed.us/) v2

The new version of [AppSeed](https://appseed.us/) - Generate Digital Products, Update legacy code by chat, Inject new modules, Software Auto-healing, AI, Deployment automation (any provider), Docker, K8s. 

> 👉 `LIVE Demo`: https://appseed-v2.onrender.com/
 
<br />

## Features

- Social login: GitHub
- Marketplace: list current items from [AppSeed](https://appseed.us)
- Generator:
  - MVC: Django, NodeJS, Flask, FastAPI
  - Full-Stack: React, Vue with any API Backend
  - API [ manage visually the data ]
  - eCommerce
  - Website
- Deployment options: Render, AppSeed Cloud Digital Ocean, User Provider (AWS, DO, Azure)
- Developer Tools
  - AI introspection to different data sources
  - CSV processing and data extraction
  - CSV to model
- Sections:
  - `product/` -> for products, structure mirrored from AppSeed
    - Sample: https://appseed.us/product/rocket-pro/django/  -> pattern `product/DESIGN/BACKEND/FRONTEND/`
  - `blog/` -> same as Invat_eu
    - https://invat.eu/blog/article-100-5/
  - `docs/` -> only index file at this moment
  - `tools/`-> only index file at this moment
  - `support/`
  - `deploy/` - CI/CD Assistance 
  - `custom-development`
  - `generator/` -> only index file at this moment  
 
<br />

## SPECS

- [SPECS API](https://github.com/app-generator/appseed-v2/blob/main/apps/api/README.md)
- [SPECS Aut](https://github.com/app-generator/appseed-v2/blob/main/apps/auth/README.md)
- [SPECS Blog](https://github.com/app-generator/appseed-v2/blob/main/apps/blog/README.md)
- [SPECS Deploy](https://github.com/app-generator/appseed-v2/blob/main/apps/deploy/README.md)
- [SPECS Docs](https://github.com/app-generator/appseed-v2/blob/main/apps/docs/README.md)
- [SPECS Generator](https://github.com/app-generator/appseed-v2/blob/main/apps/generator/README.md)
- [SPECS Pages](https://github.com/app-generator/appseed-v2/blob/main/apps/pages/README.md)
- [SPECS Products](https://github.com/app-generator/appseed-v2/blob/main/apps/products/README.md)
- [SPECS Tasks](https://github.com/app-generator/appseed-v2/blob/main/apps/tasks/README.md)
- [SPECS DevTools](https://github.com/app-generator/appseed-v2/blob/main/apps/tools/README.md)

<br />

For more input please contact [support](https://appseed.us/support/) using the following: 

- Official Email `support@appseed.us`
- Discord: https://discord.gg/fZC6hup (3k+ members).

<br />

## Stack

- Python/Django
- React
- Docker
- CI/CD - LIVE Deploy on Digital Ocean

<br />

## Manual Build 

> Download the code 

```bash
$ git clone https://github.com/app-generator/appseed-v2.git
$ cd appseed-v2
``` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

> Start the APP

```bash
$ python manage.py createsuperuser # create the admin
$ python manage.py runserver       # start the project
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

## CLI

Once the VENV is activated, we can use the console to interact with the codebase:

> List available commands

```bash
$ python manage.py help 
(Truncated Output)
Type 'manage.py help <subcommand>' for help on a specific subcommand.
Available subcommands:
...
[cli]
    cmd_apps
    cmd_models
    cmd_showcfg
...
```

> List Registered Apps

```bash
$ python manage.py cmd_apps
(Truncated Output)
 APP -> Webpack Loader
 APP -> Administration
 APP -> Authentication and Authorization
 ...
```

> List Registered Models

```bash
$ python manage.py cmd_models
(Truncated Output)
 APP -> Administration
         |- (model) -> <class 'django.contrib.admin.models.LogEntry'>
 APP -> Authentication and Authorization
         |- (model) -> <class 'django.contrib.auth.models.Permission'>
         |- (model) -> <class 'django.contrib.auth.models.Group'>
         |- (model) -> <class 'django.contrib.auth.models.User'>
```

> print Configuration 

```bash
$ python manage.py cmd_showcfg
(Truncated Output)
 Cfg Key: INSTALLED_APPS -> ['webpack_loader', 'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles', 'cli', 'apps.common', 'apps.pages', 'apps.users', 'apps.blog', 'debug_toolbar', 'allauth', 'allauth.account', 'allauth.socialaccount', 'allauth.socialaccount.providers.github', 'allauth.socialaccount.providers.google', 'django_quill']
 Cfg Key: DEBUG -> True
 Cfg Key: USE_TZ -> True
 Cfg Key: ROOT_URLCONF -> core.urls
 Cfg Key: MEDIA_ROOT -> D:\work\appseed-v2\media
 Cfg Key: APPEND_SLASH -> True
 Cfg Key: STATICFILES_FINDERS -> ['django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder']
 Cfg Key: STATICFILES_DIRS -> D:\work\appseed-v2\static
 Cfg Key: STATIC_ROOT -> D:\work\appseed-v2\staticfiles  
```

<br />

## LICENSE

[@EULA](./LICENSE.md)

<br />

---
Crafted and released under [AppSeed](https://appseed.us/) brand by [Sm0ke](https://x.com/Sm0keDev)
