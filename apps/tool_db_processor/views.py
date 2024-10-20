from django.shortcuts import render

# Create your views here.

def db_processor(request):

    context = {
        'segment': 'db_processor',
        'parent': 'tools'
    }    
    return render(request, "tools/db-processor.html", context)