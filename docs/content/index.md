---
title         : Rocket Django PRO - Premium Starter
page_info     : Premium Django Starter styled with Tailwind and Flowbite
sidebar_label : Rocket Django PRO
tags          : programming, django
---

# [Rocket Django PRO](https://appseed.us/product/rocket-pro/django/)

Premium Django Starter that incorporates a few modern technologies provided out-of-the-box, at a production-ready level. 
[Rocket PRO](https://appseed.us/product/rocket-pro/django) comes with API (via DRF), Charts, server-side DataTable, Celery for async tasks processing, and Docker support.    

- [Rocket Django PRO](https://rocket-django-pro.onrender.com/) - `LIVE Demo`
- [Rocket Django PRO](https://appseed.us/product/rocket-pro/django/) - `Product Page`

![Rocket Django - Premium Django Starter styled with Tailwind and Flowbite](https://github-production-user-asset-6210df.s3.amazonaws.com/51070104/272299949-6f4a8fd7-7cce-472a-9566-9519db338c7d.gif) 

<br />

## Features

The codebase is shipped with basic features that are usually implemented in most of the projects: 

- Up-to-date Dependencies
- Tailwind/Flowbite Integration via WebPack
- `Extended User Model`
- API via `DRF` 
- Charts
- Charts via React
- Enhanced DataTables
- Media Files Manager 
- `Celery` (async processing)
- Docker

<br />

## System Requirements

- [Python3](https://www.python.org) - the programming language used to code the app
- [GIT](https://git-scm.com) - used to clone the source code from the Github repository
- [NodeJS](https://nodejs.org/) v18.20.0 or above (for Tailwind set up)
- [Docker](https://www.docker.com/) - a popular virtualization software

<br />

## Download Sources 

> Unzip sources or clone the private repository (requires a [purchase](https://appseed.us/product/rocket-pro/django/))

```bash
$ unzip rocket-django-pro.zip
// OR
$ git clone https://github.com/app-generator/priv-rocket-django-pro.git
$ cd rocket-django-pro
```

Once the sources are available in the local filesystem, we can start the project using `Docker` or `manual build`. 

<br />

## Start with `Docker`

```bash
# Optional (kill all existing containers)
$ docker container kill $(docker ps -q) ; docker container rm $(docker ps -a -q) ; docker network prune -f 
# Start the APP
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running. The starter comes with two default users:

- Ordinary user: `test` / `test@appseed.us` / `Pass12__` (the password)
- Django SuperUser (admin): `admin` / `admin@appseed.us` / `Pass12__` (the password)

Once authenticated with the above credentials, the sidebar shows different items. 

<br />

## Manual Build 

> Create `.env` from `env.sample`

```env
DEBUG=False

SECRET_KEY=<STRONG_KEY_HERE>
```

> Install **Django** modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

> Install **Tailwind/Flowbite** (another terminal)

Tested with **Node** `v18.20.0` (use at least this version or above)

```bash
$ npm install
$ npm run dev
$ npx tailwindcss -i ./static/assets/style.css -o ./static/dist/css/output.css --watch # DEVELOPMENT (LIVE reload)
$ npx tailwindcss -i ./static/assets/style.css -o ./static/dist/css/output.css         # PRODUCTION
```

> Migrate DB

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

> `Create Superuser` & Start the [Rocket Django](https://appseed.us/product/rocket/django/) Starter

```bash
$ python manage.py createsuperuser # create the admin
$ python manage.py runserver       # start the project
```

At this point, we can start using the starter.

<br />

## Use MySql 

By default, the starter uses SQLite for persistence. In order to use MySql, here are the steps: 

- Start the MySql Server
- Create a new DataBase
- Create a new user with full privileges over the database 
- Install the MySql Python Driver (used by Django to connect)
  - `$ pip install mysqlclient`
- Edit the `.env` with the SQL Driver Information & DB Credentials 

```env

DB_ENGINE=mysql
DB_HOST=localhost
DB_NAME=<DB_NAME_HERE>
DB_USERNAME=<DB_USER_HERE>
DB_PASS=<DB_PASS_HERE>
DB_PORT=3306

```

Once the above settings are done, run the migration & create tables: 

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

## Production Build

To use the starter in production mode, here are the steps: 

- Set  **DEBUG=False** in `.env`
- Execute `collectstatic` command
  - `$ python manage.py collectstatic --no-input` 

<br />

## **Deploy on Render**

- Create a Blueprint instance
  - Go to https://dashboard.render.com/blueprints this link.
- Click `New Blueprint Instance` button.
- Connect the `repo` that you want to deploy.
- Fill the `Service Group Name` and click on the `Update Existing Resources` button.
- Edit the Environment and [specify the PYTHON_VERSION](https://render.com/docs/python-version)
  - Version `3.11.5` was used for **[this deployment](https://rocket-django.onrender.com/)**
- After that, your deployment will start automatically.

At this point, the product should be LIVE.

<br />

## Codebase 

```bash
< PROJECT ROOT >
   |
   |-- core/                 # Project Settings 
   |    |-- settings.py 
   |    |-- wsgi.py     
   |    |-- urls.py     
   |
   |-- home/                 # Presentation app 
   |    |-- views.py         # serve the HOMEpage  
   |    |-- urls.py     
   |    |-- models.py
   |
   |-- apps/                 # Utility Apps 
   |    |-- common/          # defines models & helpers
   |    |    |-- models.py   
   |    |    |-- util.py 
   |    |-- users            # Handles Authentication 
   |    |-- api              # DRF managed API
   |    |-- charts           # Showcase Different Charts
   |    |-- tables           # Implements DataTables
   |    |-- tasks            # Celery, async processing
   |
   |-- templates/            # UI templates 
   |-- static/               # Tailwind/Flowbite 
   |    |-- src/             # 
   |         |-- input.css   # CSS Styling
   |
   |-- Dockerfile            # Docker
   |-- docker-compose.yml    # Docker 
   |
   |-- render.yml            # CI/CD for Render
   |-- build.sh              # CI/CD for Render 
   |
   |-- manage.py             # Django Entry-Point
   |-- requirements.txt      # dependencies
   |-- .env                  # ENV File
   |
   |-- *************************************************      
```   

<br />

## Resources

- Access [AppSeed](https://appseed.us/) for more starters and support 
- [Deploy Projects on Aws, Azure and DO](https://www.docs.deploypro.dev/) via **DeployPRO**
- Create landing pages with [Simpllo, an open-source site builder](https://www.simpllo.com/)
- Build apps with [Django App Generator](https://app-generator.dev/django/) (free service)
