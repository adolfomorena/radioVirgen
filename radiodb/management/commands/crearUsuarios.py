from django.core.management.base import BaseCommand
from radiodb.models import *
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Podcast'

    def handle(self, *args, **kwargs):
        try:
            fake = Faker()

            

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al cargar usuarios: {e}'))