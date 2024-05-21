import os
import json
from django.core.management.base import BaseCommand
from apps.common.models_blog import Tag
from django.conf import settings

class Command(BaseCommand):
    help = 'Create tags'

    def handle(self, *args, **kwargs):
        Tag.objects.all().delete()

        media_dir = getattr(settings, 'MEDIA_ROOT')
        json_file_path = os.path.join(media_dir, 'seeder', 'tags.json')
        
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            self.create_tags(data)

    def create_tags(self, tags):
        for tag in tags:
            Tag.objects.get_or_create(name=tag)
            self.stdout.write(self.style.SUCCESS(f'Created tag: {tag}'))
        