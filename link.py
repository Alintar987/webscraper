from bs4 import BeautifulSoup
import requests

def ob_links(url):
    pelis = []

    # definir la variable con el lnk de la busqueda
    page = requests.get(url)

    # Obtener el codigo html de la pagina
    bSoup = BeautifulSoup(page.content, 'html.parser')

    # Guardar todas las variables en una lista
    links_list = bSoup.find_all('a')

    # Ciclo para ver uno por uno los datos especificos
    for link in links_list:

        # el attrs hace que el código sea mucho más fácil y conciso 
        if 'href' in link.attrs:

            # Guardar en una variable el primer dato de la lista
            op = str(link.attrs['href'])
            
            # Dividir el link en / para obtener solo peliculas
            div = op.split('/')

            # Omitir error de que el link es muy pequeño para abrirlo
            try:
                search = div[3]

                # Detectar si en el link en la posicion 3 hay un numero
                # si no hay numero eleva un error
                try:
                    # Convertir el texto de la 3 seccion del link en numero
                    search = int(search)

                    # Guardar en lista general link de peliculas
                    pelis.append(op)
                    
                    # Omite el error si no puede convertir un texto el numero
                except:
                    pass

            except IndexError:
                pass

    return pelis