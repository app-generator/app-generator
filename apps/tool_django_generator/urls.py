from django.urls import path
from apps.tool_django_generator import views

urlpatterns = [
    path('tools/django-generator', views.index, name="tool_django_generator"),
]
