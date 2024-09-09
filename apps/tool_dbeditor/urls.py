from django.urls import path

from apps.tool_dbeditor import views

urlpatterns = [
    path("db-editor" , views.db_editor, name="db_editor"),
]
