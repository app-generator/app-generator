from django.urls import path
from .views import serve_docs

urlpatterns = [
    path('', serve_docs, {'path': 'index.html'}, name='docs_index'),
    path('<path:path>/', serve_docs, name='docs_serve'),
]
