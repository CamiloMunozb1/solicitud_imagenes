# Funciones importadas de las funcionalidades.
from funciones.busqueda_imagenes import BuscadorImagenes
from funciones.gestor_imagen import GuardarImagen

while True:
    # Menu de usuario.
    print("""
        Bienvenido a la solicitud de imagenes:
            1. Buscar imagenes.
            2. Gestion de imagenes.
            3. Salir
        """)
    try:
        # Entrada de usuario y opciones para la eleccion del usuario.
        usuario = str(input("Ingresa la opcion que desees: ")).strip()
        if not usuario:
            print("El campo debe estar completo.") # Validador de usuario.
            break
        elif usuario == "1":
            imagen = BuscadorImagenes() # Clase principal
            imagen.busqueda_imagen() # Funcion de ejecucion
        elif usuario == "2":
            guardado = GuardarImagen() # Clase principal
            guardado.guardado_imagen() # Funcion de ejecucion.
        elif usuario == "3":
            print("Gracias por usar y solicitar tus imagenes favoritas.") # Salida del programa 
            break
        input("\nPresiona enter para continuar...")
    # Manejo de errores.
    except TypeError:
        print("Error de digitacion, volver a intentar.")
    except Exception as error:
        print(f"Error en el programa : {error}.")