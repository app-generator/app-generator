# Change Log

## [0.0.16] 2024-07-30
### Changes

- HOMEpage Update (minor)

## [0.0.15] 2024-07-30
### Changes

- [AI Processor](https://app-generator.dev/ai-processor/)
- Enhance products
  - tags
  - videos 

## [0.0.14] 2024-06-19
### Changes

- Update OAuth Scope
  - Remove access to REPOs
  - Workflow
- Add CSV Processor (not fully tested)    

## [0.0.13] 2024-06-17
### Changes

- Update CLI: 
  - Added GitHub Uploader
- Django Core Template
  - Update README & Settings

## [0.0.12] 2024-06-16
### Changes

- Added Django generator
  - `$ python manage.py generator -f sources/input-template-volt.json`
- Update README

## [0.0.11] 2024-05-22
### Changes

- Integrate DOCS [ Sphinx ]

## [0.0.10] 2024-05-21
### Changes

- Refactor Codebase
  - Move [Util](https://github.com/app-generator/appseed-v2/tree/main/util) from apps -> ROOT 
- Added [Util.Logger](https://github.com/app-generator/appseed-v2/blob/main/util/logger/__init__.py)
  - Usage: Apps.Pages, `index()`
    - https://github.com/app-generator/appseed-v2/blob/main/apps/pages/views.py

Sample Output, that prints the TimeStamp, File, Function & Line Number

```log
2024-05-21 22:19:16.741500 - AppSeed, DEBUG [apps.pages.views->support(), L:23] Begin
```

## [0.0.9] 2024-05-21
### Changes

- Added Blog Section 
- Added DOCS Section
- Update GitHub Login Scope
  - Email
  - Repo access (private & public)
  - Workflow (CI/CD)

## [0.0.8] 2024-05-20
### Changes

- Added Celery Beat:
  - [CRON Settings](https://github.com/app-generator/appseed-v2/blob/main/core/celery.py)
  - [Tasks/Scripts](https://github.com/app-generator/appseed-v2/tree/main/tasks_scripts) DIR
  - [Tasks LOGS](https://github.com/app-generator/appseed-v2/tree/main/tasks_scripts/logs)
    - [Sample LOG](https://github.com/app-generator/appseed-v2/blob/main/tasks_scripts/logs/2024-05-20-16-30-critical_task.log)

## [0.0.7] 2024-05-20
### Changes

- Update HOMEpage
- Added new pages
  - Terms, About and Support 

## [0.0.6] 2024-05-19
### Changes

- Update `AppSeed V2` SPECS: 
  - [SPECS API](https://github.com/app-generator/appseed-v2/blob/main/apps/api/README.md)
  - [SPECS Auth](https://github.com/app-generator/appseed-v2/blob/main/apps/auth/README.md)
  - [SPECS Blog](https://github.com/app-generator/appseed-v2/blob/main/apps/blog/README.md)
  - [SPECS Deploy](https://github.com/app-generator/appseed-v2/blob/main/apps/deploy/README.md)
  - [SPECS Docs](https://github.com/app-generator/appseed-v2/blob/main/apps/docs/README.md)
  - [SPECS Generator](https://github.com/app-generator/appseed-v2/blob/main/apps/generator/README.md)
  - [SPECS Pages](https://github.com/app-generator/appseed-v2/blob/main/apps/pages/README.md)
  - [SPECS Products](https://github.com/app-generator/appseed-v2/blob/main/apps/products/README.md)
  - [SPECS Tasks](https://github.com/app-generator/appseed-v2/blob/main/apps/tasks/README.md)
  - [SPECS DevTools](https://github.com/app-generator/appseed-v2/blob/main/apps/tools/README.md)

## [0.0.5] 2024-05-19
### Changes

- Refactoring
- Added [CLI](https://github.com/app-generator/appseed-v2/tree/main/cli) & [Custom Commands](https://github.com/app-generator/appseed-v2/tree/main/cli/management):
  - `python manage.py help`         # Check the `CLI` app
  - `python manage.py cmd_apps`     # [Django - List all registered APPS](https://github.com/app-generator/appseed-v2/blob/main/cli/management/commands/cmd_apps.py) 
  - `python manage.py cmd_models`   # [Django - List models (app APPS)](https://github.com/app-generator/appseed-v2/blob/main/cli/management/commands/cmd_models.py)
  - `python manage.py cmd_showcfg`  # [Django - Print Configuration](https://github.com/app-generator/appseed-v2/blob/main/cli/management/commands/cmd_showcfg.py)

## [0.0.4] 2024-05-19
### Changes

- Added [LIVE Deploy](https://appseed-v2.onrender.com/) via Render
- Added SPECS for all apps:
  - [SPECS API](https://github.com/app-generator/appseed-v2/blob/main/apps/api/README.md)
  - [SPECS Aut](https://github.com/app-generator/appseed-v2/blob/main/apps/auth/README.md)
  - [SPECS Blog](https://github.com/app-generator/appseed-v2/blob/main/apps/blog/README.md)
  - [SPECS Deploy](https://github.com/app-generator/appseed-v2/blob/main/apps/deploy/README.md)
  - [SPECS Docs](https://github.com/app-generator/appseed-v2/blob/main/apps/docs/README.md)
  - [SPECS Generato](https://github.com/app-generator/appseed-v2/blob/main/apps/generator/README.md)
  - [SPECS Pages](https://github.com/app-generator/appseed-v2/blob/main/apps/pages/README.md)
  - [SPECS Products](https://github.com/app-generator/appseed-v2/blob/main/apps/products/README.md)
  - [SPECS Tasks](https://github.com/app-generator/appseed-v2/blob/main/apps/tasks/README.md)
  - [SPECS DevTools](https://github.com/app-generator/appseed-v2/blob/main/apps/tools/README.md)

## [0.0.3] 2024-05-18
### Changes

- Added APPS folders
  - mostly codebase structure changes 

## [0.0.2] 2024-05-10
### Changes

- Update RM (minor)

## [0.0.1] 2024-05-10
### Changes

- REPO Created
