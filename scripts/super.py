from os import environ
import django
environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ecommerce.settings')
django.setup()
from django.core.management import BaseCommand
from products.models import Item
import csv


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('file.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                user = Item.objects.get_or_create(price=row[0], title=row[1], description=row[2], is_available=True)
                print(user)


command = Command()
command.handle()
