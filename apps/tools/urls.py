from django.urls import path
from apps.tools import views

urlpatterns = [
    path('tools/', views.index, name="tools"),
]
