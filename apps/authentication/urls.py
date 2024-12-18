from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('signin/', views.SignInView.as_view(), name="signin"),
    path('signout/', views.signout_view, name="signout"),
]