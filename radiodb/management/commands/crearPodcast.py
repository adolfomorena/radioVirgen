from django.core.management.base import BaseCommand
from radiodb.models import *
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Podcast'

    def handle(self, *args, **kwargs):
        try:
            fake = Faker()
            todos_autores = list(Autor.objects.all())
            programas = list(Programa.objects.all())
            cont = 1

            while cont <=300:
                titulo = fake.sentence(nb_words=4)
                fecha_publicacion = fake.date_between(start_date='-5y', end_date='today')
                categorias = random.choice(["Educativo", "Comedia", "Formación"])
                link = f"http://www.drive{cont}.com"

                nuevos_autores = random.sample(todos_autores, random.randint(1, 5))
                programa_nuevo = random.choice(programas)

                # Si ya existe un podcast que involucre alguno de estos autores en el mismo programa, se salta la creación
                if Podcast.objects.filter(autores__in=nuevos_autores, programa=programa_nuevo).exists():
                    continue

                podcast = Podcast(
                    titulo=titulo,
                    fecha_publicacion=fecha_publicacion,
                    categorias=categorias,
                    linkDrive=link
                )
                podcast.save()
                podcast.autores.set(nuevos_autores)
                cont+=1
                '''
                
                if len(lista_podcast_autores_repe) == 0:
                    podcast = Podcast(
                        titulo=titulo,
                        fecha_publicacion=fecha_publicacion,
                        categorias=categorias,
                        linkDrive = link
                    )
                    podcast.save()
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
                                categorias=categorias,
                                linkDrive=link,
                                programa = programa_nuevo
                            )
                            podcast.save()
                            podcast.autores.set(random.sample(todos_autores, random.randint(1, 5)))
                            podcast.save()
                            cont+=1

                '''

            self.stdout.write(self.style.SUCCESS('300 podcasts han sido cargados exitosamente.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al cargar podcasts: {e}'))

