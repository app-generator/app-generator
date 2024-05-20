from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("support/", views.support, name="support"),
    path("custom-development/", views.custom_development, name="custom_development"),
    path("terms/", views.terms, name="terms"),
    path("about/", views.about, name="about"),
]
