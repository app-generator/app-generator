import os, json
from django.core.management.base import BaseCommand
from django.conf import settings

import markdown

from util.helpers import files_get, file_md_process, file_write, parse_md_header

class Command(BaseCommand):
    help = 'Generate DOCS'

    def handle(self, *args, **kwargs):

        BASE_DIR = getattr(settings, 'BASE_DIR')
        DOCS_DIR = os.path.join(BASE_DIR, 'docs', 'content')
        
        md_files = files_get( DOCS_DIR, 'md')

        #print( ' > Found ' + str( len(md_files) ) + ' MarkDown files in ' + DOCS_DIR )

        for f in md_files:
            status, file_dir, file_name, file_ext, file_header, md_content = file_md_process( f )
            print ( '*** Markdown File:  ' + f      ) 
            print ( '  > DIR        : ' + file_dir  ) 
            print ( '  > File Name  : ' + file_name ) 
            print ( '  > Extension  : ' + file_ext  ) 
            #print ( '  > HEADER     : ' + str( file_header )  ) 
            #print ( '  > MD Content : ' + str( md_content  )  ) 

            # file_header = LIST
            # md_content = LIST 
            
            md_content      = "\n\r".join( md_content)
            md_header_props = parse_md_header( file_header )

            # Write HTML     
            f_html = os.path.join(file_dir, file_name + '.html' )
            file_write( f_html, markdown.markdown(md_content) )

            # Write header (JSON)
            f_html_json = os.path.join(file_dir, file_name + '.json' )
            file_write( f_html_json, md_header_props )
