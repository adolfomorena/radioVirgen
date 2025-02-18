# radioVirgen
superuser=fran
password=1234



# Comando Django: Insertar Autores con Faker

## Descripción

Este comando genera e inserta **30 registros de autores** en la base de datos de la aplicación `radiodb` utilizando la biblioteca `Faker`.


## Comando
```sh
python manage.py crearAutores
```

# Comando Django: Insertar Usuarios con Faker

## Descripción

Este comando genera e inserta 10 usuarios en la base de datos de la aplicación `radiodb` utilizando la biblioteca `Faker`.


## Comando
```sh
python manage.py crearUsuarios
```





# Comando Django: Insertar Podcasts con Faker

## Descripción

Este comando genera e inserta **300 registros de podcasts** en la base de datos de la aplicación `radiodb` utilizando la biblioteca `Faker`. 
Cada podcast se asocia aleatoriamente con autores y programas existentes.

## Comando

```sh
python manage.py crearPodcasts
```
# Comando Django: Añadir Podcast a Lista de Pendientes

## Descripción

Este comando permite añadir un **podcast** a la lista de pendientes de un usuario en la base de datos de `radiodb`. Antes de añadirlo, se realizan verificaciones para evitar duplicados en la lista de escuchados y pendientes.

## Uso del Comando

```sh
python manage.py aniadirPodcastAPendientes --n "nick_usuario" --p "titulo_podcast"
```
# Comando Django: Añadir Podcast a Lista de Pendientes por nick o id

## Descripción

Este comando permite añadir un **podcast** a la lista de pendientes de un usuario en la base de datos de `radiodb`. Antes de añadirlo, se realizan verificaciones para evitar duplicados en la lista de escuchados y pendientes.
## Uso del Comando
```sh
python manage.py aniadirPodcastPendientesNombreOId --n "nick_usuario_O_id" --p "titulo_podcast"
```

# Comando Django: Listar reproducciones por nick

## Descripción

Este comando lista las resproducciones del usuario pasandole su nick por parametro
## Uso del Comando
```sh
python manage.py reproduccionesNick --n "nick_usuario" 
```
