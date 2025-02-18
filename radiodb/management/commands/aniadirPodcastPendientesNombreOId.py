from django.core.management.base import BaseCommand
from django.db.models import Q
from radiodb.models import Usuario, Podcast, Lista_Pendientes, Lista_Escuchados

class Command(BaseCommand):
    help = 'Añade un podcast a la lista de pendientes de un usuario (buscado por nombre o ID), verificando que no haya sido escuchado antes'

    def add_arguments(self, parser):
        parser.add_argument('--u', type=str, help='Nombre o ID del usuario', required=True)
        parser.add_argument('--p', type=str, help='Título del podcast', required=True)

    def handle(self, *args, **kwargs):
        usuario_param = kwargs['u']
        podcast_param = kwargs['p']

        try:
            # Buscar usuario por ID o por nombre
            if usuario_param.isdigit():
                usuario = Usuario.objects.filter(id=usuario_param).first()
            else:
                usuario = Usuario.objects.filter(nik=usuario_param).first()
            if not usuario:
                self.stdout.write(self.style.ERROR(f'No se encontró un usuario con el ID o nick "{usuario_param}".'))
                return

            # Buscar el podcast por su título
            podcast = Podcast.objects.filter(titulo=podcast_param).first()
            if not podcast:
                self.stdout.write(self.style.ERROR(f'No se encontró un podcast con el título "{podcast_param}".'))
                return

            # Verificar si el podcast ya ha sido escuchado por el usuario
            if Lista_Escuchados.objects.filter(usuario=usuario, podcast=podcast).exists():
                self.stdout.write(self.style.WARNING(f'El podcast "{podcast_param}" ya ha sido escuchado por {usuario.nik}. No se añadirá a pendientes.'))
                return

            # Verificar si ya está en la lista de pendientes
            if Lista_Pendientes.objects.filter(usuario=usuario, podcast=podcast).exists():
                self.stdout.write(self.style.WARNING(f'El podcast "{podcast_param}" ya está en la lista de pendientes de {usuario.nik}.'))
                return

            # Añadir a la lista de pendientes
            Lista_Pendientes.objects.create(usuario=usuario, podcast=podcast)
            self.stdout.write(self.style.SUCCESS(f'Podcast "{podcast_param}" añadido a la lista de pendientes de {usuario.nik}.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error inesperado: {e}'))
