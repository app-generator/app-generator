from django.contrib import admin
from django.apps import apps
from apps.common.models_blog import Article, State
from django.contrib import messages
from datetime import datetime
from django.utils.translation import ngettext


excluded_models = ['common.Article']

for model in apps.get_app_config('common').get_models():
    model_name = f"{model._meta.app_label}.{model.__name__}"
    if model_name not in excluded_models:
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass


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