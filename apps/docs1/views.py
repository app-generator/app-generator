
from django.http import HttpResponse, Http404
import os


def serve_docs_index(request):
    index_path = os.path.join(os.path.dirname(__file__), '_build', 'html', 'index.html')
    if os.path.exists(index_path):
        with open(index_path, 'r') as f:
            return HttpResponse(f.read(), content_type='text/html')
    else:
        raise Http404("Index file not found")
