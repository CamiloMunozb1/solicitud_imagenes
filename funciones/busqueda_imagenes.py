import requests # Libreria para las peticiones HTTP a la API.
import os # Libreria para manipular la API_KEY.
from dotenv import load_dotenv # libreria para cargar las variables de entorno.

class BuscadorImagenes:
    def __init__(self):
        load_dotenv() # Carga las variables de entorno.
        self.api_key = os.getenv('API_KEY') # Api_key donde se mandaran las peticiones.
    
    def busqueda_imagen(self):
        try:
            # Entrada de usuario.
            usuario_buscador = input("Ingresa el nombre de la imagen que necesitas: ").strip()
            # Validador de campo.
            if not usuario_buscador:
                print("El campo debe estar completo")

            # Url a donde se llevara a cabo las peticiones.
            url_busqueda = f"https://api.unsplash.com/search/photos?query={usuario_buscador}&client_id={self.api_key}"

            respuesta = requests.get(url_busqueda) # Se abre la informacion de la URL.
            peticion_json = respuesta.json() # Se recibe la informacion en formato Json.
            imagen_encontrada = peticion_json["results"][0]["id"] # Se devuelve la imagen buscada.
            descripcion_imagen = peticion_json["results"][0]["description"] # Se devuelve la informacion de la imagen.
            url_imagen = peticion_json["results"][0]["links"]["download"] # Se devuelve el link de la imagen.
            # Se devuelve al usuario la informacion encontrada.
            print(f"Imagen encontrada : {imagen_encontrada}")
            print(f"Descripcion de la imagen : {descripcion_imagen}")
            print(f"La URL de descarga de la imagen es : {url_imagen}")
        # Manejo de errores.
        except Exception as error:
            print(f"Error en el programa : {error}.")
