from django.urls import path
from apps.products import views


urlpatterns = [
    path('product/', views.products_view, name="products"),
    path('product/<str:design>/<str:tech1>/', views.products_by_tech1, name="products_by_tech1"),
]
