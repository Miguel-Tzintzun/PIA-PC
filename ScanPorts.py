import socket
import sys
import logging

logging.basicConfig(filename='error_puerto.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_ports(ip_address):
    port_check = [-1, 21, 22, 25, 80, 443]  
    results = []
    logging.info(f"Verificando puertos abiertos en {ip_address}.")
    for port in port_check:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((ip_address, port))
                status = "Abierto" if result == 0 else "Cerrado"
                results.append((port, status))
                logging.info(f"Puerto {port}: {status}")
        except Exception as e:
            results.append((port, "Error"))
            logging.error(f"Error al verificar el puerto {port}: {e}")
    return results

ip_address = sys.argv[1]
print(f"Dirección IP: {ip_address}")
print("Puertos:")
results = check_ports(ip_address)
for port, status in results:
    print(f"Puerto {port}: {status}")
