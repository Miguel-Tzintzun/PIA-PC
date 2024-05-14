import argparse
import menuwebs 
import menuverify
import subprocess
import Metadata
import IHBP
import script

def main():
    parser = argparse.ArgumentParser(description="PIA PROGRAMACIÓN PARA CIBERSEGURIDAD")
    parser.add_argument('-w', '--webscraping', action='store_true', help='Realizar Web Scraping')
    parser.add_argument('-u', '--urlverify', metavar='URL', help='Verificar una URL')
    parser.add_argument('-p', '--portscan', action='store_true', help='Escanear Puertos')
    parser.add_argument('-m','--metadata', action='store_true', help='Extraer metadatos de las imágenes.')
    parser.add_argument('-hp', '--haveibeenpwned', action='store_true', help='Consultar si una cuenta ha sido usada')
    parser.add_argument('-a', '--automate', action='store_true', help='Automatización de Análisis de Malware')
    args = parser.parse_args()

    if args.webscraping:
        menuwebs.menuwebs()
    elif args.urlverify:
        menuverify.menuverify(args.urlverify)
    elif args.portscan:
        #Ejecutar el script PowerShell
        subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", "CheckPorts3.ps1"])
        pass
    elif args.metadata:
        Metadata.extract_metadata()
        pass
    elif args.haveibeenpwned:
        IHBP.IHBP()
        pass
    elif args.automate:
        script.script()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
