#Importamos el modulo web_scraping.py
import web_scraping

def menuwebs():
    url = input("Ingrese la URL: ") #Solicitamos al usuario que ingrese una URL
    url_nueva = web_scraping.verificador_navegacion(url) #llamamos a la función para verificar y corregir la URL ingresada
    html = web_scraping.conexion_request(url_nueva) #Llamada a la función para estabecler una conexión con la pagina web
    
    print(html) #Se imprime el contenido HTML de la página web

#Esta parte asegura que la función 'menuwebs() se ejecute solo si el script se esta ejecutando directamente'
if __name__=='__main__':
    menuwebs()
