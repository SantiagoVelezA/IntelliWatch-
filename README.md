# Proyecto de Automatización con Python

## Descripción
Este script monitorea una carpeta, detecta archivos Excel/CSV, los procesa y envía un correo con un resumen de los datos.

## Precondiciones

# Entorno virtual
Crear un entorno virtual "python -m venv env"
Iniciar el entorno virtual ".\Scripts\env\activate"

# Crear carpeta con ficheros src
    "__init__.py"
    "monitor.py"
    "notificacion.py"
    "procesar.py"

# Crear fichero .gitignore
se usa en Git para excluir archivos y carpetas que no deben ser rastreados ni subidos al repositorio.

# COMO FUNCIONA EL CODIGO:
Se ejecuta la funcion <"python main.py"> para que se el sistema empiece a monitorear que un archivo se agrege en la carpeta .\archivos_entrada
from src.monitor import iniciar_monitoreo
if __name__ == "__main__":
    print("Iniciando monitoreo de la carpeta...")
    iniciar_monitoreo()