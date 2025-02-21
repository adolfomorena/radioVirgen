
from django.core.management.base import BaseCommand
from django.db.models import Count
from radiodb.models import *

class Command(BaseCommand):
    help = 'Lista las reproducciones de un usuario basado en su nick'

    def add_arguments(self, parser):
        parser.add_argument(
            '--u',
            type=str,
            help='id del usuario',
            required=True
        )
        parser.add_argument(
            '--m',
            type=str,
            help='id Metodo de pago',
            required=True
        )

    def handle(self, *args, **kwargs):
        id_param = kwargs['u']
        id_pago = kwargs['m']

        try:


            usuario = Usuario.objects.get(id=id_param)
            self.stdout.write(self.style.SUCCESS(f'Usuario encontrado: {usuario.nombre} {usuario.apellidos}'))

            metodoCambio = MetodosPago.objects.get(id=id_pago)
            self.stdout.write(self.style.SUCCESS(f'Metodo encontrado: {metodoCambio.tipo}'))


            metodos = MetodosPago.objects.filter(usuario=usuario)

            for m in metodos:
                m.predeterminado = False
                m.save()

            metodoCambio.predeterminado = True
            metodoCambio.save()
            self.stdout.write(self.style.SUCCESS(f'Metodo de pago cambiado correctamente'))

        except Usuario.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'No se encontró un usuario con el  {id_param}.'))
        except MetodosPago.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'No se encontró un metodo de pago con el id {id_pago}.'))