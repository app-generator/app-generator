from django.shortcuts import render

# Create your views here.


def tasks(request):
    context = {
        'segment': 'tasks'
    }
    return render(request, 'pages/tasks.html', context)