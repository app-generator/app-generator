# [Django Generated](https://app-generator.dev/tools/django-generator/) Project

Starter built with [Django App Generator](https://app-generator.dev/tools/django-generator/) (an open-source service) using a modern UI Kit.

In order to use the sources, follow the build instructions as presented in `Start with Docker` and `Manual Build` sections. 

<br />

## Features: 

- `Up-to-date Dependencies`, best practices
- Modern UI
- Extended User Profile 
- (optional) API Generator
- (optional) Celery
- (optional) OAuth Github, Google
- (optional) CI/CD for Render
- (optional) Docker

<br />

## [Django Documentation](https://app-generator.dev/docs/technologies/django.html)

- [Getting Started](https://app-generator.dev/docs/technologies/django/index.html)
- [Django Cheatsheet](https://app-generator.dev/docs/technologies/django/cheatsheet.html)
- [Adding Custom Commands in Django](https://app-generator.dev/docs/technologies/django/custom-command.html)
- [Integrate React in Django](https://app-generator.dev/docs/technologies/django/integrate-react.html)

<br />

## Deploy on `Render` (free plan)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

<br /> 

## Start with `Docker`

> In case the starter was built with Docker support, here is the start up CMD:

```bash
$ docker-compose up --build
```

Once the above command is finished, the new app is started on `http://localhost:5085`

<br />

## Manual Build 

> Download/Clone the sources  

```bash
$ git clone https://github.com/<THIS_REPO>.git
$ cd <LOCAL_Directory>
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
Starter built with [Django App Generator](https://app-generator.dev/tools/django-generator/) - open-source service for developers.
