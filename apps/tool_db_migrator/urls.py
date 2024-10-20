from django.urls import path

from apps.tool_db_migrator import views

urlpatterns = [
    path("tools/db-migrator" , views.db_migrator, name="tool_db_migrator"),
]
