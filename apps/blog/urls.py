from django.urls import path, include, re_path
from django.utils.translation import gettext_lazy as _

from . import views

urlpatterns = [
    path("blog/", views.blogs, name='blog'),
    path("blog/tags/<str:tags>/", views.blogs, name='blog'),
    path("blog/<str:slug>/", views.blog_details, name="blog_detail"),
    path("blog/tag/<str:slug>/", views.filter_by_tags, name="filter_by_tags"),
    path("add-bookmark/<str:slug>/", views.add_bookmark, name="add_bookmark"),
]