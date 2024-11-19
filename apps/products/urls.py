from django.urls import path, re_path
from apps.products import views


urlpatterns = [
    path('product/', views.products_view, name="products"),
    path('product/tags/<str:tags>/', views.products_view, name="products"),
    path('grouped-product/<str:design>/<str:tech1>/', views.products_by_tech1, name="products_by_tech1"),

    # Admin dashboard
    #re_path(r'^(?P<type>[^/]+)/(?P<tech1>[^/]+)?/?$', views.admin_dashboard, name="admin_products"),
    #path('admin-dashboards/<str:tech1>/', views.admin_dashboard_by_tech1, name="admin_dashboard_by_tech1"),

    # Categories
    path('admin-dashboards/', views.dashboards, name="dashboards"),
    path('admin-dashboards/<str:aTech>/', views.dashboards, name="dashboards_tech"),
    path('admin-dashboards/<str:aTech>/<str:aType>/', views.dashboards, name="dashboards_tech_type"),

    path('apps/', views.apps, name="apps"),
    path('apps/<str:aTech>/', views.apps, name="apps_tech"),
    path('apps/<str:aTech>/<str:aType>/', views.apps, name="apps_tech_type"),

    path('ui-kit/', views.ui_kit, name="ui_kit"),
    path('ui-kit/<str:design_system>/', views.ui_kit, name="ui_kit_design_system"),

    path('agency/', views.agency, name="agency"),
    path('agency/<str:design_by>/', views.agency, name="agency_design_by"),

    path('product/<str:design>/<str:tech1>/', views.product_detail, name="product_detail"),
    path('download-product/<str:slug>/', views.download_product, name="download_product"),
    path('fetch-changelog/', views.fetch_changelog_view, name='fetch_changelog'),
]
