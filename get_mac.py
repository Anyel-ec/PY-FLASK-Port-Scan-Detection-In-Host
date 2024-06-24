import requests

def get_mac_details(mac_address):
    url = f"https://api.macvendors.com/{mac_address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return "No se pudo obtener la información del fabricante."
    except requests.RequestException as e:
        return f"Se produjo un error al consultar la API: {e}"

if __name__ == "__main__":
    mac_address = input("Introduce la dirección MAC del dispositivo: ")
    details = get_mac_details(mac_address)
    print(f"Información del fabricante para la MAC {mac_address}: {details}")
