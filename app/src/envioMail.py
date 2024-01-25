import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.dataBase.citas import Cita
from dotenv import load_dotenv
import os


def enviar_email_confirmacion(cita: Cita):
        load_dotenv()
        mail = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        if mail is None or password is None:
           return ("Error: Las variables de entorno MAIL y PASSWORD no se cargaron correctamente.")

        # Comprobar que la cita tiene un cliente y un correo electrónico
        if cita.cliente is None or cita.cliente.email is None:
            return("Error: La cita no tiene un cliente o el cliente no tiene un correo electrónico.")

        # Configurar el servidor SMTP
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(mail, password)

        # Crear el mensaje
        mensaje = MIMEMultipart()
        mensaje['From'] = mail
        mensaje['To'] = cita.cliente.email
        mensaje['Subject'] = "Confirmación de cita"

        #  Crear el cuerpo del mensaje
        cuerpo = f"Hola {cita.cliente.nombre},\n\nTu cita ha sido confirmada para el {cita.fecha_inicio}.\n\nGracias,\nTu equipo"
        mensaje.attach(MIMEText(cuerpo, 'plain'))

        # Enviar el correo electrónico
        texto = mensaje.as_string()
        servidor.sendmail(mail, cita.cliente.email, texto)
        servidor.quit()