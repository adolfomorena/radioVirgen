from django.core.management.base import BaseCommand
from radiodb.models import *
from faker import Faker


class Command(BaseCommand):
    help = 'Autores'

    def handle(self, *args, **kwargs):
        try:
            fake = Faker()

            for i in range(30):
                nombre = fake.name()
                fecha_registro = fake.date_between(start_date='-5y', end_date='today')

                Autor.objects.create(
                    nombre=nombre,
                    fecha_registro=fecha_registro
                )

            self.stdout.write(self.style.SUCCESS('30 autores han sido insertados exitosamente.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al insertar autores: {e}'))
