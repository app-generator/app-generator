from django.urls import path

from apps.tool_dbeditor import views

urlpatterns = [
    path("tools/db-editor" , views.db_editor, name="db_editor"),
]
