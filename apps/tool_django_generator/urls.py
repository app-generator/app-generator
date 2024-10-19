from django.urls import path
from apps.tool_django_generator.views import *

urlpatterns = [
    path("tools/django-generator", index, name="tool_django_generator"),
    path(
        "tools/django-generator-status",
        StatusView.as_view(),
        name="django-generator-status",
    ),
    path(
        "tools/django-generator/design",
        DesignView.as_view(),
        name="dajngo-geneator-design"
    )
]
