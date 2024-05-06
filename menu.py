import menuwebs 
import menuverify
#imports


"""Definimos la función main() que será la función principal del programa,
el bucle while True garantiza que el menú se mantega mostrande indefinidamente hasta que el
usuario decida salir"""
def main():
    while True:
#Imprime el menú en la consola con varias opciones que el usuario elija
        print("\nMenú:")
        print("1. Web Scraping")
        print("2. Verificador de URLs")
        print("3. ")
        print("4. ")
        print("5. ")
        print("6. ")
        print("7. Salir")

#Solicitamos al usuario que ingrese la opcion
        opcion = input("\nSelecciona una opción: ")

        try:
            if opcion == "1":
                menuwebs.menuwebs()
            elif opcion == "2":
                base_url = input("Enter the URL of the webpage: ")
                menuverify.menuverify(base_url)
            elif opcion == "3":
                ()
            elif opcion == "4":
                ()
            elif opcion == "5":
                ()
            elif opcion == "6":
                ()
            elif opcion == "7":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
#Maneja cualquier excepción que pueda ocurrir durante a ejecución del codigo e imprime un mensaje de error
        except Exception as e:
            print(f"Er1ror: {e}")

"""Esta linea verifica si el scriptse está ejecunado directamente y,
 si es así, llama a la función main() para iniciar el programa"""
if __name__ == "__main__":
    main()
    
