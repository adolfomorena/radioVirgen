from django.db import models
from django.db.models import CASCADE


# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nik = models.CharField(max_length=100, unique=True, null=True, blank=True)
    correo = models.EmailField(unique=True)
    fecha_nac = models.DateField()
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"



class MetodosPago(models.Model):
    tipo = models.CharField(max_length=100)
    numeroTarjeta = models.CharField(max_length=16, null=True, blank=True)
    cvc = models.CharField(max_length=3, null=True, blank=True)
    nombreTitular = models.CharField(max_length=100, null=True, blank=True)
    correroTitular = models.EmailField(null=True, blank=True)
    numeroCuenta = models.CharField(max_length=24, null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=CASCADE, null=True, blank=True, related_name='metodos_pago_usuario')
    predeterminado = models.BooleanField()

    def __str__(self):
        return f"{self.tipo} {self.id}"

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(tipo__in=["PagoTarjeta", "Paypal", "Transferencia"]), name='pagos_check')
        ]


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Programa(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    fecha_baja= models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo


class Podcast(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    fecha_baja = models.DateField(null=True, blank=True)
    autores = models.ManyToManyField(Autor, related_name='autores')
    categorias = models.CharField(max_length=100)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, null=True, blank=True, related_name='podcast_programa')
    linkDrive = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(categorias__in=["Educativo", "Comedia", "Formación"]), name='categorias_check')
        ]

class Lista_Pendientes(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=CASCADE, null=True, blank=True,related_name='lista_pendientes_usuario')
    podcast = models.ForeignKey(Podcast, on_delete=CASCADE, null=True, blank=True,related_name='lista_pendientes_podcast')

    def __str__(self):
        return f"{self.usuario} {self.podcast}"

    class Meta:
        unique_together = ['usuario', 'podcast']

class Lista_Escuchados(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=CASCADE, null=True, blank=True,related_name='lista_escuchados_usuario')
    podcast = models.ForeignKey(Podcast, on_delete=CASCADE, null=True, blank=True,related_name='lista_escuchados_podcast')
    fecha_escucha = models.DateField()

    def __str__(self):
        return f"{self.usuario} {self.podcast}"

    class Meta:
        unique_together = ['usuario', 'podcast','fecha_escucha']

class MeGusta_Podcast(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=CASCADE, null=True, blank=True,related_name='megusta_podcast_usuario')
    podcast = models.ForeignKey(Podcast, on_delete=CASCADE, null=True, blank=True,related_name='megusta_podcast_podcast')

    def __str__(self):
        return f"{self.usuario} {self.podcast}"

    class Meta:
        unique_together = ['usuario', 'podcast']

class MeGusta_Programa(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=CASCADE, null=True, blank=True,related_name='megusta_programa_usuario')
    programa = models.ForeignKey(Programa, on_delete=CASCADE, null=True, blank=True,related_name='megusta_programa_programa')

    def __str__(self):
        return f"{self.usuario} {self.programa}"

    class Meta:
        unique_together = ['usuario', 'programa']