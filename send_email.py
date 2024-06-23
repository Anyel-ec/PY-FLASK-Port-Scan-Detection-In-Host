import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Dirección de correo electrónico del remitente
email_sender = os.getenv('SENDER')
# Contraseña del remitente obtenida de las variables de entorno
password = os.getenv('PASSWORD')
# Dirección de correo electrónico del destinatario
email_reciver = "appatino@espe.edu.ec"

# Imprime la contraseña para verificar que se ha cargado correctamente
print(f"Contraseña leída: {password}")

# Si la contraseña no se ha cargado (es None), detiene la ejecución con un error
if password is None:
    raise ValueError("No se pudo leer la contraseña del archivo .env")

# Asunto del correo electrónico
subject = "Prueba de envio de correo"
# Cuerpo del correo electrónico
body = "Este es un mensaje de prueba"

# Crea un objeto EmailMessage para configurar los detalles del correo
em = EmailMessage()
# Establece el remitente del correo
em["From"] = email_sender
# Establece el destinatario del correo
em["To"] = email_reciver
# Establece el asunto del correo
em["Subject"] = subject
# Establece el cuerpo del correo
em.set_content(body)

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
