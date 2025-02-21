
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


    def handle(self, *args, **kwargs):
        id_param = kwargs['u']


        try:
            metodosList = ["PagoTarjeta", "Paypal", "Transferencia"]
            # Buscar el usuario por su nick
            usuario = Usuario.objects.get(id=id_param)
            self.stdout.write(self.style.SUCCESS(f'Usuario encontrado: {usuario.nombre} {usuario.apellidos}'))

            # Obtener las reproducciones del usuario
            metodos = MetodosPago.objects.filter(usuario=usuario)


            if metodos.exists():
                self.stdout.write(self.style.SUCCESS(f'Reproducciones de {usuario.nik}:'))
                for m in metodos:
                    if m.tipo == metodosList[0]:
                        self.stdout.write(
                            f"- Metodo: {m.tipo} "
                            f"(Numero Tarjeta: {m.numeroTarjeta})"
                            f"(CVC: {m.cvc})"
                            f"(Nombre del Titular: {m.nombreTitular})"
                        )
                    elif m.tipo == metodosList[1]:
                        self.stdout.write(
                            f"- Metodo: {m.tipo} "
                            f"(Correo: {m.correroTitular})"
                        )
                    elif m.tipo == metodosList[2]:
                        self.stdout.write(
                            f"- Metodo: {m.tipo} "
                            f"(Numero de cuenta: {m.numeroCuenta})"
                            f"(Nombre del Titular: {m.nombreTitular})"
                        )
            else:
                self.stdout.write(self.style.WARNING(f'No se encontraron metodos de pago para el usuario {usuario.nik}.'))
        except Usuario.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'No se encontró un usuario con el nick {nick}.'))