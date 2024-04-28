import menuwebs
#imports

def main():
    while True:
        print("\nMenú:")
        print("1. Web Scraping")
        print("2. ¿La URL es segura?")
        print("3. Enviar PDF a un sms")
        print("4. ")
        print("5. ")
        print("6. ")
        print("7. Salir")

        opcion = input("\nSelecciona una opción: ")

        try:
            if opcion == "1":
                menuwebs.menuwebs()
            elif opcion == "2":
                ()
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
        except Exception as e:
            print(f"Er1ror: {e}")

if __name__ == "__main__":
    main()
