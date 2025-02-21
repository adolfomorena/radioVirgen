from django.core.management.base import BaseCommand
from django.db.models import Count
from radiodb.models import *


class Command(BaseCommand):


    def handle(self, *args, **kwargs):
        try:

            metodos = ["PagoTarjeta", "Paypal", "Transferencia"]
            usuario  = Usuario.objects.filter(id="1").first()


            transferencia = MetodosPago(
                tipo=metodos[2],
                numeroCuenta="ES1234567891234567",
                nombreTitular=usuario.nombre + " " + usuario.apellidos,
                usuario=usuario,
                predeterminado=False
            )
            transferencia.save()

            self.stdout.write(self.style.SUCCESS(f'Metodo Transferencia añadida correctamente'))

            tarjeta = MetodosPago(
                tipo=metodos[0],
                numeroTarjeta="14656456",
                cvc="123",
                nombreTitular=usuario.nombre + " " + usuario.apellidos,
                usuario=usuario,
                predeterminado=False
            )
            tarjeta.save()
            self.stdout.write(self.style.SUCCESS(f'Metodo Tarjeta añadida correctamente'))

            paypal = MetodosPago(
                tipo=metodos[1],
                correroTitular="asda@gmail.com",
                usuario=usuario,
                predeterminado=True)
            paypal.save()
            self.stdout.write(self.style.SUCCESS(f'Metodo Paypal añadida correctamente'))

        except Usuario.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'No se encontró un usuario con id: {1}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al cargar metodos de pago: {e}'))