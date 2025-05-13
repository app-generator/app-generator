# Built with [Django App Generator](https://app-generator.dev/tools/django-generator/)

Starter generated with [Django Generator](https://app-generator.dev/tools/django-generator/) (an open-source service) using **__DESIGN__ Design**, best practices and up-to-date Dependencies.
In order to use the sources, follow the build instructions as presented in `Start with Docker` and `Manual Build` sections. 

- Get [Support](https://app-generator.dev/ticket/create/?generated_repo=https://github.com/app-generator/__REPO_NAME__) via `eMail` and `Discord`
- Resources:
  - [Getting Started with Django](https://app-generator.dev/docs/technologies/django/index.html)
  - [Onboarding Kit for Developers](https://app-generator.dev/onboarding-kit/) - Premium resources for coding services in no-time.
  - [Discounts for Developers](https://app-generator.dev/discounts) - Build your own dev bundle and start fast 
  - [Build Dynamic Services with Django](https://app-generator.dev/docs/developer-tools/dynamic-django/index.html)
  
<br />

## Features: 

- `Up-to-date Dependencies`, Best practices
- Desing: __DESIGN__
- Extended User Profile 
- (optional) API Generator
- (optional) Celery
- (optional) OAuth Github, Google
- (optional) CI/CD for Render
- (optional) Docker

<br />

## [Deploy on Render](https://app-generator.dev/docs/deployment/render/index.html) (free plan)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

<br /> 

## [Start Project with Docker](https://app-generator.dev/docs/technologies/docker/index.html)

> In case the starter was built with Docker support, here is the start up CMD:

```bash
$ docker-compose up --build
```

Once the above command is finished, the new app is started on `http://localhost:5085`

<br />

## Manual Build 

> Download/Clone the sources  

```bash
$ git clone https://github.com/__REPO_NAME__.git
$ cd __REPO_NAME__
```

<br />

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> `Set Up Database`

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> `Start the App`

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

__CELERY__

__OAUTH_GITHUB__

---
Starter built with [Django App Generator](https://app-generator.dev/tools/django-generator/) - Open-source service for developers and companies.
