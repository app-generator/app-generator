from django.urls import path
from .views import GeneratorViewAPI

urlpatterns = [
    path('generator/', GeneratorViewAPI.as_view(), name='generator_api'),
]
