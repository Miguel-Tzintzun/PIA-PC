#Se importa el modulo verify_links
import verify_links

#Definimos la función menuverify
def menuverify(base_url): #tomamos el argumento base_url
    links = verify_links.get_links(base_url) #Se llama a la funcion para obtener todos los enlaces de la página web
    if not links:
        print("No links found on the webpage.")
    else:
        results = verify_links.check_links(links, base_url) #se llama la funcion para verificar cada enlace
        for link, status in results.items():
            print(f"{link}: {status}") #Devuelve un diccionario con el estado de los enlaces, si estan activos o rotos
#luego, se itera sobre los resultados y se imprime cada enlace junto con su estado

if __name__ == "__main__": #Luego se verifica si el script esta siendo ejecutado como un programa principal
    base_url = input("Enter the URL of the webpage: ")
    menuverify(base_url)
