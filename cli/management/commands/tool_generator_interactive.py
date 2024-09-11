import os, json, uuid, re, pprint  
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.common.models import *
from apps.helpers.generator import * 

import inquirer

questions = [
  inquirer.Text('project_name', message="Project Friendly Name"),
  inquirer.List('framework',
                message="The Backend Framework",
                choices=['django', 'flask (soon)', 'nodejs (soon)'],
            ),
  inquirer.List('design',
                message="The UI Kit",
                choices=['datta', 'volt', 'soft-dashboard'],
            ),
  inquirer.List('database',
                message="The Database",
                choices=['sqlite', 'mysql', 'pgsql'],
            ),
  inquirer.List('oauth',
                message="Social Login",
                choices=['none', 'github'],
            ),
  inquirer.List('sample_model',
                message="Add a Product Model",
                choices=['no', 'yes'],
            ),            
  inquirer.List('custom_user',
                message="Extend User Model",
                choices=['no', 'yes'],
            ),
  inquirer.List('celery',
                message="Add Celery Support",
                choices=['no', 'yes'],
            ),            
  inquirer.List('docker',
                message="Add Docker Scripts",
                choices=['no', 'yes'],
            ),
  inquirer.List('ci_cd',
                message="(Render) CI/CD Scripts",
                choices=['no', 'yes'],
            ),
  inquirer.List('go_live',
                message="(Render) LIVE Deploy",
                choices=['no', 'yes'],
            ),
]

class Command(BaseCommand):

    help = 'Generate Code'

    def add_arguments(self, parser):
        
        parser.add_argument('-i', '--info', action='store_true', help='Prin Help')

    def handle(self, *args, **kwargs):

        ARG_HELP   = kwargs[ 'info' ]

        if ARG_HELP:
            print(f"")
            print(f" > HELP: Generator Interactive (CLI version)")
            print(f"    -i (or --info)      : Print this help, and exit")
            print(f"")
            return  

        answers = inquirer.prompt(questions)
        pprint.pp( answers, indent=4 )
        
        print ('\n ------------------ \n')

        JSON_PATH = os.path.join('sources', 'input-template.json')
        JSON_DATA = json_load( JSON_PATH )
        
        if not JSON_DATA:
            print( ' > Err loading JSON: ' + JSON_PATH )            
            return

        JSON_DATA['design' ] = answers['design']
        JSON_DATA['backend'] = 'django'

        # DB: Sqlite, PgSQL, MySql
        JSON_DATA['db']['driver'] = answers['database']

        # Oauth
        if 'github' == answers['oauth']:
            JSON_DATA['auth']['github'] = "1"
            
        if 'yes' != answers['sample_model']:
            JSON_DATA['models'] = {}
            JSON_DATA['tools']['generator'] = {}

        if 'yes' != answers['custom_user']:
            JSON_DATA['custom_user'] = {}

        if 'yes' == answers['celery']:
            JSON_DATA['tools']['celery'] = '1'

        if 'yes' == answers['docker']:
            JSON_DATA['deploy']['docker'] = '1'

        if 'yes' == answers['ci_cd']:
            JSON_DATA['deploy']['ci_cd'] = '1'

        #pprint.pp( JSON_DATA, indent=4 )

        file_content = json.dumps( JSON_DATA, indent=4)

        print( file_content )

        file_name    = h_random_ascii(8) + '_' + answers['framework'] +'_template.json' 
        file_path    = os.path.join('sources', file_name)

        file_write(file_path, file_content)

        print( '> File saved = ' + file_path )
        print( '> HOW to generate code:')
        print( '    |-- python manage.py tool_generator -f ' + file_path )

        return
