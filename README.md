# [AppSeed](https://appseed.us/) v2

The new version of [AppSeed](https://appseed.us/) - Generate, Update legacy code, inject new modules, auto-healing, AI, deployment automation (any cloud provider: AWS, DO, Azure), Docker, k8s.  

> LIVE Demo: https://appseed-v2.onrender.com/
 
<br />

## Features

- Social login: GitHub
- Marketplace: list current items
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

## LICENSE

[@EULA](./LICENSE.md)

<br />

---
Crafted and released by [AppSeed](https://appseed.us/) 
