from django.urls import path
from apps.dashboard import views


urlpatterns = [
    # Blog articles
    path('blogs/', views.blog_dashboard, name="blog_dashboard"),
    path("create-blog/", views.create_blog, name="create_blog"),
    path('update-blog/<str:slug>/', views.update_blog, name="update_blog"),
    path('delete-blog/<str:slug>/', views.delete_blog, name="delete_blog"),
    path('bookmarked-blog/', views.bookmarked_blog, name="bookmarked_blog"),

    # Products
    path('products/', views.product_dashboard, name="product_dashboard"),
    path('create-product/', views.create_product, name="create_product"),
    path('update-product/<str:slug>/', views.update_product, name="update_product"),
    path('delete-product/<str:slug>/', views.delete_product, name="delete_product"),
]
