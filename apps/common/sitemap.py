from django.contrib.sitemaps import Sitemap
from apps.common.models_products import Products
from apps.common.models_blog import Article
from django.urls import reverse
class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Products.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return reverse("product_detail", args=[obj.design,obj.tech1])
    

class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
 
    def items(self):
        return Article.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return reverse("blog_detail", args=[obj.slug])

