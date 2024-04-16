import hashlib

def hashing():
    # Función para obtener el hash de un archivo
    def obtener_hash(file_path, algoritmo='sha256'):
        try:
            # Abrir el archivo en modo binario
            with open(file_path, 'rb') as f:
                # Leer el contenido del archivo
                contenido = f.read()
                # Calcular el hash del contenido utilizando el algoritmo especificado
                hash_obj = hashlib.new(algoritmo)
                hash_obj.update(contenido)
                # Obtener el hash en formato hexadecimal
                hash_resultado = hash_obj.hexdigest()
                return hash_resultado
        except FileNotFoundError:
            print("Error: El archivo especificado no fue encontrado.")
        except PermissionError:
            print("Error: Permiso denegado para acceder al archivo.")

    # Ejemplo de uso
    archivo_path = 'ruta/al/archivo.txt'  # Reemplaza 'ruta/al/archivo.txt' con la ruta de tu archivo
    hash_sha256 = obtener_hash(archivo_path)
    print("Hash SHA-256 del archivo:", hash_sha256)
    pass
