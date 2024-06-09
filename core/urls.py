"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path 
from django.views.static import serve

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView

import os


from apps.common.sitemap import BlogSitemap,ProductSitemap

sitemaps = {
    'blog': BlogSitemap,
    'product': ProductSitemap,
}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('apps.pages.urls')),
    path("users/", include("apps.authentication.urls")),
    path("tasks/", include("apps.tasks.urls")),
    path("dashboard/", include("apps.dashboard.urls")),
    path("", include("apps.products.urls")),
    path('', include('apps.blog.urls')),
    path('ticket/', include('apps.ticket.urls')),
    # path('docs/', include('apps.docs.urls')),
    path('docs/', include('docs.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/', include('apps.api.product.v1.urls')),
    path('api/', include('apps.api.chat.v1.urls')),

     path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
     path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    
    path("__debug__/", include("debug_toolbar.urls")),   


    # Serve other documentation files
    re_path(r'^docs/(?P<path>.*)$', serve, {
        'document_root': os.path.join(os.path.dirname(__file__), '..', 'apps', 'docs', '_build', 'html'),
        'show_indexes': True
    }),   

]

schema_view = get_schema_view(
   openapi.Info(
      title="Products API",
      default_version='v1',
      description="Product description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

