# app/email_sender.py
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Dirección de correo electrónico del remitente
email_sender = os.getenv('SENDER_EMAIL')
# Contraseña del remitente obtenida de las variables de entorno
password = os.getenv('EMAIL_PASSWORD')
# Dirección de correo electrónico del destinatario
email_reciver = os.getenv('RECEIVER_EMAIL')

# Función para enviar un correo electrónico
def send_email(ip_src):
    # Asunto del correo electrónico
    subject = "⚠️ Alerta de Seguridad: Escaneo de Puertos Detectado ⚠️"
    # Cuerpo del correo electrónico en formato HTML
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

    # Crea un objeto EmailMessage para configurar los detalles del correo
    em = EmailMessage()
    # Establece el remitente del correo
    em["From"] = email_sender
    # Establece el destinatario del correo
    em["To"] = email_reciver
    # Establece el asunto del correo
    em["Subject"] = subject
    # Establece el cuerpo del correo en formato HTML
    em.set_content(body, subtype="html")

    # Intenta enviar el correo y maneja posibles excepciones
    try:
        # Conecta con el servidor SMTP de Gmail
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            # Inicia sesión en el servidor SMTP
            smtp.login(email_sender, password)
            # Envía el correo
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
