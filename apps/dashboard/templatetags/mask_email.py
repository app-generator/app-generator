from django import template

register = template.Library()

@register.filter(name='mask_email')
def mask_email(email):
    if not email:
        return ""
    try:
        username, domain = email.split('@')
        masked_username = username[:2] + '*' * (len(username) - 2)
        masked_domain = '*' * len(domain)
        return f"{masked_username}@{masked_domain}"
    except ValueError:
        return "********"