from os import system as cmd
import mechanicalsoup
import link
from tqdm.auto import tqdm

def main(search):
    cmd('cls')
# -------------------------- Buscar -------------------------------------
    # Crear un objeto del navegador 
    browser = mechanicalsoup.StatefulBrowser()

    # Meter pagina web dentro del objeto
    browser.open("https://cuevana3.me/")

    # Seleccionar el formulario de la barra de busqueda
    browser.select_form('form[action="https://cuevana3.me/"]')

    # Poner el nombre asignado al formulario y el texto
    browser["s"] = search
    
    # Dar en buscar o aceptar
    browser.submit_selected()

    # Para obtener la url del sitio
    url = browser.get_url()
# ----------------------------- Obtener peliculas ----------------------------------
    # Obtener los links de las peliculas encontradas de la busqueda
    links = link.ob_links(url)

    return links