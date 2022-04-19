import requests
from bs4 import BeautifulSoup

def ob_nombre(website):

    result = requests.get(website)
    content = result.text

    soup = BeautifulSoup(content, "lxml")

    title = soup.find("h1").get_text()

    title = title.replace("á", "a")
    title = title.replace("é", "e")
    title = title.replace("í", "i")
    title = title.replace("ó", "o")
    title = title.replace("ú", "u")

    title = title.replace("Á", "A")
    title = title.replace("É", "E")
    title = title.replace("Í", "I")
    title = title.replace("Ó", "O")
    title = title.replace("Ú", "U")

    return title