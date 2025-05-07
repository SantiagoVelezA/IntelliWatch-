import pandas as pd
import os
import json
import time
from src.notificacion import enviar_correo

CARPETA_REPORTES = "./reportes/"

def procesar_archivo(ruta_archivo):
    try:
        print(f"Procesando archivo: {ruta_archivo}")
        
        # Cargar el archivo
        if ruta_archivo.endswith(".csv"):
            df = pd.read_csv(ruta_archivo)
        else:
            df = pd.read_excel(ruta_archivo)

        # Generar resumen del archivo
        resumen = {
            "Nombre del archivo": os.path.basename(ruta_archivo),
            "Filas": df.shape[0],
            "Columnas": df.shape[1],
            "Encabezados": df.columns.tolist()
        }

        if not os.path.exists(CARPETA_REPORTES):
            os.makedirs(CARPETA_REPORTES)

        # Guardar resumen en JSON
        timestamp = int(time.time())
        ruta_reporte = os.path.join(CARPETA_REPORTES, f"resumen_{timestamp}.json")
        
        with open(ruta_reporte, "w", encoding="utf-8") as f:
            json.dump(resumen, f, indent=4, ensure_ascii=False)

        print(f"Resumen guardado en: {ruta_reporte}")

        # Enviar notificación por correo
        enviar_correo(ruta_reporte)

    except Exception as e:
        print(f"Error procesando el archivo: {e}")