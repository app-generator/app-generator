from django.shortcuts import render
from django.http import Http404
import os
import markdown
import json
from collections import defaultdict

from django.conf import settings

from util.helpers import file_read

def serve_docs(request, path='index.html'):
    
    BASE_DIR = getattr(settings, 'BASE_DIR')
    DOCS_DIR = os.path.join(BASE_DIR, 'docs', 'content')
    DOCS_FILE = os.path.join(DOCS_DIR, 'index.html')

    context = {
    'content_title' : 'Some Title',     
    'content'       : file_read( DOCS_FILE )
    }
    return render(request, 'docs/index.html', context)
