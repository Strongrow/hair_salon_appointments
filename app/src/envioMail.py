import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.dataBase.citas import Cita


def enviar_email_confirmacion(cita: Cita):
        mail = "crodriguez@bogotamovil.com.co"
        # Configurar el servidor SMTP
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(mail, "Aa1o3o6349oo++-")

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