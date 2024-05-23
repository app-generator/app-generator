from django.urls import path
from .views import serve_docs_index

urlpatterns = [
    path('', serve_docs_index, name='docs_index'),
    # path('<path:path>/', serve_docs, name='docs_serve'),
]
