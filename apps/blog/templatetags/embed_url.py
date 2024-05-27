from django import template
from urllib.parse import urlparse, parse_qs

register = template.Library()

@register.filter
def to_embed_url(value):
    query = urlparse(value).query
    video_id = parse_qs(query).get('v')
    return f"https://www.youtube.com/embed/{video_id[0]}" if video_id else value
