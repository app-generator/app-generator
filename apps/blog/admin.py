from datetime import datetime

from django.contrib import admin, messages
from django.utils.translation import ngettext

from apps.blog.models import Article
from home.models import State


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'state']
    list_filter = ['state']
    search_fields = ['title']
    actions = ['make_published']
    
    def make_published(self, request, queryset):
        updated = queryset.update(state=State.PUBLISHED, published_at=datetime.now())
        self.message_user(request, ngettext(
            '%d article was published successfully.',
            '%d articles were published successfully.',
            updated,
        ) % updated, messages.SUCCESS)
    
    make_published.short_description = "Publish selected articles"

admin.site.register(Article, ArticleAdmin)
