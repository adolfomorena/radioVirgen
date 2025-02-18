from django.core.management.base import BaseCommand
import random
from radiodb.models import *
from faker import Faker


class Command(BaseCommand):
    help = 'Reproducciones'

    def handle(self, *args, **kwargs):
        fake = Faker()
        usuarios = list(Usuario.objects.all())
        podcasts = list(Podcast.objects.all())

        try:
            for user in usuarios:
                num_repros = random.randint(20,70)
                for i in range (num_repros):
                    podcast = random.choice(podcasts)
                    fecha = fake.date_between(start_date='-5y', end_date='today')
                    Lista_Escuchados.objects.create(
                        usuario=user,
                        podcast=podcast,
                        fecha_escucha=fecha
                    )
            self.stdout.write(self.style.SUCCESS(f'Reproducciones asignadas exitosamente al usuario {user.nik}'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al asignar reproducciones: {e}'))