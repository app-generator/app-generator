from django.shortcuts import render

# Create your views here.

def db_migrator(request):

    context = {
        'segment': 'db_migrator',
        'parent': 'tools'
    }    
    return render(request, "tools/db-migrator.html", context)