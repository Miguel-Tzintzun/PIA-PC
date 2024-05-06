#! python3 #Indicamos que el script debe ser ejecutado utilizando Python3


import requests #Se importa para realizar operaciones de solicitud HTTP
from bs4 import BeautifulSoup #Se importa para el analisis de HTML
from urllib.parse import urljoin #Se importa para la manipulación de URL



def get_links(url):
    try:
        #tomamos una url como entrada
        response = requests.get(url) #Realizamos una solicitud HTTP a esa URL utilizando request.get
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []
        #Encuentra todos los elementos <a> (enlaces) en la página
        for link in soup.find_all('a'):
            href = link.get('href') #Extraemos el atributo 'href' de cada uno para obtener la URL
            if href:
                links.append(href)
        return links #Retorna una lista de todas las URLs encontradas en la página.
    except requests.exceptions.RequestException as e:
        print("Error fetching the webpage:", e)
        return []

def check_links(links, base_url):
    results = {} #Se toma una lista de URLs y una URL base como entrada.
    for link in links: #Itera sobre cada URL en la lista
        if link.startswith('http'): #Si comienza con http, la deja como está
            url = link
        else:
            url = urljoin(base_url, link) #en caso contrario utilizar urljoin para contruir una URL absoluta
        try:
            response = requests.get(url) #Solicitud de HTTP a cada URL utilizando requests.get()
            if response.status_code == 200: #Si el estado es 200, el enlace es válido y se almacena como OK
                results[url] = 'OK'
            else:
                results[url] = 'Broken' #en caso contrario reciberemos una noticia para el usuario ya que es un link roto y puede ser no seguro
        except requests.exceptions.RequestException:
            results[url] = 'Error' #Si ocurre un error en la solicitud, se registra como un 'Error'
    return results #retorna un diccionario con los resultados de la verificación de los enlaces
