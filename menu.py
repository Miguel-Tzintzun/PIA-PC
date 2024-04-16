import web_scraping
import port_scanning
import encryption
import hashing
import metadata

def main():
    while True:
        print("\nMenú:")
        print("1. Web Scraping")
        print("2. Escaneo de Puertos")
        print("3. Cifrado y Descifrado de Mensajes")
        print("4. Obtención de Hash")
        print("5. Revisión de Encabezados y Metadatos")
        print("6. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            web_scraping.web_scraping()
        elif opcion == "2":
            port_scanning.port_scanning()
        elif opcion == "3":
            encryption.encryption()
        elif opcion == "4":
            hashing.hashing()
        elif opcion == "5":
            metadata.metadata()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
