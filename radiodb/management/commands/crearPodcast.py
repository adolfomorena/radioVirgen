from django.core.management.base import BaseCommand
from radiodb.models import *
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Podcast'

    def handle(self, *args, **kwargs):
        try:
            fake = Faker()
            todos_autores = Autor.objects.all()
            cont = 0

            while cont <=300:
                titulo = fake.sentence(nb_words=4)
                fecha_publicacion = fake.date_between(start_date='-5y', end_date='today')
                duracion = random.randint(10, 180)
                categoria = random.choice(["Educativo", "Comedia", "Formación"])
                link = fake.url()

                nuevos_autores = random.sample(todos_autores, random.randint(1, 5))

                lista_podcast_autores_repe = Podcast.objects.filter(autores__in=[autor for autor in nuevos_autores])

                programa_nuevo = random.choice(Programa.objects.all())

                if len(lista_podcast_autores_repe) == 0:
                    podcast = Podcast(
                        titulo=titulo,
                        fecha_publicacion=fecha_publicacion,
                        duracion=duracion,
                        categoria=categoria,
                        link = link
                    )
                    podcast.autores.set(nuevos_autores)
                    podcast.programa = programa_nuevo
                    podcast.save()
                    cont+=1

                else:
                    for podcast in lista_podcast_autores_repe:
                        if podcast.programa == programa_nuevo:
                            break
                        else:
                            podcast = Podcast(
                                titulo=titulo,
                                fecha_publicacion=fecha_publicacion,
                                duracion=duracion,
                                categoria=categoria,
                                link=link,
                                programa = programa_nuevo
                            )
                            podcast.autores.set(random.sample(todos_autores, random.randint(1, 5)))
                            podcast.save()
                            cont+=1

            self.stdout.write(self.style.SUCCESS('300 podcasts han sido cargados exitosamente.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al cargar podcasts: {e}'))

