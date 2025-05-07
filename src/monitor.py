import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src.procesar import procesar_archivo

CARPETA_ENTRADA = "./archivos_entrada/"
EXTENSIONES_PERMITIDAS = [".csv", ".xlsx"]

def esperar_archivo_disponible(ruta_archivo, intentos=5, espera=1):
    """Intenta acceder al archivo varias veces antes de rendirse"""
    for _ in range(intentos):
        if os.path.exists(ruta_archivo):
            try:
                with open(ruta_archivo, "rb") as f:
                    return True
            except PermissionError:
                pass
        time.sleep(espera)
    return False

class MonitorCarpeta(FileSystemEventHandler):
    def on_created(self, event):
        ruta_archivo = event.src_path
        archivo = os.path.basename(ruta_archivo)

        if archivo.startswith("~$"):  # Ignorar archivos temporales de Excel
            print(f"Ignorando archivo temporal: {archivo}")
            return

        if not archivo.lower().endswith(tuple(EXTENSIONES_PERMITIDAS)):
            print(f"Archivo no compatible: {archivo}")
            return

        print(f"Nuevo archivo detectado: {ruta_archivo}")

        if esperar_archivo_disponible(ruta_archivo):
            procesar_archivo(ruta_archivo)
        else:
            print(f"No se pudo acceder al archivo después de varios intentos: {ruta_archivo}")

def iniciar_monitoreo():
    # Lo que hacemos aqui es validar si la carpeta de entrada existe, si no existe la creamos
    if not os.path.exists(CARPETA_ENTRADA):
        os.makedirs(CARPETA_ENTRADA)

    event_handler = MonitorCarpeta()
    observer = Observer()
    observer.schedule(event_handler, CARPETA_ENTRADA, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()