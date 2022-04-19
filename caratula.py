
import requests
from bs4 import BeautifulSoup

def ob_caratula(url):
    # definir la variable con el lnk de la busqueda
    page = requests.get(url)

    # Obtener el codigo html de la pagina
    bSoup = BeautifulSoup(page.content, 'html.parser')

    # Guardar todas las variables en una lista
    links_list = bSoup.find_all('img')

    # Ciclo para ver uno por uno los datos especificos
    for link in links_list:

        # el attrs hace que el código sea mucho más fácil y conciso 
        if 'data-src' in link.attrs:

            # Guardar en una variable el primer dato de la lista
            op = str(link.attrs['data-src'])

            # Descargar la imagen de forma local 
            #urllib.request.urlretrieve(op, f"temp/image{numero_de_imagen}.png")

            break
    return op
