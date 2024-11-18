from django.urls import path, re_path
from apps.products import views


urlpatterns = [
    path('product/', views.products_view, name="products"),
    path('product/tags/<str:tags>/', views.products_view, name="products"),
    path('grouped-product/<str:design>/<str:tech1>/', views.products_by_tech1, name="products_by_tech1"),

    # Admin dashboard
    #re_path(r'^(?P<type>[^/]+)/(?P<tech1>[^/]+)?/?$', views.admin_dashboard, name="admin_products"),
    path('admin-dashboards/<str:tech1>/', views.admin_dashboard_by_tech1, name="admin_dashboard_by_tech1"),

    path('product/<str:design>/<str:tech1>/', views.product_detail, name="product_detail"),
    path('download-product/<str:slug>/', views.download_product, name="download_product"),
    path('fetch-changelog/', views.fetch_changelog_view, name='fetch_changelog'),
]
