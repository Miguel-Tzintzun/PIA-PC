import requests #Se importa para realizar operaciones de solicitud HTTP
from bs4 import BeautifulSoup #Se importa para el analisis de HTML
from urllib.parse import urljoin #Se importa para la manipulación de URL



def get_links(url):
    try:
        #tomamos una url como entrada
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                links.append(href)
        return links
    except requests.exceptions.RequestException as e:
        print("Error al recuperar la página web:", e)
        return []


def check_links(links, base_url):
    results = {} #Se toma una lista de URLs y una URL base como entrada.
    for link in links: #Itera sobre cada URL en la lista
        if link.startswith('http'): #Si comienza con http, la deja como está
            url = link
        else:
            url = urljoin(base_url, link)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                results[url] = 'OK'
            else:
                results[url] = 'Broken'
        except requests.exceptions.RequestException:
            results[url] = 'Error'
    return results #retorna un diccionario con los resultados
