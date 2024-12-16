from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('signin/', views.SignInView.as_view(), name="signin"),
    path('signin2/', views.SignInView2.as_view(), name="signin2"),
    path('signout/', views.signout_view, name="signout"),
]