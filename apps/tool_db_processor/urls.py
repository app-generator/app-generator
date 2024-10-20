from django.urls import path

from apps.tool_db_processor import views

urlpatterns = [
    path("tools/db-processor" , views.db_processor, name="tool_db_processor"),
]
