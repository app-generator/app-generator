from django.urls import path

from apps.tool_db_processor import views

urlpatterns = [
    path("tools/db-processor" , views.db_processor, name="tool_db_processor"),
    path("tools/db-processor/checkconnect", views.check_connect_view, name="check_connect_db"),
    path("tools/db-processor/db-analyze", views.db_analyze_view, name="DB migrate"),
]
