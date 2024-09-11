from django.urls import path
from apps.tool_csv_processor import views

urlpatterns = [
    path('tools/csv-processor/', views.index, name="tool_csv_processor"),
]
