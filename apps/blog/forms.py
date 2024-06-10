import copy
from django import forms
from django.utils.translation import gettext_lazy as _
from django_quill.forms import QuillFormField
from apps.common.models_blog import Tag, Article, VisibilityChoices

from django.conf import settings

def extend_quill_config(*args):
    default_config = getattr(settings, "QUILL_CONFIGS", None)
    configs = copy.deepcopy(default_config)
    config = configs['default']
    
    for arg in args:
        config['modules']['toolbar'][1].append(arg)
        config['formats'].append(arg)
        
    return config


class ArticleForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        config = extend_quill_config('image', 'video')
        
        self.fields['content'].widget.config = config

        if user and not user.profile.pro:
            self.fields['canonical_url'].widget.attrs['readonly'] = True
            # self.fields.pop('canonical_url')
        
    thumbnail = forms.ImageField(
        label=_("Thumbnail"),
        widget=forms.FileInput(
            attrs={
            'style': "opacity: 0; position: absolute; width: 100%; height: 100%; top: 0; left: 0; cursor: pointer; pointer-events: none;",
            'accept': 'image/png, image/gif, image/jpeg',
        }),
    )
    title = forms.CharField(
        label=_("Title"),
        widget=forms.TextInput(
            attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 
            'placeholder': 'Title'
        }),
        min_length=5,
    )
    slug = forms.CharField(
        label=_("Slug"),
        widget=forms.TextInput(
            attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 
            'placeholder': 'Slug'
        }),
        min_length=5,
    )
    subtitle = forms.CharField(
        label=_("Subtitle"),
        widget=forms.TextInput(
            attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 
            'placeholder': 'Subtitle'
        }),
        min_length=10,
    )
    canonical_url = forms.CharField(
        label=_("Canonical URL (Pro)"),
        widget=forms.TextInput(
            attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 
            'placeholder': 'Canonical URL'
        }),
        min_length=10,
        required=False
    )
    video = forms.URLField(
        label=_("Video (Optional)"),
        widget=forms.URLInput(
            attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 
            'placeholder': 'https://www.youtube.com/watch?v=video_id',
            'for': 'id_video'
        }),
        required=False
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        label=_("Tags"),
        widget=forms.SelectMultiple(
            attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            'id': 'tags'
        }),
    )
    visibility = forms.ChoiceField(
        label=_("Visibility"),
        choices=VisibilityChoices.choices,
        widget=forms.Select(
            attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            'id': 'visibility'
        }), 
        required=False
    )
    content = QuillFormField(
        label=_("Content"),
        widget=forms.Textarea(
            attrs={
            'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 
            'placeholder': 'Type here',
        }),
    )

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if Article.objects.filter(slug=slug).exists():
            raise forms.ValidationError("A blog article with this slug already exists.")
        return slug