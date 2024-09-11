from django.urls import path
from apps.tool_flask_generator import views

urlpatterns = [
    path('tools/flask-generator/', views.index, name="tool_flask_generator"),
]
