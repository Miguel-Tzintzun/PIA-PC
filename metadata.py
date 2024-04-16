import exifread

def metadata():
    # Función para revisar los encabezados y metadatos de un archivo de imagen
    def revisar_encabezados_y_metadatos(archivo_path):
        try:
            # Abrir el archivo en modo binario
            with open(archivo_path, 'rb') as f:
                # Leer los encabezados y metadatos utilizando exifread
                tags = exifread.process_file(f)
                # Imprimir los encabezados y metadatos
                for tag, value in tags.items():
                    print(f"{tag}: {value}")
        except FileNotFoundError:
            print("Error: El archivo especificado no fue encontrado.")
        except PermissionError:
            print("Error: Permiso denegado para acceder al archivo.")

    # Ejemplo de uso
    archivo_path = 'ruta/a/imagen.jpg'  # Reemplaza 'ruta/a/imagen.jpg' con la ruta de tu archivo de imagen
    revisar_encabezados_y_metadatos(archivo_path)

    pass
