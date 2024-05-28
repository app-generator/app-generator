from django.urls import path
from apps.products import views


urlpatterns = [
    path('products/', views.products_view, name="products"),
    path('products/<str:tech1>/', views.products_by_tech1, name="products_by_tech1"),
]
