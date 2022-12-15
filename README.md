# Entrega intermedia:
Para correr el programa, realizar los siguientes pasos:

1 Abrir VSCode.

2 Seleccionar Clone git repository

3 Seleccionar o crear una carpeta para el programa.

4 En la terminal ejecuta los comandos:
  python manage.py migrate
  python manage.py runserver
 
5 Ya se puede abrir la pagina que aparece en el texto, tipicamente: http://127.0.0.1:8000/

6  Si quieres tener algunos datos precargados, en la terminal, ejecuta los comandos:
  python manage.py shell
  import seed_data
  
En la web hay 3 tipos de modelos: mi-familia, automoviles y mascotas:
- Agrega las url que ves abajo a la url en la barra de direcciones para utilizarlas, las funciones Alta y Buscar están funcionando, las demás no están aún 100% testeadas.

Ejemplos, reemplaza las URLs antes de mi-familia por las que te aparezcan cuando haces runserver!
Familia

http://127.0.0.1:8000/mi-familia : Para ver los familiares(sólo veras Familiares pre cargados si hiciste el paso 6)
http://127.0.0.1:8000/mi-familia/alta Para crear un familiar nuevo
http://127.0.0.1:8000/mi-familia/buscar Para buscar un familiar

Automoviles

http://127.0.0.1:8000/automoviles/
http://127.0.0.1:8000/automoviles/alta
http://127.0.0.1:8000/automoviles/buscar

Mascotas

http://127.0.0.1:8000/mascotas/
http://127.0.0.1:8000/mascotas/alta
http://127.0.0.1:8000/mascotas/buscar

Muchas gracias!
