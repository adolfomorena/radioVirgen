from django.core.management.base import BaseCommand
from radiodb.models import *


class Command(BaseCommand):
    help = 'Listar usuarios'

    def handle(self, *args, **kwargs):
        usuarios = list(Usuario.objects.all())

        try:
            if not usuarios:
                self.stdout.write(self.style.WARNING('No hay usuarios registrados en la base de datos.'))
            else:
                for user in usuarios:
                    self.stdout.write(f'Nombre: {user.nombre} - Apellidos: {user.apellidos} - Nik: {user.nik} - ID: {user.id}')

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al listar los usuarios: {e}'))