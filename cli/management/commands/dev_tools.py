from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):

    help = 'Print all tools '

    def handle(self, *args, **kwargs):

        print( ' *** *** *** *** *** *** *** *** *** ***' )
        print( ' *** App Generator' )
        call_command('tool_generator', info=1)

        print( ' ***  *** *** ***  *** *** *** *** *** ***' )
        print( ' *** Interactive App Generator (Generates a project JSON Descriptor) ' )
        call_command('tool_generator_interactive', info=1)

        print( ' ***  *** *** ***  *** *** *** *** *** ***' )
        print( ' *** Upload Directories on GitHub (recursive operation) ' )
        call_command('tool_github_uploader', info=1)

        print( ' ***  *** *** ***  *** *** *** *** *** ***' )
        print( ' *** DB processor - Dump Tables & Data (any DBMS) ' )
        call_command('tool_db_processor', info=1)        

        print( ' ***  *** *** ***  *** *** *** *** *** ***' )
        print( ' *** CSV Processor - Inspect local & distant CSV Files ' )
        call_command('tool_inspect_source', info=1)        

        print( ' ***  *** *** ***  *** *** *** *** *** ***' )
        print( ' *** Codebase Inspector - Print registered apps' )
        call_command('help_print_apps')      