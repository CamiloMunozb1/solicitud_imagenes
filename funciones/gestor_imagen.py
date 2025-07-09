import os
import shutil

class GuardarImagen:
    def __init__(self):
        pass
    def guardado_imagen(self):
        try:
            ruta_imagen = input("Ingresa la ruta de la imagen: ").strip()
            if not ruta_imagen:
                print("No se pueden tener los campos vacios.")
                return
            if not os.path.isfile(ruta_imagen):
                print("La ruta no corresponde a un archivo válido. Asegúrate de que sea una imagen.")
                return
            ruta_destino = os.path.join(os.path.expanduser("~"),'POWER')
            if not os.path.exists(ruta_destino):
                os.makedirs(ruta_destino)
                nombre_archivo = os.path.basename(ruta_imagen)
                destino_completo = os.path.join(ruta_destino, nombre_archivo)
                shutil.copy2(ruta_imagen,destino_completo)
                print('destino real :',destino_completo)
                print(f"Archivo : {ruta_imagen} se traslado exitosamente a {ruta_destino}")
        except Exception as error:
            print(f"Error en el programa: {error}.")

