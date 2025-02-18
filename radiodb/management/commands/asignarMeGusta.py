from django.core.management.base import BaseCommand
from radiodb.models import *


class Command(BaseCommand):
    help = 'Me Gusta'

    def add_arguments(self, parser):
        parser.add_argument('--u', type=str, help='Introduce el ID del usuario', required=True)
        parser.add_argument('--p', type=str, help='Introduce el ID del podcast')

    def handle(self, *args, **kwargs):
        id_usuario = kwargs['u']
        id_podcast = kwargs.get('p')

        try:
            usuario = Usuario.objects.get(id=id_usuario)

            if id_podcast:
                podcast = Podcast.objects.get(id=id_podcast)

                megusta = MeGusta_Podcast.objects.create(usuario_id=id_usuario, podcast_id=id_podcast)

                if megusta:
                   self.stdout.write(self.style.SUCCESS(f'Se ha añadido el podcast {podcast.titulo} a Me Gusta'))
                else:
                    self.stdout.write(
                        self.style.ERROR(f'No se ha podido añadir el podcast {podcast.titulo} a Me Gusta'))

            else:
                megusta = MeGusta_Podcast.objects.filter(usuario=id_usuario)
                if megusta.exists():
                    self.stdout.write(f"Podcasts que le gustan al usuario {usuario.nombre} {usuario.apellidos}:")
                    for m in megusta:
                        self.stdout.write(f"  - ID: {m.podcast.id} - Título: {m.podcast.titulo}")
                else:
                    self.stdout.write(f"El usuario {usuario.nombre} no tiene podcasts marcados como Me Gusta.")


        except Usuario.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'No se encontró el usuario con id: {id_usuario}'))

        except Podcast.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'No se encontró el podcast con id: {id_podcast}'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al añadir Me Gusta: {e}'))
