# custom_tags.py
from django import template
import os

register = template.Library()

@register.filter
def is_string(value):
    return isinstance(value, str)

    
    

# In your template
