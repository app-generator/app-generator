from django.urls import path
from apps.tasks import views


urlpatterns = [
    path('', views.tasks, name="tasks"),
]
