import os # Libreria para la interaccion de los archivos dentro del equipo.
import shutil # Libreria para manipulacion de archivos en alto nivel.

class GuardarImagen:
    def __init__(self):
        pass
    def guardado_imagen(self):
        try:
            # Entrada de usuario.
            ruta_imagen = input("Ingresa la ruta de la imagen: ").strip()
            # Validador de campos.
            if not ruta_imagen:
                print("No se pueden tener los campos vacios.")
                return
            if not os.path.isfile(ruta_imagen): # Se revisa que la ruta de la imagen si exista.
                print("La ruta no corresponde a un archivo válido. Asegúrate de que sea una imagen.")
                return
            ruta_destino = os.path.join(os.path.expanduser("~"),'POWER') # Carpeta de destino de la imagen.
            if not os.path.exists(ruta_destino): # Se revisa que la carpeta exista.
                os.makedirs(ruta_destino) # Si no existe la carpeta crea la carpeta.
                nombre_archivo = os.path.basename(ruta_imagen) # Se pasa la ruta de la imagen a la carpeta.
                destino_completo = os.path.join(ruta_destino, nombre_archivo) # Se une la carpeta al archivo.
                shutil.copy2(ruta_imagen,destino_completo) # Se copian los archivos.
                # Se muestran los resultados al usuario
                print('destino real :',destino_completo)
                print(f"Archivo : {ruta_imagen} se traslado exitosamente a {ruta_destino}")
        # Manejo de errores.
        except Exception as error:
            print(f"Error en el programa: {error}.")

