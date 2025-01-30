from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Autor)
admin.site.register(Programa)
admin.site.register(Podcast)
admin.site.register(Lista_Pendientes)
admin.site.register(Lista_Escuchados)
admin.site.register(MeGusta_Podcast)
admin.site.register(MeGusta_Programa)