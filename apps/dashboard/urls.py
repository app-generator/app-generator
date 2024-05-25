from django.urls import path
from apps.dashboard import views


urlpatterns = [
    path('blog/', views.blog_dashboard, name="blog_dashboard"),
    path('update-blog/<str:slug>/', views.update_blog, name="update_blog"),
    path('delete-blog/<str:slug>/', views.delete_blog, name="delete_blog"),
    path('bookmarked-blog/', views.bookmarked_blog, name="bookmarked_blog"),
]
