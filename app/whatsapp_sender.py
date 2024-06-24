# app/whatsapp_sender.py
import os
from dotenv import load_dotenv
from twilio.rest import Client

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Credenciales de Twilio
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_whatsapp_number = os.getenv('FROM_WHATSAPP_NUMBER')
to_whatsapp_number = os.getenv('TO_WHATSAPP_NUMBER')

# Crear el cliente de Twilio
twilio_client = Client(account_sid, auth_token)

# Función para enviar un mensaje de WhatsApp
def send_whatsapp(ip_src):
    message_body = f"⚠️ Alerta de Seguridad: Se ha detectado un posible escaneo de puertos en tu máquina. Fuente del ataque: {ip_src}"
    try:
        message = twilio_client.messages.create(
            body=message_body,
            from_=from_whatsapp_number,
            to=to_whatsapp_number
        )
        print(f"Mensaje de WhatsApp enviado con SID: {message.sid}")
    except Exception as e:
        print(f"Error al enviar el mensaje de WhatsApp: {e}")
