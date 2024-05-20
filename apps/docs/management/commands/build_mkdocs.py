from django.core.management.base import BaseCommand
import subprocess
import os

class Command(BaseCommand):
    help = 'Build MkDocs site'

    def handle(self, *args, **kwargs):
        docs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../docs')
        subprocess.call(['mkdocs', 'build'], cwd=docs_dir)
        self.stdout.write(self.style.SUCCESS('Successfully built MkDocs site'))
