from django.core.management.base import BaseCommand
from django.db.models import Count
from radiodb.models import *


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--n', type=str, help='Nick del usuario', required = True)
        parser.add_argument('--p', type=str, help='Título del podcast', required = True)

    def handle(self, *args, **kwargs):
        nick = kwargs['n']
        podcast_titulo = kwargs['p']

        try:
            # Buscar usuario por su nick
            usuario = Usuario.objects.get(nik=nick)

            # Buscar el podcast por su título
            podcast = Podcast.objects.get(titulo=podcast_titulo)

            # Verificar si el podcast ya ha sido escuchado por el usuario
            if Lista_Escuchados.objects.filter(usuario=usuario, podcast=podcast).exists():
                self.stdout.write(self.style.WARNING(
                    f'El podcast "{podcast_titulo}" ya ha sido escuchado por {usuario.nik}. No se añadirá a pendientes.'))
                return

            # Verificar si ya está en la lista de pendientes
            if Lista_Pendientes.objects.filter(usuario=usuario, podcast=podcast).exists():
                self.stdout.write(self.style.WARNING(
                    f'El podcast "{podcast_titulo}" ya está en la lista de pendientes de {usuario.nik}.'))
                return

            # Añadir a la lista de pendientes
            Lista_Pendientes.objects.create(usuario=usuario, podcast=podcast)
            self.stdout.write(
                self.style.SUCCESS(f'Podcast "{podcast_titulo}" añadido a la lista de pendientes de {usuario.nik}.'))

        except Usuario.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'No se encontró un usuario con el nick "{nick}".'))
        except Podcast.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'No se encontró un podcast con el título "{podcast_titulo}".'))
