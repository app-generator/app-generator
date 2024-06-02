from django import template
from apps.common.models import TeamRole

register = template.Library()

@register.filter(name='get_role')
def get_role(team, user):
    return TeamRole.objects.get(team=team, author=user).role