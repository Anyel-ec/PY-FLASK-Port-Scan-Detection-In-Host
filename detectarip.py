import socket

def obtener_ip():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"Tu dirección IP es: {ip_address}")
    except socket.error as err:
        print(f"No se pudo obtener la dirección IP. Error: {err}")

if __name__ == "__main__":
    obtener_ip()
