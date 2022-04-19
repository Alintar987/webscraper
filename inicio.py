
from os import system as cmd
from tqdm.auto import tqdm
import videos
import obtener
import caratula

cmd('@mode con cols=60 lines=4')
cmd('color 09')

# Inicio del html
DATA = """<!DOCTYPE html
<html>
    <head>
        <title>Peliculas</title>
    </head>
    <body>
"""
# Final del html
DATAB = """
    </body>
</html>"""

# Obtener el dato de la pelicula
op = input('\n Que pelicula quiere ver?: ')

# Sacar links de la pagina de peliculas
links = obtener.main(op)

# Contar peliculas
count = 0
for _ in links:
    count += 1

# Descontar 10 peliculas sugeridas
count -= 10

# Si no se encuentran resultados no crear el html
if count == 0:
    print('\nNo se encontraron resultados. :(')
    input('Intenta escribir bien el nombre...')

# Si hay resultados encontrados crear el html
else:
    print('----------------------- Creando HTML -----------------------')
    
    # Crear archivo html con el inicio
    generar = open(f'{op}.html', 'w')
    generar.write(DATA)
    generar.close()

    # El ciclo va a dar una vuelta por cada resultado 
    for i in tqdm(range(count)):
        
        # Obtener el video de las peliculas
        video = "https://" + videos.main(links[i])

        # Obtener la caratula de las peliculas
        imagen = caratula.ob_caratula(links[i])

        # Crear bloque HTML con video y imagen
        añadir = f"""
            <a href="{video}" target="_blank">
                <img src="{imagen}" alt="">
            </a>
            """
        genera = open(f'{op}.html', 'a') # Abrir HTML en modo añadir
        genera.write(añadir) # añadir el bloque de codigo creado
        genera.close() # Cerrar archivo HTML

        #Barra De progreso
        print("", end='\r')

    # Añadir parte final del HTML
    generar1 = open(f'{op}.html', 'a')
    generar1.write(DATAB)
    generar1.close()

    # Ejecutar HTML creado
    cmd(f'"{op}.html"')