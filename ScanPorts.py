import socket
import sys

#Verificar puerto 25
def check_ports(ip_address):
    ports_to_check = [21, 22, 25, 80, 443]  
    results = []
    print(f"Verificando puertos abiertos en {ip_address}...")
    for port in ports_to_check:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((ip_address, port))
            if result == 0:
                status = "Abierto"
            else:
                status = "Cerrado"
            results.append((port, status))
            s.close()
        except Exception as e:
            results.append((port, "Error"))
    return results
    
ip_address = sys.argv[1]
results = check_ports(ip_address)
for port, status in results:
    print(f"Puerto {port}: {status}")
