import requests

class BuscadorImagenes:
    def __init__(self):
        self.api_key = r"TU_API_KEY"
    
    def busqueda_imagen(self):
        try:

            usuario_buscador = input("Ingresa el nombre de la imagen que necesitas: ").strip()
            if not usuario_buscador:
                print("El campo debe estar completo")

            url_busqueda = f"https://api.unsplash.com/search/photos?query={usuario_buscador}&client_id={self.api_key}"

            respuesta = requests.get(url_busqueda)
            peticion_json = respuesta.json()
            imagen_encontrada = peticion_json["results"][0]["id"]
            descripcion_imagen = peticion_json["results"][0]["description"]
            url_imagen = peticion_json["results"][0]["links"]["download"]
            print(f"Imagen encontrada : {imagen_encontrada}")
            print(f"Descripcion de la imagen : {descripcion_imagen}")
            print(f"La URL de descarga de la imagen es : {url_imagen}")

        except Exception as error:
            print(f"Error en el programa : {error}.")
