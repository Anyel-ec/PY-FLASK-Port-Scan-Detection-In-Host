# app/email_sender.py
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
from .whatsapp_sender import send_whatsapp

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Dirección de correo electrónico del remitente
email_sender = os.getenv('SENDER_EMAIL')
# Contraseña del remitente obtenida de las variables de entorno
password = os.getenv('EMAIL_PASSWORD')
# Dirección de correo electrónico del destinatario
email_receiver = os.getenv('RECEIVER_EMAIL')

# Función para enviar un correo electrónico
def send_email(ip_src):
    subject = "⚠️ Alerta de Seguridad: Escaneo de Puertos Detectado ⚠️"
    body = f"""
    <html>
        <body style="font-family: Arial, sans-serif; text-align: center;">
            <div style="border: 2px solid red; padding: 20px; margin: 20px;">
                <h1 style="color: red;">⚠️ Alerta de Seguridad ⚠️</h1>
                <p style="font-size: 18px;">Se ha detectado un posible escaneo de puertos en tu máquina.</p>
                <p style="font-size: 16px;">Fuente del ataque: <b>{ip_src}</b></p>
                <p style="color: red; font-size: 20px;">¡Podrían estar intentando vulnerar tu sistema!</p>
            </div>
        </body>
    </html>
    """

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body, subtype="html")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_sender, password)
            smtp.send_message(em)
            print("Correo enviado exitosamente")
    except smtplib.SMTPAuthenticationError:
        print("Error de autenticación: Verifique su usuario y contraseña.")
    except smtplib.SMTPRecipientsRefused:
        print("Error: El destinatario ha sido rechazado por el servidor.")
    except smtplib.SMTPException as e:
        print(f"Error al enviar el correo: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    # Enviar mensaje de WhatsApp
    send_whatsapp(ip_src)
