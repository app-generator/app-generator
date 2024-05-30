from apps.common.models_authentication import Profile

def profile_context(request):
    is_company = False
    if request.user.is_authenticated:
        is_company = Profile.objects.filter(user=request.user, role='Company').exists()
    return {'is_company': is_company}