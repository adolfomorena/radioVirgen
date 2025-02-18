from django.core.management.base import BaseCommand
from radiodb.models import *

class Command(BaseCommand):
    help = 'delete podcast'

    def handle(self, *args, **kwargs):
        try:
            Podcast.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('podcast eliminados.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al eliminar podcasts: {e}'))

