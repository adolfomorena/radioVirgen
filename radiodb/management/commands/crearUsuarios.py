from django.core.management.base import BaseCommand
from radiodb.models import *
from faker import Faker


class Command(BaseCommand):
    help = 'Usuarios'

    def handle(self, *args, **kwargs):
        try:
            fake = Faker()

            for i in range(10):
                nombre = fake.name()
                apellidos = fake.last_name()
                nik = fake.user_name()
                correo = fake.email()
                fecha_nac = fake.date_between(start_date='-40y', end_date='-18y')
                fecha_registro = fake.date_between(start_date='-5y', end_date='today')

                Usuario.objects.create(
                    nombre=nombre,
                    apellidos=apellidos,
                    nik=nik,
                    correo=correo,
                    fecha_nac=fecha_nac,
                    fecha_registro=fecha_registro
                )

            self.stdout.write(self.style.SUCCESS('10 usuarios han sido insertados exitosamente.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al insertar usuarios: {e}'))