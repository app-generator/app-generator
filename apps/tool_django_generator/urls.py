from django.urls import path, re_path
from apps.tool_django_generator.views import *

urlpatterns = [
    re_path(r"^tools/django-generator/(?:(?P<design>[\w-]+)/)?$", index, name="tool_django_generator"),
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