from django.urls import path
from apps.products import views


urlpatterns = [
    path('product/', views.products_view, name="products"),
    path('product/<str:design>/<str:tech1>/', views.products_by_tech1, name="products_by_tech1"),

    # Admin dashboard
    path('admin-dashboard/', views.admin_dashboard, name="admin_products"),
    path('admin-dashboard/<str:tech1>/', views.admin_dashboard_by_tech1, name="admin_dashboard_by_tech1"),
]
