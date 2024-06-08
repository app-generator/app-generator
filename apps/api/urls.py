from django.urls import path
from apps.api import views


urlpatterns = [
    path('product/', views.ProductListView.as_view(), name="product-list"),
    path('product/dashboard/', views.ProductDashboardListView.as_view(), name='product-dashboard-list'),
    path('product/apps/', views.ProductAppsListView.as_view(), name='product-apps-list'),
    path('product/api/', views.ProductAPIListView.as_view(), name='product-api-list'),
    path('product/django/', views.ProductDjangoListView.as_view(), name='product-django-list'),
    path('product/flask/', views.ProductFlaskListView.as_view(), name='product-flask-list'),
    path('product/nodejs/', views.ProductNodejsListView.as_view(), name='product-nodejs-list'),
]
