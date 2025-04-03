import requests, json
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup

from helpers import *

class Command(BaseCommand):
    help = 'AppSeed Products Migration'

    def handle(self, *args, **kwargs):
        
        db_products = json.loads( file_load( os.path.join('media', 'migration', 'appseed_products.json') ) )
        
        if db_products:
            for i in db_products[0]['data']:
                
                #print( f" > {i['canonical']}" )

                new_url = f"https://app-generator.dev{i['canonical']}"
                try:
                    check_response = requests.get(new_url)
                    if check_response.status_code == 200:
                        self.stdout.write(self.style.SUCCESS(f"OK: {new_url}"))
                    else:
                        self.stdout.write(self.style.ERROR(f"Error: {new_url.replace('app-generator.dev','appseed.us')}"))
                except requests.RequestException as e:
                    self.stdout.write(self.style.ERROR(f"Error: {new_url} - {e}"))

        else:
            self.stdout.write(self.style.ERROR(f'Failed to load products file'))
