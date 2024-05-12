import argparse
import menuwebs 
import menuverify
import script

def main():
    parser = argparse.ArgumentParser(description="Este es un programa con varias opciones.")
    parser.add_argument('-w', '--webscraping', action='store_true', help='Realizar Web Scraping')
    parser.add_argument('-u', '--urlverify', metavar='URL', help='Verificar una URL')
    parser.add_argument('-p', '--portscan', action='store_true', help='Escanear Puertos')
    parser.add_argument('-m', '--metadata', action='store_true', help='Mostrar Metadatos')
    parser.add_argument('-hp', '--haveibeenpwned', action='store_true', help='Consultar si una cuenta ha sido comprometida')
    parser.add_argument('-a', '--automate', action='store_true', help='Automatización de Análisis de Malware')

    args = parser.parse_args()

    if args.webscraping:
        menuwebs.menuwebs()
    elif args.urlverify:
        menuverify.menuverify(args.urlverify)
    elif args.portscan:
        # Lógica para la opción de escanear puertos
        pass
    elif args.metadata:
        # Lógica para la opción de mostrar metadatos
        pass
    elif args.haveibeenpwned:
        # Lógica para la opción de Have I been Pwned
        pass
    elif args.automate:
        script.script()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
