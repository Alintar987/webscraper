# [Webscraper Para Peliculas](https://github.com/Alintar987/webscraper)

Este es un pequeño proyecto que crea archivos `HTML` con peliculas que se puede ejecutar en el navegador sin tener ningun tipo de anuncio, consiste en conseguir las caratulas de las peliculas de un sitio web llamado **[Cuevana3](https://cuevana3.me/)** y crea un html con los links de los videos y lo ejecuta al instante para dejarlo visualizar de forma organizada y sin anuncios.

## Instalacion
Para poder utilizar el script debemos descargar el proyecto y los requerimientos en un ambiente virtual.

Primero tenemos que descargar el proyecto con:
```bash
git clone https://github.com/Alintar987/webscraper.git
```
Es recomendable crear un ambiete virtual para mantener todo en una misma carpeta para eso nos movemos a la ruta con **[cd](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cd)** y ponemos el siguiente comando:
```bash
py -m venv venv
```
Activamos el ambiente virtual escribiendo el siguiente comando:
```bash
.\venv\Scripts\activate.bat
```
Ahora descargamos los requerimientos para eso usamos el comando:
```bash
pip install -r requirements.txt
```

## Como usar
para utilizarlo es bastante sencillo

el archivo principal es inicio.py para ejecutarlo desde el ambiente virtual basta con poner:
```bash
py inicio.py
```
luego va a salir un recuadro preguntando la pelicula ponemos el nombre de la pelicula y este busca en la pagina si se encuentran varios resultados agrega todo creando un archivo html y luego abriendolo en el navegador.

## Plantilla del archivo html
cuando nos crea el archivo HTML con los resultados agrega al `body` un `a` y dentro del `href` se almacena el link de la pelicula y crea un `img` y al `src` le pasa como parametro la caratula de la pelicula, el parametro `target="_blank"` es para que se abra en otra pestaña del navegador.
```html
<!DOCTYPE html
<html>
    <head>
        <title>Peliculas</title>
    </head>
    <body>
        <a href="" target="_blank">
            <img src="" alt="">
        </a>
    </body>
</html>
```

## Ejemplo 
podemos ver que hay un archivo `ejemplo.html` lo podemos abrir en el navegador donde muestra como queda el resultado de los archivos HTML que crea el script.

## Librerias
Las librerias usadas en este pequeño proyecto son:

- **[requests](https://pypi.org/project/requests/)**
- **[BeautifulSoup](https://pypi.org/project/BeautifulSoup/)**
- **[tqdm](https://pypi.org/project/tqdm/)**
- **[os](https://docs.python.org/3/library/os.html)**
- **[mechanicalsoup](https://pypi.org/project/MechanicalSoup/)**
