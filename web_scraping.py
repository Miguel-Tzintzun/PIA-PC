import requests
from bs4 import BeautifulSoup

def web_scraping():
    #URL de la pagina a scrapear
    url = 'https://www.bbc.com/news'

    #Realizar la solicitud GET a la página
    response = requests.get(url)

    #Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        #Parsear el contenido HTML
        soup = BeautifulSoup(response.content, "html.parser")

        #Encontrar todas las etiquetas 'a' que contienen los enlaces a las noticias
        links = soup.find_all('a', class_='gs-c-promo-heading')

        #Imprimir el título y el enlace de cada noticia
        for link in links:
            title = link.text.strip() # Obtener el texto del titulo
            href = link['href']     #Obtener el enlace (atributo href)
            print(f"Título: {title}")
            print(f"Enlace: {href}")
            print("--------")
    else:
        print("Error al cargar la página: ", response.status_code)
    pass

