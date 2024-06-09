import requests
from bs4 import BeautifulSoup
import html2text
import markdown2
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def fetch_changelog(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find('article')
        if article:
            html_content = str(article)
            markdown_content = html2text.html2text(html_content)
            html_rendered = markdown2.markdown(markdown_content)
        else:
            html_rendered = '<p>Changelog content not found.</p>'
    else:
        html_rendered = '<p>Unable to fetch changelog at this time.</p>'
    
    return mark_safe(html_rendered)