#Se importa el modulo verify_links
import verify_links


def menuverify(base_url): #tomamos el argumento base_url  

    links = verify_links.get_links(base_url) 

    if not links:
        print("No se encontraron links en la página web.")
    else:
        results = verify_links.check_links(links, base_url)
        for link, status in results.items():
            print(f"{link}: {status}") 

if __name__ == "__main__":

    base_url = input("Ingresa la URL de la página web: ")
    menuverify(base_url)

