#Importamos el modulo web_scraping.py
import web_scraping


def menuwebs():


    url = input("Ingrese la URL: ") #Solicitamos al usuario que ingrese una URL
    url_nueva = web_scraping.verificador_navegacion(url) 
    html = web_scraping.conexion_request(url_nueva) 
    print(html)


if __name__=='__main__':
    menuwebs()
