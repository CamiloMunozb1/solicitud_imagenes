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
            if os.path.exists(ruta_imagen):
                ruta_destino = os.path.join(os.path.expanduser("~"),'Imágenes')
                shutil.copy2(ruta_destino)
                print(f"Archivo : {ruta_destino} se traslado exitosamente a {ruta_destino}")
            else:
                print("Imagen no encontrada.")
        except Exception as error:
            print(f"Error en el programa: {error}.")

