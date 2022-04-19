from bs4 import BeautifulSoup
import requests

def main(url):
    # Primero definir la variable con el lnk de la pagina web
    page = requests.get(url)

    # Obtener el codigo html de la pagina
    bSoup = BeautifulSoup(page.content, 'html.parser')

    # Guardar todas las variables en una lista
    links_list = bSoup.find_all('iframe')

    # Ciclo para ver uno por uno los datos especificos
    for link in links_list:

        # el attrs hace que el código sea mucho más fácil y conciso 
        if 'data-src' in link.attrs:

            # Guardar en una variable el primer dato de la lista
            op = str(link.attrs['data-src'])
            
            # Como el navegador no reconoce // toca quitarlo
            op = op.replace('//', '')
            break

    return op

