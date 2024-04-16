import socket

def port_scanning():
    # Función para escanear un puerto específico en un host
    def scan_port(host, port):
        try:
            # Crear un objeto de socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Establecer un tiempo de espera para la conexión
            s.settimeout(1)
            # Intentar conectar al puerto en el host
            result = s.connect_ex((host, port))
            # Si el resultado es 0, el puerto está abierto
            if result == 0:
                print(f"El puerto {port} está abierto")
            else:
                print(f"El puerto {port} está cerrado")
            # Cerrar el socket
            s.close()
        except socket.error as e:
            print(f"Error al escanear el puerto {port}: {e}")

    # Especificar el host a escanear y el rango de puertos
    host = '127.0.0.1'  # Puedes cambiar esto por la dirección IP o el nombre de dominio que desees escanear
    puertos_a_escanear = range(1, 1025)  # Escanea los puertos del 1 al 1024 (puertos comunes)

    # Escanear cada puerto en el rango especificado
    for puerto in puertos_a_escanear:
        scan_port(host, puerto)

    pass
