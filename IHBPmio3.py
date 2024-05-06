import random
import requests
import os
import json
import random 

api_key= 'ec1e2ebed1754f1b8c00f2b90aa15905'
def get_vul(correo):
	url_api="https://haveibeenpwned.com/api/v3/breachedaccount/" + correo #reutilizacion dela api
	headers = {
		"hibp-api-key": api_key 
	}
	
	response = requests.get(url_api, headers=headers)
	if response.status_code==200: 
		return response.json()
	else:
		return None

#creacion directorio 	
directorio_bulnerabilidades = 'bulneabilidades'
if not os.path.exists(directorio_bulnerabilidades):
    os.makedirs (directorio_bulnerabilidades)

#insertar correo
correo = input("Ingrese el correo electronico que desea investigar")#'falso@hotmail.com'
vul=get_vul(correo)

#############
if vul:
     print("Se han encontrado vulnerabilidades en el correo")
     with open(f"{directorio_bulnerabilidades}/Vulnerabilidades.txt", "a") as file:
                file.write(f"Correo vulnerado: {correo}\n")
                print(vulne["Name"])
                for vulne in vul:
                    file.write(f"-{vulne['Name']}\n")
                    print(vulne['Name'])
                               
                ##contraseñas#
                minusculas="abcdefghijklmnopqrstuvwxyz"
                mayusculas="QWERTYUIOPASDFGHJKLÑZXCVBNM"
                numeros="1234567890"
                simbolos="#%&@~"

                todas= minusculas+mayusculas+numeros+simbolos
                longitud=12

                for o in range(5):
                        muestra=random.sample(todas, longitud)
                        #print(muestra)
                        contraseña="".join(muestra)
                        print("podrias cambiar tu contraseña por:", contraseña)


else:
             print(f"No se ha encontrado vulnerabilidades para: {correo}")
             print("****        ****")
             print("****        ****")
             print("    -_____-      ")



#carita feliz en grande 









