import requests
from django.contrib.auth.models import User
from apps.common.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount
from django.core.files.base import ContentFile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        if instance.is_superuser:
            profile.role = "admin"
            profile.save()


@receiver(post_save, sender=SocialAccount)
def update_profile_with_github_avatar(sender, instance, created, **kwargs):
    if created and instance.provider == 'github':
        try:
            profile = Profile.objects.get(user=instance.user)
            avatar_url = instance.extra_data.get('avatar_url')
            profile.full_name = instance.extra_data.get('name', '')
            profile.email = instance.extra_data.get('email', '')

            if avatar_url:
                response = requests.get(avatar_url)
                if response.status_code == 200:
                    file_name = f"{instance.user.id}_avatar.jpg"
                    profile.avatar.save(file_name, ContentFile(response.content), save=False)
            
            profile.save()

        except Profile.DoesNotExist:
            pass