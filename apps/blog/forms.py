import copy
from django import forms
from django.utils.translation import gettext_lazy as _
from django_quill.forms import QuillFormField

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
            'style': "opacity: 0; position: absolute; width: 100%; height: 100%; top: 0; left: 0; cursor: pointer; pointer-events: none;",
            'accept': 'image/png, image/gif, image/jpeg',
        }),
    )
    title = forms.CharField(
        label=_("Title"),
        widget=forms.TextInput(
            attrs={
            'class': 'form-input', 
            'placeholder': 'Title'
        }),
        min_length=5,
    )
    subtitle = forms.CharField(
        label=_("Subtitle"),
        widget=forms.TextInput(
            attrs={
            'class': 'form-input', 
            'placeholder': 'Subtitle'
        }),
        min_length=10,
    )
    tags = forms.CharField(
        label=_("Tags"),
        widget=forms.TextInput(
            attrs={
            'name': 'tags',
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
    bookmarked = forms.BooleanField(
        label=_("Bookmark"),
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600',
                'name': 'bookmarked'
        }),
    )