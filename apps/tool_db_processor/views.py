from django.shortcuts import render

# Create your views here.

def db_processor(request):

    context = {
        'segment'        : 'db_processor',
        'parent'         : 'tools',
        'page_title'     : 'DataBase Processor - Analyze and Unload Data for SQLite, PostgreSQL, MySql',
        'page_info'      : 'Process your database information with ease - unload, analyze schema, download in different formats',
        'page_keywords'  : 'db processor, unload db data, sql to json, database tools, db tool, custom development, ai tools, dev tools, tools for developers and companies',
        'page_canonical' : 'tools/db-migrator',        
    }     
    return render(request, "tools/db-processor.html", context)