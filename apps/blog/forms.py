import copy
from django import forms
from django.utils.translation import gettext_lazy as _
from django_quill.forms import QuillFormField
from apps.common.models_blog import Tag

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
        super().__init__(*args, **kwargs)
        config = extend_quill_config('image', 'video')
        
        self.fields['content'].widget.config = config
        
    thumbnail = forms.ImageField(
        label=_("Thumbnail"),
        widget=forms.FileInput(
            attrs={
            'class': "block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400",
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
    subtitle = forms.CharField(
        label=_("Subtitle"),
        widget=forms.TextInput(
            attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 
            'placeholder': 'Subtitle'
        }),
        min_length=10,
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        label=_("Tags"),
        widget=forms.SelectMultiple(
            attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
        }),
    )
    content = QuillFormField(
        label=_("Content"),
        widget=forms.Textarea(
            attrs={
            'class': 'form-textarea', 
            'placeholder': 'Type here',
        }),
    )