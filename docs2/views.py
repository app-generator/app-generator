from django.http import HttpResponse, Http404
import mimetypes
import os

def mkdocs_view(request, path='index.html'):
    # Base directory where the MkDocs static files are located
    base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')
    print(base_path)
    print(path)
    
    # Construct the full path to the requested resource
    full_path = os.path.join(base_path, path)

    # If the path is a directory, look for an index.html file inside it
    print(full_path)
    if os.path.isdir(full_path):
        full_path = os.path.join(full_path, 'index.html')

    # Check if the file exists
    if not os.path.exists(full_path):
        raise Http404("Page not found")

    # Determine the content type
    content_type, encoding = mimetypes.guess_type(full_path)
    if content_type is None:
        content_type = 'application/octet-stream'

    # Read and return the file content
    with open(full_path, 'rb') as file:
        file_content = file.read()
        print(file)

    return HttpResponse(file_content, content_type=content_type)
