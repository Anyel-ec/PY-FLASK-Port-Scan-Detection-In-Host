from scapy.all import sniff
from scapy.layers.inet import TCP, IP
 
# Dirección IP de tu máquina
MY_IP = "192.168.1.7"
 
def detect_port_scan(packet):
    if packet.haslayer(TCP) and packet.haslayer(IP):
        if packet[IP].dst == MY_IP:  
            # Verifica si el paquete tiene solo el flag SYN activado
            if packet[TCP].flags == "S":
                ip_src = packet[IP].src
                tcp_dport = packet[TCP].dport
                print(f"Posible escaneo de puertos detectado desde IP: {ip_src}, en el puerto: {tcp_dport}")
                # Envien msj 
                # enviar emails
                

def main():
    print("Iniciando la detección de escaneo de puertos...")
    # Captura paquetes TCP entrantes hacia tu IP
    sniff(filter=f"tcp and dst host {MY_IP}", prn=detect_port_scan, store=0)

if __name__ == "__main__":
    main() 