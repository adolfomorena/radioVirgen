from django.core.management.base import BaseCommand

from django.core.management.base import BaseCommand
from django.db.models import Count
from radiodb.models import *

class Command(BaseCommand):
    help = 'Lista las reproducciones de un usuario basado en su nick'

    def add_arguments(self, parser):
        parser.add_argument(
            '--n',
            type=str,
            help='Nick del usuario',
            required=True
        )

    def handle(self, *args, **kwargs):
        nick = kwargs['n']  # Obtenemos el nick del usuario

        try:
            # Buscar el usuario por su nick
            usuario = Usuario.objects.get(nik=nick)
            self.stdout.write(self.style.SUCCESS(f'Usuario encontrado: {usuario.nombre} {usuario.apellidos}'))

            # Obtener las reproducciones del usuario
            reproducciones = Lista_Escuchados.objects.filter(usuario=usuario).select_related('podcast')


            if reproducciones.exists():
                self.stdout.write(self.style.SUCCESS(f'Reproducciones de {usuario.nik}:'))
                for reproduccion in reproducciones:
                    self.stdout.write(
                        f"- Podcast: {reproduccion.podcast.titulo} "
                        f"(Fecha de escucha: {reproduccion.fecha_escucha})"
                    )
            else:
                self.stdout.write(self.style.WARNING(f'No se encontraron reproducciones para el usuario {usuario.nik}.'))
        except Usuario.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'No se encontró un usuario con el nick {nick}.'))