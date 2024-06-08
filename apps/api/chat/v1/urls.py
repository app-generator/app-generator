from django.urls import path
from apps.api.chat.v1 import views


urlpatterns = [
    path('chat/', views.ChatView.as_view(), name="chat"),
]
