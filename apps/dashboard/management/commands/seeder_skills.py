from django.core.management import BaseCommand
from apps.common.models import CategoryChoices, Skills

class Command(BaseCommand):
    help = 'Create skills for users'
    
    def handle(self, *args, **options):
        # Initialy delete all existing skills
        Skills.objects.all().delete()

        categories = {
            'PROGRAMMING': ['Python', 'Javascript', 'Ruby', 'Java', 'C++', 'C#'],
            'FRAMEWORK': ['React', 'Vue', 'Django', 'Flask', 'NodeJS', 'Spring', 'Angular'],
            'DEPLOYMENT': ['CI/CD', 'AWS', 'DO', 'Azure', 'GCP', 'Heroku'],
            'NOCODE': ['Bubble', 'Webflow', 'Retool', 'Airtable', 'Adalo', 'Appgyver']
        }

        for category_name, skills_list in categories.items():
            for skill in skills_list:
                category, _ = Skills.objects.get_or_create(category=category_name, name=skill)
                self.stdout.write(self.style.SUCCESS(f'Successfully created skill "{category.name}" in category "{category.category}"'))