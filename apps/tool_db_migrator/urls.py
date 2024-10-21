from django.urls import path

from apps.tool_db_migrator.views import *

urlpatterns = [
    path("tools/db-migrator" , db_migrator, name="tool_db_migrator"),
    path("tools/db-migrator/checkconnect", check_connect_view, name="check_connect_db"),
    path("tools/db-migrator/db-migrate", db_migrate_view, name="DB migrate"),
]
