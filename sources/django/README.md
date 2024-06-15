# `Generated` Django Project

Starter built with [Django App Generator](https://app-generator.dev/django/) - Actively supported by [AppSeed](https://appseed.us/) via `Email` and `Discord`. 

In order to use the sources, follow the build instructions as presented in `Start with Docker` and `Manual Build` sections. 

<br />

## Features: 

- ✅ `Up-to-date Dependencies`
- ✅ Modern UI 
- ✅ API Generator (optional)
- 🚀 [AWS, DO, Azure Deploy Assistance](https://deploypro.dev/) via `DeployPRO` service (read the [DOCS](https://docs.app-generator.dev/deployment/intro))

<br />

## Need More? 

- 🚀 Upgrade to **PRO Account** - **Only [$19/mo](https://appseed.gumroad.com/l/rocket-pro-subscription)**
  - `Unlimited Apps`
  - `Premium Support`
  - `CI/CD Scripts` (Render)
- 👉 **[Custom Development Services](https://appseed.us/custom-development/)** for `accelerated growth`
  - `Dedicated Team`: PM, Developer, Tester
  - `Post-delivery Warranty` and Support
  - `AWS, DO, Azure Deploy Assistance` included

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

> `Generate your API` (optional) 

```bash
$ python manage.py generate-api -f
```

<br />

> `Start the App`

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

---
Starter built with [Django App Generator](https://app-generator.dev/django/), a free service provided by AppSeed.
