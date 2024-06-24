# app/port_scanner.py
from scapy.all import sniff
from scapy.layers.inet import TCP, IP
import threading
from .ip_utils import get_ip
from .email_sender import send_email
import sys

# Dirección IP de tu máquina
MY_IP = get_ip()
print(f"Tu dirección IP es: {MY_IP}")
if not MY_IP:
    print("No se pudo obtener la dirección IP. Terminando el programa.")
    exit(1)

# Conjunto para asegurar que el correo se envíe solo una vez por IP
sent_emails = set()
# Bloqueo para sincronizar el acceso al conjunto sent_emails
sent_emails_lock = threading.Lock()

# Variable para contar los paquetes de escaneo detectados
scan_detected_count = 0

# Función para detectar un escaneo de puertos
def detect_port_scan(packet):
    global scan_detected_count
    if packet.haslayer(TCP) and packet.haslayer(IP):
        if packet[IP].dst == MY_IP:
            # Verifica si el paquete tiene solo el flag SYN activado
            if packet[TCP].flags == "S":
                ip_src = packet[IP].src
                tcp_dport = packet[TCP].dport
                print(f"Posible escaneo de puertos detectado desde IP: {ip_src} en el puerto: {tcp_dport}")
                with sent_emails_lock:
                    if ip_src not in sent_emails:
                        sent_emails.add(ip_src)
                        send_email(ip_src)
                        scan_detected_count += 1
                        update_progress(scan_detected_count)

# Función para actualizar la barra de carga (opcional)
def update_progress(count):
    print(f"Detección en progreso... Paquetes de escaneo detectados: {count}")

# Función principal para iniciar la detección de escaneo de puertos
def start_port_scanner_detection():
    print("Iniciando la detección de escaneo de puertos...")
    sys.stdout.flush()  # Asegura que se imprime el mensaje inmediatamente

    # Captura paquetes TCP entrantes hacia tu IP
    sniff(filter=f"tcp and dst host {MY_IP}", prn=detect_port_scan, store=0)

    print("\nDetección de escaneo de puertos finalizada.")
    sys.stdout.flush()  # Asegura que se imprime el mensaje inmediatamente
