import requests
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Sitemap checker'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Fetching urls...'))

        response = requests.get("https://appseed-docs.onrender.com/sitemap.xml")
        response = requests.get("https://docs.appseed.us/sitemap.xml")
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "lxml-xml")
            loc_tags = soup.find_all('loc')

            urls = [loc.text for loc in loc_tags]

            for url in urls:
                new_url = url.replace('docs.appseed.us', 'app-generator.dev/docs')
                try:
                    check_response = requests.get(new_url)
                    if check_response.status_code == 200:
                        self.stdout.write(self.style.SUCCESS(f"OK: {new_url}"))
                    else:
                        self.stdout.write(self.style.ERROR(f"Error: {new_url}"))
                except requests.RequestException as e:
                    self.stdout.write(self.style.ERROR(f"Error: {new_url} - {e}"))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to fetch sitemap: {response.status_code}'))
