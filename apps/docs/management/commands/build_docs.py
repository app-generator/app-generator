from django.core.management.base import BaseCommand
import os
from apps.docs.views import process_directory
# Paths
INPUT_DIR = 'apps/docs/content'
OUTPUT_DIR = 'apps/docs/output'

class Command(BaseCommand):
    help = 'Generate HTML files from Markdown'

    def handle(self, *args, **kwargs):
        try:
            process_directory(INPUT_DIR, OUTPUT_DIR)
            self.stdout.write(self.style.SUCCESS('Successfully built docs'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error building docs: {e}'))
