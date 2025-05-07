import smtplib
import json
from email.message import EmailMessage

# Configuración del correo
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_EMISOR = "svelezacevedo3@gmail.com"
EMAIL_PASSWORD = "dxiu tzgp morr bavn "
EMAIL_DESTINATARIO = "svelezacevedo3@gmail.com"

def enviar_correo(ruta_reporte):
    try:
        # Leer el resumen del archivo JSON
        with open(ruta_reporte, "r", encoding="utf-8") as f:
            contenido = json.load(f)

        # Crear el mensaje de correo
        mensaje = EmailMessage()
        mensaje["Subject"] = f"Resumen del archivo {contenido['Nombre del archivo']}"
        mensaje["From"] = EMAIL_EMISOR
        mensaje["To"] = EMAIL_DESTINATARIO
        mensaje.set_content(f"""
        Se ha procesado un nuevo archivo.
        Nombre: {contenido['Nombre del archivo']}
        Filas: {contenido['Filas']}
        Columnas: {contenido['Columnas']}
        Encabezados: {", ".join(contenido['Encabezados'])}
        """)

        # Conectar al servidor SMTP y enviar correo
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as servidor:
            servidor.starttls()  # Seguridad
            servidor.login(EMAIL_EMISOR, EMAIL_PASSWORD)
            servidor.send_message(mensaje)

        print("Correo enviado exitosamente.")
    
    except Exception as e:
        print(f"Error al enviar correo: {e}")