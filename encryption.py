from cryptography.fernet import Fernet

def encryption():
    # Generar una clave de cifrado aleatoria
    clave = Fernet.generate_key()

    # Crear un objeto Fernet con la clave generada
    cipher_suite = Fernet(clave)

    # Mensaje a cifrar
    mensaje_original = "¡Hola, este es un mensaje secreto!"

    # Cifrar el mensaje
    mensaje_cifrado = cipher_suite.encrypt(mensaje_original.encode())

    print("Mensaje cifrado:", mensaje_cifrado)

    # Descifrar el mensaje
    mensaje_descifrado = cipher_suite.decrypt(mensaje_cifrado).decode()

    print("Mensaje descifrado:", mensaje_descifrado)
    pass
