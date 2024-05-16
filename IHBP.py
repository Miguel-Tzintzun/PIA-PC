import random
import requests
import os
import logging
from datetime import datetime
import time


def IHBP():

    # Configuración de logging
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    log_file = 'consulta_correos.log'
    logging.basicConfig(filename=log_file, level=logging.INFO, format=log_format)

    api_key = 'a088638961ba4831aa70ea60271ab16b'


    def get_vul(correo):
        try:

            url_api = "https://haveibeenpwned.com/api/v3/breachedaccount/" + correo
            headers = {

                "hibp-api-key": api_key 

            }
            
            response = requests.get(url_api, headers = headers)
            response.raise_for_status()  # Esto generará una excepción
            if response.status_code == 200: 
                return response.json()

            elif response.status_code == 404:
                print("La API no encontró ninguna información.")
                return None

            else:
                print(f"Error al realizar la solicitud a la API. Código de estado: {response.status_code}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Error al conectarse a la API: {e}")
            return None

    directorio_vulnerabilidades = 'vulnerabilidades'
    if not os.path.exists(directorio_vulnerabilidades):
        os.makedirs(directorio_vulnerabilidades)

    # Temporizador de 7 segundos
    print("Bienvenido al programa de consulta de vulnerabilidades.")
    print("El programa se iniciará en 7 segundos.")
    time.sleep(7)

    # Registro del correo ingresado y la hora de la consulta
    correo = input("Ingrese el correo electrónico que desea investigar: ")
    logging.info(f"Consulta de vulnerabilidades para el correo '{correo}' realizada a las {datetime.now()}")

    vul = get_vul(correo)

    if vul:

        print("Se han encontrado vulnerabilidades en el correo")
        with open(f"{directorio_vulnerabilidades}/Vulnerabilidades.txt", "a") as file:
            file.write(f"Correo vulnerado: {correo}\n")
            for vulne in vul:
                print(vulne['Name'])
                file.write(f" - {vulne['Name']}\n")

            # Generar contraseñas sugeridas
            minusculas = "abcdefghijklmnopqrstuvwxyz"
            mayusculas = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
            numeros = "1234567890"
            simbolos = "#%&@~"

            todas = minusculas + mayusculas + numeros + simbolos
            longitud = 12

            for _ in range(5):
                muestra = random.sample(todas, longitud)
                contraseña = "".join(muestra)
                print("Podrías cambiar tu contraseña por:", contraseña)

    else:

        print(f"No se ha encontrado vulnerabilidades para: {correo}")
        print("   *****   ")
        print(" *       * ")
        print("*  O   O  *")
        print("*    ^    *")
        print(" *  \_/  * ")
        print("   *****   ")


