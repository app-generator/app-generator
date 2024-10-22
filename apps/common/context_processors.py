from apps.common.models_authentication import Profile, RoleChoices
from django.conf import settings

def profile_context(request):
    is_company = False
    if request.user.is_authenticated:
        is_company = Profile.objects.filter(user=request.user, role=RoleChoices.COMPANY).exists()
    return {'is_company': is_company}


def version_context(request):
    return {
        'version': getattr(settings, 'VERSION')
    }