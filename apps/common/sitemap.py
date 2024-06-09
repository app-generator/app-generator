from django.contrib.sitemaps import Sitemap
from apps.common.models_products import Products
from apps.common.models_blog import Article

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Products.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
    

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.updated_at