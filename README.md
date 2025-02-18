# radioVirgen
superuser=fran
password=1234


# 1-a. Comando Django: Insertar Autores con Faker

## Descripción

Este comando genera e inserta **30 registros de autores** en la base de datos de la aplicación `radiodb` utilizando la biblioteca `Faker`.
### Autor 
Adolfo

## Comando
```sh
python manage.py crearAutores
```


# 1-b. Comando Django: Insertar Podcasts con Faker

## Descripción

Este comando genera e inserta **300 registros de podcasts** en la base de datos de la aplicación `radiodb` utilizando la biblioteca `Faker`. 
Cada podcast se asocia aleatoriamente con autores y programas existentes.
### Autor 
Adolfo
## Comando

```sh
python manage.py crearPodcasts
```


# 1-c. Comando Django: Insertar Usuarios con Faker

## Descripción

Este comando genera e inserta 10 usuarios en la base de datos de la aplicación `radiodb` utilizando la biblioteca `Faker`.
### Autor 
Adolfo

## Comando
```sh
python manage.py crearUsuarios
```


# 2. Comando Django: Listar datos de todos los Usuarios

## Descripción

Este comando lista los datos de todos los usuarios en la base de datos de la aplicación `radiodb`.
### Autor 
Adolfo

## Comando
```sh
python manage.py listarUsuarios
```


# 3. Comando Django: Listar reproducciones por nick

## Descripción

Este comando lista las resproducciones del usuario pasandole su nick por parametro.
### Autor 
Manuel
## Uso del Comando
```sh
python manage.py reproduccionesNick --n "nick_usuario" 
```


# 4. Comando Django: Añadir Podcast a Lista de Pendientes

## Descripción

Este comando permite añadir un **podcast** a la lista de pendientes de un usuario en la base de datos de `radiodb`. Antes de añadirlo, se realizan verificaciones para evitar duplicados en la lista de escuchados y pendientes.
### Autor 
Manuel
## Uso del Comando

```sh
python manage.py aniadirPodcastAPendientes --n "nick_usuario" --p "titulo_podcast"
```

# 5. Comando Django: Añadir un Podcast a la lista Me Gusta por id 

## Descripción

Este comando añade un registro en la lista me gusta, pasando un id de usuario y un id de podcast, 
en caso de pasar solo el id de un usuario mostrara los me gusta que tiene ese usuario en la base de datos de la aplicación `radiodb`.
### Autor 
Adolfo

## Comando
```sh
python manage.py asignarMeGusta
```


# 6. Comando Django: Añadir Podcast a Lista de Pendientes por nick o id

## Descripción

Este comando permite añadir un **podcast** a la lista de pendientes de un usuario en la base de datos de `radiodb`. Antes de añadirlo, se realizan verificaciones para evitar duplicados en la lista de escuchados y pendientes.
### Autor 
Manuel
## Uso del Comando
```sh
python manage.py aniadirPodcastPendientesNombreOId --u "nick_usuario_O_id" --p "titulo_podcast"
```


