from django.urls import path, re_path
from apps.tool_django_generator.views import *

urlpatterns = [
    re_path(r"^tools/flask-generator/(?:(?P<design>[\w-]+)/)?$", index, name="tool_flask_generator"),
    path(
        "tools/flask-generator-status",
        StatusView.as_view(),
        name="flask-generator-status",
    ),
    path(
        "tools/flask-generator/design",
        DesignView.as_view(),
        name="flask-generator-design"
    )
]