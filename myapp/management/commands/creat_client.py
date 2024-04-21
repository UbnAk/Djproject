from myapp.models import Client
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create user."
    
    def handle(self, *args, **kwargs):
        # cl = Client(name='John', email='john@example.com',
        # phone_number='88887776655', address='г. Москва')
        cl = Client(name='Maksim', email='maks@example.com',
        phone_number='88911234567', address='г. Ульяновск')
        cl.save()
        self.stdout.write(f'{cl}')
