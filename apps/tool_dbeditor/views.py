from django.shortcuts import render

# Create your views here.


def db_editor(request):
    return render(request, "tools/db-editor.html")